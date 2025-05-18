z=int(input())
for _ in range(z):
    gx,gy = map(int,input().split())
    p=int(input())
    mat=[tuple(map(int,input().split())) for _ in range(p)]
    dp=[[0]*(gy+1) for _ in range(gx+1)]
    
    x0=gx
    y0=gy
    for x1,y1,x2,y2 in mat:
        if x1+x2==0: y0=min(y0,min(y1,y2))
        if y1+y2==0: x0=min(x0,min(x1,x2))
    for i in range(x0+1):
        dp[i][0]=1
    for i in range(y0+1):
        dp[0][i]=1
    
    for y in range(1,gy+1):
        for x in range(1,gx+1):
            a=0
            if (x-1,y,x,y) not in mat and (x,y,x-1,y) not in mat:
                a+=dp[x-1][y]
            if (x,y-1,x,y) not in mat and (x,y,x,y-1) not in mat:
                a+=dp[x][y-1]
            dp[x][y]=a
    print(dp[-1][-1] or "Miserable Hokusai!")