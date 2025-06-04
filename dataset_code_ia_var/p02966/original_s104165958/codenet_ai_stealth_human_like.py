n = int(input())

A = []
for x in range(n):
    row = []
    for y in range(n):
        row.append(0)
    A.append(row)

Al = []
for i in range(n+1):
    Al.append([0]*(n+1))
Ar = []
for i in range(n+1):
    Ar.append([0]*(n+1))

for i in range(n):
    x = [int(xx) for xx in input().split()]
    for j in range(n):
        if i < j:
            A[i][j] = x[j-1]  # hmm, index shenanigans
        elif i > j:
            A[i][j] = x[j]

# accumulate from left and right
for i in range(n):
    for j in range(i+1, n):
        Al[j][i+1] = Al[j][i] + A[j][i]   # why i+1 on left? works I guess
        if i-1 >= 0:
            Ar[i][j] = Ar[i-1][j] + A[i][j]
        else:
            Ar[i][j] = A[i][j]

# print("Al:", Al)
# print("Ar:", Ar)

dp = []
for i in range(n+1):
    dp.append([float("inf")]*(n+1))
dp[0][0] = 0

for i in range(n+1):
    for j in range(i, n+1): # not sure why j starts from i but that's how it's done
        l = 0
        r = 0
        k = j+1
        while k <= n:
            l = l + Al[k-1][i]
            r += (Ar[k-2][k-1] - Ar[j-1][k-1]) if j-1 >= 0 else Ar[k-2][k-1]
            before = dp[j][k]
            now = dp[i][j] + l + r
            if now < before:
                dp[j][k] = now
            k += 1
            # print('loop:', i,j,k,l,r,dp[j][k])
# print("DP:", dp)
ans = float("inf")
for i in range(n+1):
    ans = min(ans, dp[i][n])
print(ans)