INF = 10**18

N, S = map(int, input().split())
A = list(map(int, input().split()))

res = INF

rt = 0
s = 0

for lt in range(N):
    while rt < N and s < S:
        s += A[rt]
        rt += 1
    if s >= S:
        res = min(res, rt - lt)
    s -= A[lt]

print(res if res != INF else 0)