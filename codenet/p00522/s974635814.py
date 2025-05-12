m,n=map(int,raw_input().split())
p=[int(raw_input()) for _ in xrange(m)]
ce=[map(int,raw_input().split()) for _ in  xrange(n)]
dp=[[float('inf')]*(m+1) for _ in xrange(n+1)]
for i in xrange(n+1):
    dp[i][0]=0

for i in xrange(n):
    for j in xrange(1,m+1):
        if j<ce[i][0]:
            dp[i+1][j]=min(dp[i][j],ce[i][1])
            continue
        dp[i+1][j]=min(dp[i][j],dp[i][j-ce[i][0]]+ce[i][1])

p.sort()
p.reverse()
sump=[0]*(m+1)
for i in xrange(m):
    sump[i+1]+=sump[i]+p[i]

ans=0
for i in xrange(1,m+1):
    ans=max(ans,sump[i]-dp[n][i])
print(ans)