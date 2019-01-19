import random
from collections import deque

from model import NeuralNetworkInput
from keras.models import Sequential
from keras.layers import Dense, InputLayer
from keras.optimizers import Adam, RMSprop
#from keras.callbacks import TensorBoard
import numpy as np


class NeuralNetwork:
    def __init__(self):
        self.weight_backup = "weights.h5"
        self.is_learning_mode = True
        self.learning_rate = 0.01
        self.memory = deque(maxlen=1024)  # buffer for memory replay
        self.sample_batch_size = 32
        self.model = self._build_model()
        self.target_model = self._build_model()  # we use a separate target network
        self.target_model_counter = 0
        self.target_model_update_frequency = 10
        #self.tensorboard = TensorBoard(log_dir='./Graph', histogram_freq=0,
        #                               write_graph=True, write_images=True)

    def _update_target_model(self):
        self.target_model_counter += 1
        # we update the target model after a batch
        if self.target_model_counter > self.target_model_update_frequency:
            self.target_model.set_weights(self.model.get_weights())
            self.target_model_counter = 0

    def _build_model(self):
        model = Sequential([  # 6 - 12 - 1
            Dense(18, activation="relu", input_dim=6),
            Dense(18, activation="relu"),
            Dense(18, activation="relu"),
            # Dense(18, activation="relu"),
            Dense(1, activation='linear'),
        ])

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate), metrics=['acc'])

        if not self.is_learning_mode:
            model.load_weights(self.weight_backup)

        return model

    def save_model(self):
        self.target_model.save(self.weight_backup)

    def learn(self, inp: NeuralNetworkInput, target: float):
        self.memory.append((inp, target))

        if len(self.memory) < self.sample_batch_size or not self.is_learning_mode:  # or self.batch_counter < self.sample_batch_size:
            return

        sample_batch = random.sample(self.memory, self.sample_batch_size)
        x_train = np.array([s.get_state() for s, _ in sample_batch])
        y_train = np.array([t for _, t in sample_batch])
        self.model.fit(x_train, y_train, epochs=1, batch_size=len(sample_batch))#, callbacks=[self.tensorboard])
        self._update_target_model()

    def get_value(self, inp: NeuralNetworkInput):
        return self.target_model.predict(np.array([inp.get_state()]))[0][0]
