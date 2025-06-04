import sys
import math
from collections import deque
import copy
from functools import reduce
from operator import __add__

MOD = 10 ** 9 + 7

H, W = map(int, sys.stdin.readline().split())

wall = "#"
padding = lambda n: [wall] * n

layers = list(
    map(
        lambda line: list(map(lambda x: x, (wall + line.rstrip() + wall))),
        [sys.stdin.readline() for _ in range(H)]
    )
)
a = [padding(W + 2)] + layers + [padding(W + 2)]

dp = copy.deepcopy([[0]* (W + 10) for _ in range(H + 10)])

get = lambda m, i, j: m[i][j]
setcell = lambda m, i, j, v: m[i].__setitem__(j, v)

setcell(dp, 0, 1, 1)

list(
    map(
        lambda i: list(
            map(
                lambda j: (
                    get(a, i, j) != wall and setcell(
                        dp, i, j,
                        ((get(dp, i, j - 1) + get(dp, i - 1, j)) % MOD)
                    )
                ),
                range(1, W + 1)
            )
        ),
        range(1, H + 1)
    )
)

print(reduce(lambda acc, val: val, [get(dp, H, W)], 0) % MOD)