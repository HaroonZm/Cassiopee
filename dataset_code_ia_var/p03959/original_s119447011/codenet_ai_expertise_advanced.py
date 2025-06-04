import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

INF = float('inf')
MOD = 10**9 + 7

def getints(): return list(map(int, sys.stdin.readline().split()))
def getint(): return int(sys.stdin.readline())

n = getint()
t = getints()
a = getints()

just = [0] * n
ub = [INF] * n

def enforce(j, val):
    if just[j] in (0, val):
        just[j] = val
    else:
        print(0)
        sys.exit(0)

enforce(0, t[0])
enforce(n-1, a[-1])

for j in range(1, n):
    if t[j] != t[j-1]:
        enforce(j, t[j])
    else:
        ub[j] = t[j]
for j in range(n-2, -1, -1):
    if a[j] != a[j+1]:
        enforce(j, a[j])
    else:
        ub[j] = min(ub[j], a[j])

ans = 1
for j in range(n):
    if just[j] == 0:
        ans = (ans * int(ub[j])) % MOD
    elif just[j] <= ub[j]:
        continue
    else:
        print(0)
        sys.exit(0)
print(ans)