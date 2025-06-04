from functools import reduce
from operator import add, mul
from itertools import combinations, product

n = int(input())

# Première partie
def f(k):
    return ((k - 1) * (k - 2) + (k - 1)) // 2

def g(k):
    return k * (k - 2) // 2

actions = [lambda x: print(f(x)), lambda x: print(g(x))]
[actions[(1 - n % 2)](n)]

# Deuxième partie
S = set(combinations(range(1, n + 1), 2))
excl = set(filter(lambda pair: sum(pair) == n - 2 + (0 if n % 2 else 1) + 2, S))
included = S - excl
[list(map(lambda pair: print(*pair), sorted(included)))]