import random
from collections import deque
import tensorflow as tf
from model import NeuralNetworkInput
from keras.models import Sequential
from keras.layers import Dense, InputLayer, BatchNormalization
from keras.optimizers import Adam, RMSprop
import numpy as np


# from keras.callbacks import TensorBoard


class NeuralNetwork:
    def __init__(self):
        self.weight_backup = "weights.h5"
        self._is_learning_mode = True
        self.learning_rate = 0.0025
        self.memory = np.ndarray(shape=(0, 2))
        self.sample_batch_size = 32
        self.max_replay_memory_size = 4_194_304
        self.model = self._build_model()
        self.target_model = self._build_model()  # we use a separate target network
        self.load_weights()
        self.graph = tf.get_default_graph()

        self.target_model_counter = 0
        self.target_model_update_frequency = 1
        # self.tensorboard = TensorBoard(log_dir='./Graph', histogram_freq=0,
        #                               write_graph=True, write_images=True)

    def _update_target_model(self):
        self.target_model_counter += 1
        if self.target_model_counter > self.target_model_update_frequency:
            with self.graph.as_default():
                self.target_model.set_weights(self.model.get_weights())
                self.target_model._make_predict_function()
                self.target_model_counter = 0

    def _build_model(self):
        model = Sequential([
            Dense(26, activation="relu", input_dim=13),
            Dense(26, activation="relu"),
            Dense(26, activation="relu"),
            # Dense(26, activation="relu"),
            Dense(1, activation='linear'),
        ])
        model._make_predict_function()  # prebuild for concurrency
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate), metrics=['acc'])

        return model

    def load_weights(self):
        if not self._is_learning_mode:
            print("loading weight backup...")
            with self.graph.as_default():
                self.model.load_weights(self.weight_backup)
                self.target_model.load_weights(self.weight_backup)

                self.model._make_predict_function()
                self.target_model._make_predict_function()

    def save_model(self):
        if self._is_learning_mode:
            with self.graph.as_default():
                self.target_model.save(self.weight_backup)

    def learn(self, experiences):
        for e in experiences:
            inp = NeuralNetworkInput.from_proto(e.state)
            target = e.target

            # contains check really expensive, TODO find faster workaround
            # if not np.all(np.any(np.isin(self.memory, [inp, target]), axis=0)):

            if len(self.memory) > self.max_replay_memory_size:
                self.memory = np.delete(self.memory, 0, axis=0)
            self.memory = np.append(self.memory, [[inp, target]], axis=0)

        if len(self.memory) < self.sample_batch_size or not self._is_learning_mode:
            return

        for _ in range(5):
            idx = np.random.randint(len(self.memory), size=self.sample_batch_size)
            mini_batch = self.memory[idx, :]
            x_train = np.array([s[0].get_state() for s in mini_batch])
            y_train = np.array([s[1] for s in mini_batch])

            with self.graph.as_default():
                self.model.fit(x_train, y_train, epochs=1,
                               batch_size=len(mini_batch))
                self._update_target_model()

    def get_values(self, inputs: [NeuralNetworkInput]):
        states = np.array([i.get_state() for i in inputs])
        with self.graph.as_default():
            values = self.target_model.predict(states).flatten()
        return values

    def set_learning_mode(self, isTraining):
        self._is_learning_mode = isTraining
        self.load_weights()
