import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]

from collections import defaultdict

starts = defaultdict(list)
for w in words:
    starts[w[0]].append(w)

dp = {}
def f(w):
    if w in dp:
        return dp[w]
    last_char = w[-1]
    res = set()
    for nw in starts[last_char]:
        if nw != w:
            res |= f(nw)
    if not res:
        res = {w[-1]}
    dp[w] = res
    return res

res = set()
for w in words:
    res |= f(w)

for c in sorted(res):
    print(c)