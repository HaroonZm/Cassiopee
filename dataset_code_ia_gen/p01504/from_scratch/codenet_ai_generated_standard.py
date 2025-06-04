import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

case_num = 1
while True:
    n,t,k = map(int,input().split())
    if n==0 and t==0 and k==0:
        break
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v,c = map(int,input().split())
        adj[u].append((v,c))
        adj[v].append((u,c))
    bases = set()
    for _ in range(t):
        b = int(input())
        bases.add(b)

    # dp[u][x]: min cost to split subtree rooted at u into x components, each with >=1 base
    # size of dp[u] is up to min(t,k+1) but k+1 <= t so max = k+1
    INF = 10**15
    dp = [dict() for _ in range(n+1)]

    def dfs(u,p):
        # If u is base, dp[u][1]=0 else dp[u][0]=0
        dp[u] = {1:0} if u in bases else {0:0}
        for v,cost in adj[u]:
            if v==p:
                continue
            dfs(v,u)
            ndp = {}
            for x1,c1 in dp[u].items():
                for x2,c2 in dp[v].items():
                    # Two choices:
                    # 1) Cut edge u-v: cost paid, number of components add up
                    nx = x1 + x2
                    if nx <= k+1:
                        ndp[nx] = min(ndp.get(nx,INF), c1 + c2 + cost)
                    # 2) Do not cut: merge subtree, components number = max(x1,x2)
                    # But must check if combined subtree has at least one base:
                    # since dp[u] and dp[v] only keep keys with valid base counts,
                    # merging is possible with components = max(x1,x2)
                    n_components = x1 + x2 - 1
                    # Actually, no, merging two disjoint components reduces by 1,
                    # but we keep track of how many components with bases inside subtree rooted at u.
                    # The merging implies that total components is x1 + x2 - 1
                    # So:
                    nx2 = x1 + x2 -1
                    if nx2 <= k+1 and nx2 >=0:
                        ndp[nx2] = min(ndp.get(nx2,INF), c1 + c2)
            dp[u] = ndp

    # root anywhere, pick node 1
    dfs(1,-1)
    # We want dp[1][k+1] minimal cost
    res = dp[1].get(k+1,INF)
    print(f"Case {case_num}: {res}")
    case_num += 1