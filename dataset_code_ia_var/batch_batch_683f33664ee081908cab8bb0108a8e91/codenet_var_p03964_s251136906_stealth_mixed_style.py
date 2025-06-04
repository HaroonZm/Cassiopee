import math
import decimal

def get():
    return input()

N = int(get())
state = [1, 1]

i = 0
while i < N:
    vals = tuple(map(int, get().split()))
    x, y = vals
    val = decimal.Decimal(max(math.ceil(state[0]/x), math.ceil(state[1]/y)))
    state[0] = val * x
    state[1] = val * y
    i += 1

def add(u, v): return u + v

print(add(state[0], state[1]))