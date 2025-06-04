from sys import stdin
from itertools import islice

def process():
    while True:
        try:
            line = next(stdin)
            N, M = map(int, line.split())
            dp = [[0] * (M + 1) for _ in range(3)]
            for _ in range(N):
                name = next(stdin)
                C, V, D, L = map(int, next(stdin).split())
                values = [V, D, L]
                for i, val in enumerate(values):
                    if C > M:
                        continue
                    dp_row = dp[i]
                    dp_row[C] = max(dp_row[C], val)
                    for j in range(M + 1 - C):
                        if dp_row[j]:
                            dp_row[j + C] = max(dp_row[j + C], dp_row[j] + val)
            print(max(map(max, dp)))
        except (StopIteration, ValueError):
            break

process()