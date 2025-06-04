N, M = input().split()
N = int(N)
M = int(M)
L = []
R = []

A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

for i in range(M):
    x, y = input().split()
    L.append(int(x))
    R.append(int(y))

pre = []
for i in range(N+1):
    pre.append(0)
dp = []
for i in range(N+1):
    dp.append(0)

for i in range(1, N+1):
    pre[i] = i - 1

for i in range(M):
    nowR = R[i]
    nowL = L[i]
    if pre[nowR] > nowL - 1:
        pre[nowR] = nowL - 1

for i in range(N-1, 0, -1):
    if pre[i] > pre[i+1]:
        pre[i] = pre[i+1]

for i in range(1, N+1):
    if dp[i-1] > dp[pre[i]] + A[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[pre[i]] + A[i-1]

print(dp[N])