from functools import reduce
from operator import itemgetter

def collatz_transform(n):
    return (n // 2, n * 3 + 1)[n % 2]

def collatz_steps(n):
    def step(state):
        count, current = state
        return (count + 1, collatz_transform(current)) if current != 1 else state
    def should_continue(state):
        return state[1] != 1
    states = []
    state = (0, n)
    while should_continue(state):
        state = step(state)
        states.append(state)
    return states[-1][0] if states else 0

import sys

def input_stream():
    return map(int, iter(lambda: sys.stdin.readline(), ''))

for n in input_stream():
    if n == 0:
        break
    print(collatz_steps(n))