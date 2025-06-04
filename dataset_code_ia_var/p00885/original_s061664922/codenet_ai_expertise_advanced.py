from sys import stdin
from math import inf

def solve():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            b = [(0, 0), *map(lambda line: tuple(map(int, line.split())), (next(lines) for _ in range(n)))]
            dp = [[inf]*4 for _ in range(n+1)]
            dp[0][0] = 0

            for i, (cur, _) in enumerate(b[:-1]):
                updated = False
                cur_val = b[i][1]
                nxt, nxt_val = b[i+1]
                for j, cost in enumerate(dp[i]):
                    if cost == inf:
                        continue
                    delta = abs(nxt - cur)
                    # Option 1
                    if j <= 2 and cur_val + delta * (j+1) <= nxt_val and dp[i+1][j+1] > cost + delta:
                        dp[i+1][j+1] = cost + delta
                        updated = True
                    # Option 2
                    sum_path = cur*(j+1) + nxt
                    if cur_val + sum_path <= nxt_val and dp[i+1][1] > cost + nxt + cur:
                        dp[i+1][1] = cost + nxt + cur
                        updated = True
                if not updated:
                    print('NG', i+1)
                    break
            else:
                print('OK', min(dp[n]) + b[n][0])
        except StopIteration:
            break

solve()