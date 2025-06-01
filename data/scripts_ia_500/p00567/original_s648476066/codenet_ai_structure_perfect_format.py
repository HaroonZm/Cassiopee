def solve(low,n,ls):
    dp=[10**20 for i in range(n+1)]
    dp[0]=low
    for i in range(n):
        length=0
        for j in range(i,-1,-1):
            length+=ls[j]
            if i+1==n and j==0:
                continue
            if length>=low:
                high=max(length,dp[j])
                dp[i+1]=min(dp[i+1],high)
    return dp[n]-low

def main():
    n=int(input())
    ls=[int(input()) for i in range(n)]
    ans=10**20
    for i in range(n):
        length=0
        for j in range(i,n):
            length+=ls[j]
            ans=min(ans,solve(length,n,ls))
    print(ans)

main()