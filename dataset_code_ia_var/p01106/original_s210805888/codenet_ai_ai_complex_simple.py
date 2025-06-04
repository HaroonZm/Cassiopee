from functools import reduce
from operator import add, xor, itemgetter
from collections import deque
import sys

sys.setrecursionlimit(10**6)

INF, MOD = 10**18, 10**9 + 7

def bits(n):  # List of 2^i for i in (n-1)...0
    return list(map(lambda k: 2 ** k, range(n-1, -1, -1)))

def y_sequence(n, y):
    # Generate ys as per the process, but using reductions and mapping
    seq = list(zip(bits(n), range(1, n)))
    def step(acc, tup):
        exp, idx = tup
        prev_y = acc[0]
        new_y = abs(exp - prev_y + 1) if prev_y <= exp else prev_y - exp
        return (new_y, [new_y] + acc[1])
    return reduce(lambda a, b: step(a, b), reversed(list(zip(bits(n - 1), range(1, n)))), (y, [y]))[1]

def decision(x, y, yi, i, n):
    sz = 2 ** (n - i)
    arg1 = x > sz // 2
    arg2 = (y + 2 ** i) == yi
    return "R" if xor(arg1, arg2) else "L"

def transform_x(x, c, sz):
    return {
        ("L", True): lambda x: sz // 2 - x + 1,
        ("L", False): lambda x: x - sz // 2,
        ("R", True): lambda x: sz - x + 1,
        ("R", False): lambda x: x,
    }[(c, x <= sz // 2 if c == "L" else x > sz // 2)](x)

for line in iter(lambda: sys.stdin.readline(), ''):
    try:
        n, y, x = map(int, line.strip().split())
    except Exception:
        continue
    if n == 0: break
    ys = y_sequence(n, y)
    ans = deque()
    for i in map(itemgetter(0), enumerate(range(n))):
        sz = 2 ** (n - i)
        c = decision(x, 1 if i == 0 else ys[i-1], ys[i], i, n)
        x = transform_x(x, c, sz)
        ans.append(c)
    print(''.join(ans))