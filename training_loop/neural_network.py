"""Dummy Keras model for predicting a chess player's Elo rating."""

import keras
from keras import layers


class EloPredictionModel(keras.Sequential):
    def __init__(self, game_length: int) -> None:
        super().__init__([
            layers.BatchNormalization(input_shape=(8, 8, game_length)),
            layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D(pool_size=2, strides=2),

            layers.BatchNormalization(),
            layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D(pool_size=2, strides=2),

            layers.BatchNormalization(),
            layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D(pool_size=2, strides=2),

            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(1, activation='linear')
        ])

        self.compile(loss='mean_squared_error',
                     optimizer='adam',
                     metrics=['mae'])
