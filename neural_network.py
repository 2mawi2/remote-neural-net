import random
from collections import deque

from model import NeuralNetworkInput
from keras.models import Sequential
from keras.layers import Dense, InputLayer
from keras.optimizers import Adam
import numpy as np


class NeuralNetwork:
    def __init__(self):
        self.weight_backup = "weights.h5"
        self.test_mode = False
        self.learning_rate = 0.001
        self.memory = deque(maxlen=5000)  # buffer for memory replay
        self.sample_batch_size = 32
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([  # 6 - 12 - 12 - 12 - 1
            Dense(12, activation="relu", input_dim=6),
            Dense(12, activation='relu'),
            Dense(12, activation='relu'),
            Dense(1, activation='linear'),
        ])

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate), metrics=['acc'])

        if self.test_mode:
            model.load_weights(self.weight_backup)

        return model

    def _save_model(self):
        self.model.save(self.weight_backup)

    def learn(self, inp: NeuralNetworkInput, target: float):
        self.memory.append((inp, target))

        if len(self.memory) < self.sample_batch_size or self.test_mode:
            return

        sample_batch = random.sample(self.memory, self.sample_batch_size)

        for inp, target in sample_batch:
            state = np.array([inp.get_state()])
            target_f = target - self.model.predict(state)[0]

            history = self.model.fit(state, target_f, epochs=1, verbose=0)

            if len(history.history) > 0:
                print(f"msa: {history.history['loss']}")

    def get_value(self, inp: NeuralNetworkInput):
        return self.model.predict(np.array([inp.get_state()]))
