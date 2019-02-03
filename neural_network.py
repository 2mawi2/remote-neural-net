import random
from collections import deque

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
        self.memory = deque(maxlen=32)
        self.sample_batch_size = 32
        # self.raising_batch = 1024
        self.model = self._build_model()
        self.target_model = self._build_model()  # we use a separate target network
        self.load_weights()

        self.target_model_counter = 0
        self.target_model_update_frequency = 1
        # self.tensorboard = TensorBoard(log_dir='./Graph', histogram_freq=0,
        #                               write_graph=True, write_images=True)

    def _update_target_model(self):
        self.target_model_counter += 1
        if self.target_model_counter > self.target_model_update_frequency:
            self.target_model.set_weights(self.model.get_weights())
            self.target_model_counter = 0

    def _build_model(self):
        model = Sequential([
            Dense(22, activation="relu", input_dim=9),
            Dense(22, activation="relu"),
            Dense(22, activation="relu"),
            Dense(1, activation='linear'),
        ])
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate), metrics=['acc'])
        return model

    def load_weights(self):
        if not self._is_learning_mode:
            print("loading weight backup...")

            self.model.load_weights(self.weight_backup)
            self.target_model.load_weights(self.weight_backup)

    def save_model(self):
        if self._is_learning_mode:
            self.target_model.save(self.weight_backup)

    def learn(self, inp: NeuralNetworkInput, target: float):
        if (inp, target) not in self.memory:
            self.memory.append((inp, target))

        if len(self.memory) < self.sample_batch_size or not self._is_learning_mode:
            return

        sample_batch = random.sample(self.memory, self.sample_batch_size)
        x_train = np.array([s.get_state() for s, _ in sample_batch])
        y_train = np.array([t for _, t in sample_batch])
        self.model.fit(x_train, y_train, epochs=10, batch_size=len(sample_batch))  # , callbacks=[self.tensorboard])
        self._update_target_model()

        # self.sample_batch_size += self.raising_batch
    def get_values(self, inputs: [NeuralNetworkInput]):
        states = np.array([i.get_state() for i in inputs])
        values = self.target_model.predict(states).flatten()
        return values

    def set_learning_mode(self, isTraining):
        self._is_learning_mode = isTraining
        self.load_weights()
