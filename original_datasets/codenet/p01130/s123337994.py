def floyd(n,L):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                L[i][j]=min(L[i][j],L[i][k]+L[k][j])

while True:
    n,m,s,g1,g2=map(int,raw_input().split())
    if n==0:break
    s-=1
    g1-=1
    g2-=1
    INF=1e10
    L=[[INF]*n for i in range(n)]
    for i in range(n):
        L[i][i]=0
    for i in range(m):
        b1,b2,c=map(int,raw_input().split())
        b1-=1
        b2-=1
        L[b1][b2]=c
    floyd(n,L)
    ans=INF
    for i in range(n):
        ans=min(ans,L[s][i]+L[i][g1]+L[i][g2])
    print ans