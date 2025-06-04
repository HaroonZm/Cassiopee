import sys
N = int(sys.stdin.readline()[:-1])
a = []
for _ in range(N):
    line = sys.stdin.readline()[:-1]
    row = []
    for x in line.split():
        row.append(int(x))
    a.append(row)
dp = [0] * (1<<N)
S = 0
while S < (1<<N):
    tmp = 0
    i = 0
    while i < N-1:
        j = i+1
        while j < N:
            if ((S>>i)&1) and ((S>>j)&1):
                tmp += a[i][j]
            j += 1
        i += 1
    if tmp > 0:
        dp[S] = tmp
    else:
        dp[S] = 0
    T = (S-1)&S
    while T > 0:
        if dp[S] < dp[T] + dp[S^T]:
            dp[S] = dp[T] + dp[S^T]
        T = (T-1)&S
    S += 1
print(dp[(1<<N)-1])