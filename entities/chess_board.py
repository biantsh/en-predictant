"""Module providing utilities for working with a chess board."""

import chess
import numpy as np


class ChessBoard(chess.Board):
    def to_tensor(self, piece_values: dict, normalize=False) -> np.ndarray:
        board_state = repr(str(self))
        board_state = board_state.replace('\\n', ' ').replace('\'', '')

        for piece, value in piece_values.items():
            board_state = board_state.replace(piece, value)

        board_tensor = np.fromstring(board_state, sep=' ')
        board_tensor = board_tensor.reshape((8, 8))

        if normalize:
            board_tensor /= np.max(board_tensor)

        return board_tensor
