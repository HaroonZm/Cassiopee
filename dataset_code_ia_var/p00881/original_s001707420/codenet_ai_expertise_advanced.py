from collections import Counter
from sys import stdin

def solve():
    input_iter = iter(stdin.read().split())
    while True:
        m = int(next(input_iter))
        n = int(next(input_iter))
        if m == 0:
            break

        objects = [int(next(input_iter), 2) for _ in range(n)]
        dp = [bytearray(1 << m) for _ in range(1 << m)]
        bits = [1 << i for i in range(m)]

        for asked in range((1 << m) - 2, -1, -1):
            c = Counter(obj & asked for obj in objects)
            for masked, count in c.items():
                if count > 1:
                    dp[asked][masked] = min(
                        max(dp[asked | b][masked], dp[asked | b][masked | b])
                        for b in bits if not (asked & b)
                    ) + 1
        print(dp[0][0])

solve()