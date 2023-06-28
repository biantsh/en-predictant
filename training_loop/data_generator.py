import glob
import json
import math
import random

import numpy as np
import tensorflow as tf

from preprocessing.game_to_tensor import game_to_tensor


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self,
                 dataset_dir: str,
                 batch_size: int,
                 game_length: int
                 ) -> None:
        self.json_paths = glob.glob(f'{dataset_dir}/*.json')
        self.batch_size = batch_size
        self.game_length = game_length

    def __len__(self) -> int:
        return math.ceil(len(self.json_paths) / self.batch_size)

    def __getitem__(self, idx: int) -> tuple[np.ndarray, np.ndarray]:
        batch_x, batch_y = [], []

        idx_start = idx * self.batch_size
        idx_end = idx_start + self.batch_size
        idx_end = min(idx_end, len(self.json_paths))

        for json_path in self.json_paths[idx_start:idx_end]:
            game_tensor, elo = self._load_json(json_path)

            batch_x.append(game_tensor)
            batch_y.append(elo)

        return np.array(batch_x), np.array(batch_y)

    def _load_json(self, json_path: str) -> tuple[np.ndarray, np.ndarray]:
        with open(json_path, 'r') as json_file:
            game_content = json.load(json_file)

        moves = game_content['Moves']
        game_tensor = game_to_tensor(moves, self.game_length)

        elo = game_content['WhiteElo']
        elo = np.array(int(elo)).reshape(1)

        return game_tensor, elo

    def on_epoch_end(self) -> None:
        random.shuffle(self.json_paths)
