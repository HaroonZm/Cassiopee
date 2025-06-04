from functools import reduce
from operator import add

n = int(input())
result = []

def next_step(pair):
    x, acc = pair
    if x == 0:
        return (0, acc)
    digit = - (x % -2)
    next_x = (x - digit) // -2
    acc.append(str(digit))
    return (next_x, acc)

def compute(n):
    if n == 0:
        print(0)
        return
    state = (n, [])
    while state[0] != 0:
        state = next_step(state)
    # Reversing with reduce just for fun
    rev = reduce(lambda x, y: [y] + x, state[1], [])
    print(''.join(rev))

compute(n)