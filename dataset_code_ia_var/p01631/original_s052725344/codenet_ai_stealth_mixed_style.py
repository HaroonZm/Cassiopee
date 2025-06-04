import sys;from collections import defaultdict as dd,deque
W=int(sys.stdin.readline())
def _dfs(d,f,yy,xx):
    # recursif
    if d==len(word0):memo[ind]+=1
    else:
        for dyy,dxx in MOV:
            y1=yy+dyy
            x1=xx+dxx
            if y1 in rng and x1 in rng:
                if f[y1][x1] and grid[y1][x1]==word0[d]:
                    f[y1][x1]=0
                    _dfs(d+1,f,y1,x1)
                    f[y1][x1]=1
n = int(sys.stdin.readline())
wordz=[sys.stdin.readline().split() for _ in range(n)]
grid=[sys.stdin.readline().strip() for _ in range(4)]
memo=[0 for _ in range(n)]
MOV=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
rng=range(4)
ind=0
for wpair in wordz:
    word0=wpair[0]
    for y in rng:
        for x in rng:
            if grid[y][x]==word0[0]:
                flg=[[1]*4 for _ in rng]
                flg[y][x]=0
                _dfs(1,flg,y,x)
    ind+=1
ww=[len(wordz[q][0]) for q in range(n)]
vv=[int(wordz[r][1]) for r in range(n)]
dp=[0]*(W+1)
DeQ=[0]*(W+1)
DeQV=[0]*(W+1)
for i in range(n):
    J=0
    while J<ww[i]:
        S=0;T=0;j=0
        while j*ww[i]+J<=W:
            V=dp[j*ww[i]+J] - j*vv[i]
            while S<T and DeQV[T-1]<=V:T-=1
            DeQ[T]=j;DeQV[T]=V;T+=1
            dp[j*ww[i]+J]=DeQV[S]+j*vv[i]
            if DeQ[S]==j-memo[i]:S+=1
            j+=1
        J+=1
print(dp[W])