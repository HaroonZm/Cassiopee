def solve(n,w):
    dp=[[0]*(n+1) for _ in range(n+1)]
    for kukan in range(2,n+1):
        for l in range(0,n+1-kukan):
            r=l+kukan
            #decide dp[l][l+kukan]
            if (kukan-2)%2==0:
                if abs(w[l]-w[r-1])<=1 and dp[l+1][r-1]==r-l-2:
                    dp[l][r]=dp[l+1][r-1]+2
                    continue
            for i in range(l+1,r):
                if dp[l][r]<(dp[l][i]+dp[i][r]):
                    dp[l][r]=dp[l][i]+dp[i][r]
    return dp[0][n]
            

n=int(input())
while(n!=0):
    w=list(map(int,input().split()))
    print(solve(n,w))
    n=int(input())