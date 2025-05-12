def f(x,y,out,dp):
    if dp[y][x] != "#":
        return dp[y][x]
    if [[x-1,y],[x,y]] in out:
        if [[x,y-1],[x,y]] in out:
            dp[y][x] = 0
            return 0
        else:
            dp[y][x] = f(x,y-1,out,dp)
            return dp[y][x]
    if [[x,y-1],[x,y]] in out:
        dp[y][x] = f(x-1,y,out,dp)
        return dp[y][x]
    else:
        dp[y][x] = f(x-1,y,out,dp)+f(x,y-1,out,dp)
        return dp[y][x]

def solve():
    gx,gy = map(int,input().split())
    p = int(input())
    out = []
    for i in range(p):
        x1,y1,x2,y2 = map(int,input().split())
        out.append([[min(x1,x2)+1,min(y1,y2)+1],[max(x1,x2)+1,max(y1,y2)+1]])
    
    dp = [[0]*(gx+2)]
    for i in range(gy+1):
        dp.append([0]+["#"]*(gx+1))
    dp[1][1] = 1
    ans = f(gx+1,gy+1,out,dp)
    if ans == 0:
        print("Miserable Hokusai!")
    else:
        print(ans)
        #for i in dp:
        #    print(i)
    return 0

n = int(input())
for i in range(n):
    solve()