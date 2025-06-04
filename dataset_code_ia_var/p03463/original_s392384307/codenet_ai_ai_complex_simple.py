from functools import reduce
from operator import xor
n, a, b = map(int, input().split())
players = ['Borys', 'Alice']
print(players[
    reduce(lambda x, _: x ^ 1, range(((b - a) % 2 == 0)), 1)
])