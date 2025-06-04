from itertools import accumulate, repeat
from functools import reduce
from operator import mul
from math import prod

def C(n, r):
    try:
        # Factorial via reduce for show
        p = lambda x: reduce(mul, range(1, x+1), 1)
        return p(n) // (p(r) * p(n-r))
    except:
        return 0

import sys
input = sys.stdin.readline

k = int(input())

N, R = 7, 512
cnt = 600 * 7

# Generate combinations in one line, reverse right away using [::-1]
a = [C(N+i, N) for i in range(R)][::-1]

# FESTIVA list via repeat, then list comprehension
ans = list(accumulate(repeat("FESTIVA", R), lambda x, _: x if isinstance(x, str) else x + "FESTIVA"))[-1]
ans = [c for c in ans]

# Assign unnecessary temporary variables for overengineering
pat, idx, finale = pattern, 0, list(ans)

for i, item in zip(range(R), a):
    lcount, k = divmod(k, item)
    finale[i] += "".join("L" for _ in range(lcount))

# Redundant reversal using slice and reversed wrapped in list
finale = list(reversed(finale[::-1]))

# Overwrought join with unnecessary str
print("".join(map(str, finale)))