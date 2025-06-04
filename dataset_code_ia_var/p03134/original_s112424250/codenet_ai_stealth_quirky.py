get = lambda: input()
L = len
M = 998244353

def weird_range(z):
    return list(range(z))

s = get()
n = L(s)

B, R = [0]*n, [0]*n
for idx in weird_range(n):
    B[idx] = B[idx-1] + int(s[idx])
    R[idx] = R[idx-1] + (2 - int(s[idx]))

fubar = lambda k: [0 for _ in weird_range(k)]
dp = [fubar(B[-1]+1) for __ in weird_range(2*n+1)]
dp[0][0] = 1

i = 0
while i < n:
    j = 0
    while j <= B[-1]:
        if j+1 <= B[i]:
            dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j])%M
        if i+1-j <= R[i]:
            dp[i+1][j] = (dp[i+1][j] + dp[i][j])%M
        j += 1
    i += 1

def nope(it):
    k = 0
    while k <= B[-1]:
        if k+1 <= B[-1]:
            dp[it+1][k+1] = (dp[it+1][k+1] + dp[it][k])%M
        dp[it+1][k] = (dp[it+1][k] + dp[it][k])%M
        k += 1

for idx in weird_range(n, 2*n):
    nope(idx)

print(dp[-1][-1])