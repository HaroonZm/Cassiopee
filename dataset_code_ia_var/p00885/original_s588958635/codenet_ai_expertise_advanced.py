import sys
from collections import deque
from itertools import islice
from functools import partial

INF = 10**9

def gen_inputs():
    stdin = sys.stdin
    while True:
        n = stdin.readline()
        if not n:
            break
        n = n.strip()
        if not n:
            continue
        yield int(n), list(islice((map(int, line.split()) for line in stdin), int(n)))

for n, datalist in gen_inputs():
    dp = [0] + [INF] * 4
    pos, time = 0, 0
    fail_at = -1
    for i, (p, t) in enumerate(datalist):
        d = abs(p - pos)
        ndp = dp[:]
        can = False
        r = INF
        # enumerate only up to 3 for j, must handle i==0 case
        for j in range(4)[::-1] if i else [0]:
            if dp[j] == INF:
                ndp[j+1] = INF
                continue
            movement_time = d * (j+1)
            wait_time = t - time
            if j < 3 and movement_time <= wait_time:
                ndp[j+1] = min(ndp[j+1], dp[j] + d)
                can = True
            # time to move back and forth without boosting
            if pos * (j+1) + p <= wait_time:
                r = min(r, dp[j] + pos + p)
                can = True
        ndp[1] = r
        ndp = ndp[:5]
        if not can:
            fail_at = i + 1
            break
        dp = ndp
        pos, time = p, t
    if fail_at != -1:
        print(f"NG {fail_at}")
    else:
        last_p = datalist[-1][0]
        print(f"OK {min(dp[1:]) + last_p}")