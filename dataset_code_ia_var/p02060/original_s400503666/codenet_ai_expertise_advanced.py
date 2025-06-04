from functools import lru_cache

N = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
res = float('inf')

@lru_cache(maxsize=None)
def solve(i, j, k):
    total = t[0]*i + t[1]*j + t[2]*k
    cost = p[0]*i + p[1]*j + p[2]*k
    if total > N:
        return cost
    d = max(0, -(-(N - total) // t[3]))  # equivalent to ceil division
    return cost + p[3]*d

for i in range(N//t[0] + 2):
    for j in range(N//t[1] + 2):
        for k in range(N//t[2] + 2):
            res = min(res, solve(i, j, k))

print(res)