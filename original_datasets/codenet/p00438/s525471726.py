h=0
w=0
n=0
while 1:
    h,w=map(int,input().split())
    if not h and not w:
      break
    h-=1
    w-=1
    obs=[[1]*(w+1) for i in range(h+1)]
    n=int(input())
    for i in range(n):
        x,y=map(int,input().split())
        obs[x-1][y-1]=0
    dp=[[0]*(w+2) for i in range(h+2)]
    dp[0][0]=obs[0][0]
    for i in range(h+1):
        for j in range(w+1):
            if obs[i][j]:
                dp[i+1][j]+=dp[i][j]
                dp[i][j+1]+=dp[i][j]
    if obs[h][w]:
        print(dp[h][w])
    else:
        print(0)