from itertools import product, accumulate
from math import gcd
from bisect import bisect
import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)
#input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))
def ask(p, q):
    print("? {} {}".format(p, q), end="\n", flush=True)
    return int(input())

N, s, t = inpl()
X = ask(s, t)
L = [0, X]
LD = {0: s}
LD[X] = t
ans = [s, t]

for p in range(1, N+1):
    if (p == s) or (p == t):
        continue
    l = ask(s, p)
    r = ask(p, t)
    if (l*r < 0) or (l+r != X):
        continue
    ai = bisect(L, l) - 1
    av = L[ai]
    ak = LD[av]
    if av == l:
        continue
    bv = L[ai+1]
    bk = LD[bv]

    dl = ask(ak, p)
    dr = ask(p, bk)
    if av + dl + dr + (X-bv) == X:
        LD[l] = p
        ans.insert(ai+1, p)
        L.insert(ai+1, l)

print("! " + " ".join(map(str, ans)))