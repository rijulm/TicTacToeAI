EMPTY = None

a = [[EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY]]

action = (1,0)
from tictactoe import actions, result
print(actions(a))

print(result(a, action))
print(result(result(a, action), action))

