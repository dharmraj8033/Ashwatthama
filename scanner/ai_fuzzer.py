import tensorflow as tf
import numpy as np
from random import choice

class AIFuzzer:
    def __init__(self, patterns):
        self.patterns = patterns
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(10,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(len(self.patterns), activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def generate_payload(self):
        input_data = np.random.rand(1, 10)
        probabilities = self.model.predict(input_data)
        chosen_index = np.argmax(probabilities)
        return self.patterns[chosen_index]
