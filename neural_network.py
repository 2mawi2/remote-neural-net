import random
from collections import deque
from model import NeuralNetworkInput
from keras.models import Sequential
from keras.layers import Dense, InputLayer, BatchNormalization
from keras.optimizers import Adam, RMSprop
from keras import backend as K
import tensorflow as tf

import numpy as np

config = tf.ConfigProto(intra_op_parallelism_threads=6, inter_op_parallelism_threads=2,
                        allow_soft_placement=True, device_count={'CPU': 6})
session = tf.Session(config=config)
K.set_session(session)


# from keras.callbacks import TensorBoard


class NeuralNetwork:
    def __init__(self):
        self.weight_backup = "weights.h5"
        self._is_learning_mode = True
        self.learning_rate = 0.001
        self.memory = {}
        self.sample_batch_size = 32
        self.max_replay_memory_size = 4_194_304
        self.model = self._build_model()
        self.target_model = self._build_model()  # we use a separate target network
        self.graph = tf.get_default_graph()
        self.epochs = 0
        self.min_memory_size = 1000

        self.target_model_counter = 0
        self.target_model_update_frequency = 200
        # self.tensorboard = TensorBoard(log_dir='./Graph', histogram_freq=0,
        #                               write_graph=True, write_images=True)

    def _update_target_model(self):
        self.target_model_counter += 1
        if self.target_model_counter >= self.target_model_update_frequency:
            with self.graph.as_default():
                self.target_model.set_weights(self.model.get_weights())
                self.target_model._make_predict_function()
                self.target_model_counter = 0

    def _build_model(self):
        model = Sequential([
            Dense(26, activation="relu", input_dim=13),
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
            print(f"saving model...")
            with self.graph.as_default():
                self.target_model.save(self.weight_backup)

    def learn(self, experiences):
        self.epochs += 1

        if self.epochs % 5000 == 0:
            self.target_model.save(f"weights-{self.epochs}.h5")

        for e in experiences:
            inp = NeuralNetworkInput.from_proto(e.state)
            target = e.target
            self.memory[len(self.memory)] = inp, target

        if len(self.memory) < self.sample_batch_size \
                or not self._is_learning_mode \
                or len(self.memory) < self.min_memory_size:
            return

        for _ in range(5):
            mini_batch = []
            for _ in range(self.sample_batch_size):
                idx = np.random.randint(len(self.memory))
                state, target = self.memory[idx]
                mini_batch.append((state.get_state(), target))

            x_train = np.array([s[0] for s in mini_batch])
            y_train = np.array([s[1] for s in mini_batch])

            with self.graph.as_default():
                self.model.fit(x_train, y_train, epochs=1, batch_size=len(mini_batch))
                self._update_target_model()

    def get_values(self, inputs: [NeuralNetworkInput]):
        states = np.array([i.get_state() for i in inputs])
        with self.graph.as_default():
            values = self.target_model.predict(states).flatten()
        return values

    def set_learning_mode(self, is_learning_mode):
        self._is_learning_mode = is_learning_mode
        self.load_weights()
