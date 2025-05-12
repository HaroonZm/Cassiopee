h,w = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(h)]

dp = [[0]*w for _ in range(h)]

max_edge = 0

for i in range(h):
    if c[i][0] == 0:
        dp[i][0] = 1
        max_edge = 1
for i in range(w):
    if c[0][i] == 0:
        dp[0][i] = 1
        max_edge = 1
        
        
for i in range(1,h):
    for j in range(1,w):
        if c[i][j] == 1:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
            max_edge = max(max_edge,dp[i][j])

print(max_edge**2)