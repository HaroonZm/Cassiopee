from itertools import combinations
from collections import Counter
N, K, L, R, *A = map(int, open(0).read().split())
def make(A, K):
    return [Counter(map(sum, combinations(A, l))) for l in range(0, K+1)]

P = make(A[:N//2], K)
Q = make(A[N//2:], K)

ans = 0
for i in range(K+1):
    p = P[i]; q = Q[K-i]
    sq = sorted(q)
    l = r = len(q)
    s = 0
    for k, v in sorted(p.items()):
        while r and k+sq[r-1] > R:
            r -= 1
            s -= q[sq[r]]
        while l and k+sq[l-1] >= L:
            l -= 1
            s += q[sq[l]]
        ans += v * s
print(ans)