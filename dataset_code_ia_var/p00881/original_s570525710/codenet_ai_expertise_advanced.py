from collections import Counter
from sys import stdin
from functools import cache

input_iter = iter(stdin.read().split())
next_int = lambda: int(next(input_iter))

while True:
    m = next_int()
    n = next_int()
    if m == 0:
        break

    objs = [int(next(input_iter), 2) for _ in range(n)]
    bits = [1 << i for i in range(m)]

    @cache
    def dp(mask, masked):
        s = Counter(obj & mask for obj in objs)
        if s.get(masked, 0) <= 1:
            return 0
        candidates = [dp(mask | b, masked) and dp(mask | b, masked | b) for b in bits if not (b & mask)]
        if not candidates:
            return 0
        return min(max(dp(mask | b, masked), dp(mask | b, masked | b)) + 1 for b in bits if not (b & mask))

    print(dp(0, 0))