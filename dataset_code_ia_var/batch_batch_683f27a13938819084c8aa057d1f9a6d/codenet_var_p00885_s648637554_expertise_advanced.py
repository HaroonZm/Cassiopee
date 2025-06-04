from sys import stdin
from itertools import islice, repeat

INF = 10**9

def optimized_solve():
    while True:
        n_str = stdin.readline()
        if not n_str:
            break
        n = int(n_str)
        dp = [INF] * 4
        dp[0] = 0
        pos, time, fail = 0, 0, -1
        ps, ts = zip(*(map(int, s.split()) for s in islice(stdin, n)))
        for i, (p, t) in enumerate(zip(ps, ts)):
            d = abs(p - pos)
            can = False
            r = INF
            next_dp = list(dp)
            for j in reversed(range(4)):
                if j < 3:
                    next_dp[j + 1] = INF
                if dp[j] == INF:
                    continue
                if j < 3 and d * (j + 1) <= t - time:
                    can = True
                    next_dp[j + 1] = min(next_dp[j + 1], dp[j] + d)
                if pos * (j + 1) + p <= t - time:
                    r = min(r, dp[j] + pos + p)
                    can = True
            next_dp[1] = r
            next_dp[0] = INF
            if not can:
                fail = i + 1
                break
            dp = next_dp
            pos, time = p, t
        if fail != -1:
            print(f"NG {fail}")
        else:
            print(f"OK {min(dp[1:]) + pos}")

optimized_solve()