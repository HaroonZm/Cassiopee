from functools import lru_cache

n = int(input())
C = []
i = 0
while i < n:
    x, y = map(int, input().split())
    C.append((x,y))
    i += 1

Memo = {}
def F(L, R):
    key = (L,R)
    if Memo.get(key) is not None:
        return Memo[key]
    if L+1 == R:
        Memo[key] = 0
        return 0
    results = []
    for M in range(L+1, R):
        z = C[L][0] * C[M-1][1] * C[M][0] * C[R-1][1]
        res = F(L, M) + F(M, R) + z
        results.append(res)
    Memo[key] = min(results) if results else 0
    return Memo[key]

show = lambda x: print(x)
show(F(0, n))