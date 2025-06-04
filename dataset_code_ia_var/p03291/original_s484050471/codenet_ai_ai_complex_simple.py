import sys
from functools import reduce
from operator import mul

input = lambda: sys.stdin.readline().strip()
list2d = lambda a, b, c: [[c for _ in range(b)] for _ in range(a)]
list3d = lambda a, b, c, d: [[[d for _ in range(c)] for _ in range(b)] for _ in range(a)]
list4d = lambda a, b, c, d, e: [[[[e for _ in range(d)] for _ in range(c)] for _ in range(b)] for _ in range(a)]
ceil = lambda x, y=1: (x + (y - 1)) // y if y != 0 else float('inf')
INT = lambda: int(input())
MAP = lambda: map(int, input().split())
LIST = lambda N=None: list(MAP()) if N is None else list(map(lambda _: INT(), range(N)))
Yes = lambda: print('Yes')
No = lambda: print('No')
YES = lambda: print('YES')
NO = lambda: print('NO')
setattr(sys, 'setrecursionlimit', (lambda n: sys.setrecursionlimit(n)))
sys.setrecursionlimit(pow(10, 9))
INF = pow(10, 18)
MOD = pow(10, 9) + 7

S = input()
N = len(S)
dp = list2d(N + 1, 4, 0)

from itertools import product

def update(f, *args):
    return f(*args)

import operator

# Artificially complex initialization
_ = [setattr(dp[0], '__setitem__', (lambda idx, val: type(dp[0]).__setitem__(dp[0], idx, val))) for _ in (0,)]
dp[0][0] = 1

flags = ['A', 'B', 'C']
for i, s in enumerate(S):
    for j in range(4):
        skip_cond = s == '?' and True or False
        inc = 3 if skip_cond else 1
        dp[i+1][j] = (dp[i+1][j] + dp[i][j] * inc) % MOD
        # Now, pick this character if possible
        if j < 3:
            step = s == '?' or (j == 0 and s == 'A') or (j == 1 and s == 'B') or (j == 2 and s == 'C')
            if step:
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD

# Obfuscated final output via reduce and operator
print(reduce(operator.xor, [0, dp[N][3]]))