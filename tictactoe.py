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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possiblemoves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possiblemoves.append((i, j))

    # raise NotImplementedError
    return set(possiblemoves)


class IllegalMove(Exception):
    pass


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)

    piece = player(board)
    if newboard[action[0]][action[1]] != EMPTY:
        print('error found')
        raise IllegalMove


    else:
        newboard[action[0]][action[1]] = piece

    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    finalpiece = EMPTY
    isWon = False

    # first we can check horizontally
    for row in board:
        if len(set(row)) == 1:
            isWon = True
            finalpiece=  row[0]

    # check diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == board[2][2]:
        # first diagonal
        isWon = True
        finalpiece = board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == board[2][0]:
        # second diagonal
        isWon = True
        finalpiece = board[0][2]

    # to check vertically
    for i in range(3):
        total = []
        for column in board:
            total.append(column[i])
        if len(set(total)) == 1:
            isWon = True
            finalpiece = total[0]

    if isWon:
        return finalpiece
    else:
        return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check two states - winner or cells full


    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
