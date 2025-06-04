import sys
from functools import partial
from itertools import accumulate

readline = sys.stdin.readline
write = sys.stdout.write

V = [i * i for i in range(1, 18)]
dp = [1] + [0] * 300

for v in V:
    for k in range(301 - v):
        if dp[k]:
            cnt = k + v
            while cnt <= 300:
                dp[cnt] += dp[k]
                cnt += v

for N in iter(partial(int, readline()), 0):
    write(f"{dp[N]}\n")