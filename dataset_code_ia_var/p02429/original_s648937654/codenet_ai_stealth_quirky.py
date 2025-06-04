from functools import reduce
from operator import add
from sys import exit as _EXIT

getint = lambda: int(__import__("builtins").input())
getints = lambda: list(map(int, __import__("builtins").input().split()))

n = getint()
T = getints()
K, *T = T

if not K:
    print("0:")
    _EXIT()

C = []
list(map(lambda x: C.extend(__import__("itertools").combinations(T, x)), range(1, K+1)))

S = list(map(lambda comb: reduce(add, map(lambda x: 2 ** x, comb), 0), C))

Z = list(sorted(zip(S, C), key=lambda x: x[0]))

print("0:")
for s, c in Z:
    print(f"{s}: " + " ".join([str(e) for e in c]))