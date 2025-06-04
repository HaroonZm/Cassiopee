N,P=map(int,input().split())
XY=[tuple(map(int,input().split())) for _ in range(N)]
dp=[[-1]*(P+1) for _ in range(N+1)]
dp[0][P]=0
for i in range(N):
    X,Y=XY[i]
    for p in range(P+1):
        if dp[i][p]<0: continue
        # Ne pas encourager
        x_next = XY[i+1][0] if i+1<N else 0
        if X>=Y:
            dp[i+1][p]=max(dp[i+1][p],dp[i][p]+1)
            # Si on ne change pas le prochain jour
        else:
            dp[i+1][p]=max(dp[i+1][p],dp[i][p])
        # Encourager, trouver t minimal pour aller à l'école
        need=Y - X
        if need>0 and p>=need:
            # Ajuster le motivation du prochain jour
            if i+1<N:
                nx = max(0,XY[i+1][0]-need)
                XY[i+1]=(nx,XY[i+1][1])
            dp[i+1][p-need]=max(dp[i+1][p-need],dp[i][p]+1)
            # Restaurer pour ne pas affecter les itérations
            if i+1<N:
                XY[i+1]=(XY[i+1][0]+need,XY[i+1][1])
print(max(dp[N]))