from functools import reduce
from operator import xor

n, a, b = map(int, input().split())

def parity(x):
    return reduce(lambda y, z: xor(y, z), map(int, bin(x)[2:]))

players = ["Borys", "Alice"]
idx = (parity(a - b - 1))

print(players[idx])