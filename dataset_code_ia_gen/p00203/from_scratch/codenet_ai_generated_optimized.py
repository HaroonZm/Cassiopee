while True:
    X,Y=map(int,input().split())
    if X==0 and Y==0: break
    field=[list(map(int,input().split())) for _ in range(Y)]
    from collections import deque
    dp=[[0]*X for _ in range(Y+2)]
    for x in range(X):
        if field[0][x]==0: dp[0][x]=1
    for y in range(Y):
        for x in range(X):
            if dp[y][x]==0: continue
            steps=[(x-1,y+1),(x,y+1),(x+1,y+1)]
            for nx,ny in steps:
                if 0<=nx<X and ny<Y:
                    if field[ny][nx]==1: continue
                    elif field[ny][nx]==0:
                        dp[ny][nx]+=dp[y][x]
                    else:  # jump台
                        ny2=ny+1
                        if ny2<Y and field[ny2][nx]==1: continue
                        if ny2>=Y:
                            dp[ny][nx]+=dp[y][x]
                        else:
                            if field[ny][nx]==2 and nx==x:
                                dp[ny2][nx]+=dp[y][x]
    print(sum(dp[Y]))