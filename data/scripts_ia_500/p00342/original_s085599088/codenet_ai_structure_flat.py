import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
mod = 1000000007

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
ans = -float("inf")
for c in range(n):
    for d in range(c):
        m = a[c] - a[d]
        e = None
        for i in range(n - 1, -1, -1):
            if i != c and i != d:
                e = i
                break
        if e is None:
            continue
        b = None
        for i in range(e - 1, -1, -1):
            if i != c and i != d:
                b = i
                break
        if b is None:
            continue
        ans = max(ans, (a[e] + a[b]) / m)
print(ans)