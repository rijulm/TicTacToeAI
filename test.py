EMPTY = None

a = [['a', EMPTY, EMPTY],
    ['a', EMPTY, EMPTY],
     ['a', EMPTY, EMPTY]]

action = (1,0)
from tictactoe import actions, result, winner
print(actions(a))
print(winner(a))

print(result(a, action))
print(result(result(a, action), action))

