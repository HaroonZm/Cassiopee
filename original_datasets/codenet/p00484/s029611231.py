n,k=map(int,raw_input().split())
g=[[] for _ in xrange(10)]
for i in xrange(n):
    v,j=map(int,raw_input().split())
    g[j-1].append(v)
for i in xrange(10):
    g[i].sort()
    g[i].reverse()

books=[[0]*2005 for _ in xrange(10)]
for i in xrange(10):
    for j in xrange(1,len(g[i])+1):
        books[i][j]=books[i][j-1]+g[i][j-1]+2*(j-1)

dp=[[0]*(k+1) for _ in xrange(11)]
for i in xrange(10):
    for j in xrange(1,k+1):
        for l in xrange(j+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j-l]+books[i][l])

print(dp[10][k])