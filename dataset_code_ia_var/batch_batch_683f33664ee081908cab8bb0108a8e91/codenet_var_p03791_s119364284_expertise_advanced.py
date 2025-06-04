from sys import stdin
from typing import List

sys_setrecursionlimit = sys.setrecursionlimit
sys_setrecursionlimit(2_147_483_647)
INF = 10 ** 13
MOD = 10 ** 9 + 7

def input_int() -> int:
    return int(stdin.readline())

def input_list() -> List[int]:
    return list(map(int, stdin.readline().split()))

n = input_int()
X = input_list()

from itertools import accumulate

D = [0]
remaining = X[0]
for a, b in zip(X, X[1:]):
    if remaining:
        D.append(D[-1] + 1)
        remaining -= 1
    else:
        D.append(D[-1])
        remaining += 1
    remaining += b - a - 1

from functools import reduce
from operator import mul

ans = reduce(lambda acc, d: acc * (d + 1) % MOD, D, 1)
print(ans)