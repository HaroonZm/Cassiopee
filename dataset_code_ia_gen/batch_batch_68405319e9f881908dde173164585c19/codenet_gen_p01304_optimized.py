import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    gx,gy=map(int,input().split())
    p=int(input())
    blocked=set()
    for __ in range(p):
        x1,y1,x2,y2=map(int,input().split())
        if (x1,y1)>(x2,y2):
            x1,y1,x2,y2=x2,y2,x1,y1
        blocked.add(((x1,y1),(x2,y2)))
    dp=[[0]*(gy+1) for __ in range(gx+1)]
    dp[0][0]=1
    for x in range(gx+1):
        for y in range(gy+1):
            if x==0 and y==0:
                continue
            ways=0
            if x>0 and ((x-1,y),(x,y)) not in blocked:
                ways+=dp[x-1][y]
            if y>0 and ((x,y-1),(x,y)) not in blocked:
                ways+=dp[x][y-1]
            dp[x][y]=ways
    ans=dp[gx][gy]
    if ans==0:
        print("Miserable Hokusai!")
    else:
        print(ans)