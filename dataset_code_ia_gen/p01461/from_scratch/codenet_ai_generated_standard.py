import sys
sys.setrecursionlimit(10**7)
N=int(sys.stdin.readline())
yes=[0]*(N)
no=[0]*(N)
for i in range(1,N):
    y,n=map(int,sys.stdin.readline().split())
    yes[i]=y
    no[i]=n
dp=[0]*(N+1)
def dfs(u):
    if u==N:
        return 0
    if dp[u]!=0:
        return dp[u]
    y=dfs(yes[u])
    n=dfs(no[u])
    # We play both branches:
    # Time = 1(minute to next branching point) + min of:
    # 2*max(y,n) to do one branch then the other, no quicksave
    # or max(y,n)+1+min(y,n) with quicksave: save before longer path, do longer, reload (1 min), do shorter
    # Hence: min(2*max(y,n), max(y,n)+1+min(y,n))
    dp[u]=1+min(2*max(y,n), max(y,n)+1+min(y,n))
    return dp[u]
print(dfs(1))