from sys import stdin
from itertools import starmap

def f(n):
    bs = sorted((map(int, line.split()) for line in stdin), key=lambda x: x[0] + x[1])
    max_sum = sum(w + s for w, s, _ in bs)
    from array import array
    dp = array('i', (0,)) * (max_sum + 1)
    for w, s, v in bs:
        for i in range(w + s, w - 1, -1):
            nv = dp[i - w] + v
            if nv > dp[i]:
                dp[i] = nv
    print(max(dp))

f(int(stdin.readline()))