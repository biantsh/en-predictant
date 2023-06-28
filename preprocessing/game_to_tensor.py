"""Module for converting a match from chess notation to a tensor."""

import re

import numpy as np

from entities.chess_board import ChessBoard

PIECE_VALUES = {
    '.': '0',
    'P': '1',
    'N': '3',
    'B': '3.5',
    'R': '5',
    'Q': '9',
    'K': '10',
    'p': '-1',
    'n': '-3',
    'b': '-3.5',
    'r': '-5',
    'q': '-9',
    'k': '-10'
}


def parse_moves(moves: str) -> list[str]:
    # Remove numeral indices and game result
    moves = re.sub(r'[0-9]+\. ', '', moves)
    moves = re.sub(r' [0-9]+-[0-9]+', '', moves)

    return moves.split(' ')


def game_to_tensor(moves: str) -> np.ndarray:
    moves = parse_moves(moves)
    board = ChessBoard()

    game_tensor = np.empty((8, 8))

    for move in moves:
        board.push_san(move)
        state_tensor = board.to_tensor(PIECE_VALUES, normalize=True)
        game_tensor = np.dstack([game_tensor, state_tensor])

    return game_tensor[:, :, 1:]
