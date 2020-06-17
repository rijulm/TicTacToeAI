EMPTY = None

a = [[EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY]]

action = (1,0)
from tictactoe import actions, result, winner
print(actions(a))
print(winner(a))

print(result(a, action))
print(result(result(a, action), action))


"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)


    helper.calls = 0
    helper.__name__ = func.__name__

    return helper


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


@call_counter
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    elif player.calls % 2 == 0:
        return O
    else:
        return X

    # raise NotImplementedError


