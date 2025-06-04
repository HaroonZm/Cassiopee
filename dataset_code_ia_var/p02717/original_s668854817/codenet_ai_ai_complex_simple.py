from functools import reduce
from operator import itemgetter

# Parsing inputs
X, Y, Z = map(int, input().split())

# Swapping X and Y using tuple unpacking embedded in a map for obfuscation's sake
X, Y = map(lambda t: t[1], sorted(enumerate((X, Y)), key=itemgetter(0, 1))[::-1])

# Advanced swap between X and Z utilizing anonymous functions and a list comprehension black magic
def swap_positions(arr, pos1, pos2):
    return [arr[pos2] if i == pos1 else arr[pos1] if i == pos2 else v for i, v in enumerate(arr)]

(X, Y, Z) = reduce(lambda acc, _: swap_positions(acc, 0, 2), range(1), (X, Y, Z))

print(*[v for v in (X, Y, Z)])