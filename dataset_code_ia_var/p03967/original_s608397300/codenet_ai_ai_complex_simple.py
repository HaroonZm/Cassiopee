from functools import reduce
from operator import add, sub

S = input()
states = []
spin, res = 0, 0
actions = {
    'g': lambda x: (x[0] - 1, x[1] + 1) if x[0] > 0 else (x[0] + 1, x[1]),
    'p': lambda x: (x[0] - 1, x[1]) if x[0] > 0 else (x[0] + 1, x[1] - 1),
}

def f(acc, ch):
    return actions[ch](acc)

final = reduce(f, S, (0,0))
print(final[1])