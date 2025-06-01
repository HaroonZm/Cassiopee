m,n=map(int,raw_input().split())
p=[]
for _ in xrange(m):
    p.append(int(raw_input()))
ce=[]
for _ in xrange(n):
    a,b=map(int,raw_input().split())
    ce.append([a,b])
dp=[]
for _ in xrange(n+1):
    dp.append([float('inf')]*(m+1))
for i in xrange(n+1):
    dp[i][0]=0
for i in xrange(n):
    for j in xrange(1,m+1):
        if j<ce[i][0]:
            dp[i+1][j]=min(dp[i][j],ce[i][1])
        else:
            dp[i+1][j]=min(dp[i][j],dp[i][j-ce[i][0]]+ce[i][1])
p.sort()
p.reverse()
sump=[0]*(m+1)
for i in xrange(m):
    sump[i+1]=sump[i]+p[i]
ans=0
for i in xrange(1,m+1):
    if sump[i]-dp[n][i]>ans:
        ans=sump[i]-dp[n][i]
print(ans)