"""Train a neural network for predicting a chess player's Elo rating.

Example usage:
    python3 train_model.py  \
      --dataset_dir json_dataset/  \
      --output_dir trained_model/  \
      --batch_size 32
      --num_epochs 50
"""

import argparse

from training_loop.data_generator import DataGenerator
from training_loop.neural_network import EloPredictionModel

GAME_LENGTH = 100


def main(dataset_dir: str,
         output_dir: str,
         batch_size: int,
         num_epochs: int
         ) -> None:
    train_gen = DataGenerator(dataset_dir, batch_size, GAME_LENGTH)
    model = EloPredictionModel(GAME_LENGTH)

    model.fit(train_gen, epochs=num_epochs)
    model.save(output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset_dir', type=str, required=True)
    parser.add_argument('-o', '--output_dir', type=str, required=True)

    parser.add_argument('-b', '--batch_size', type=int, default=32)
    parser.add_argument('-e', '--num_epochs', type=int, default=50)

    args = parser.parse_args()
    main(args.dataset_dir,
         args.output_dir,
         args.batch_size,
         args.num_epochs)
