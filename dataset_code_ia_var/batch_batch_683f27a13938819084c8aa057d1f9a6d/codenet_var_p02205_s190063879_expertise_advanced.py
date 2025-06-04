from functools import reduce
from operator import add, sub

n = int(input())
a, b = map(int, input().split())
ops = [lambda x, y: (x[0], x[1] + x[0]), lambda x, y: (x[0] - x[1], x[1])]
s = n % 12

def step(state, i):
    if i % 2 == 0:
        return state[0], state[0] + state[1]
    else:
        return state[0] - state[1], state[1]

a, b = reduce(step, range(1, s + 1), (a, b))
print(a, b)