import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# dp[u][k]: number of ways to select k connected, pairwise vertex-disjoint subtrees completely inside subtree rooted at u, with subtree including u as connected subtree or empty
# We'll keep two arrays:
# f[u][k]: number of ways to select k connected components inside subtree u, those components do NOT necessarily include u.
# g[u][k]: number of ways to select k connected components including u (i.e., connected subtree including u)
# Finally, for overall dp at u, dp[u][k] = f[u][k] + g[u][k]

# But since question counts K components of connected subgraphs pairwise vertex-disjoint,
# and order does not matter,
# We proceed as follows (definition aligns with editorial of similar problems):

# We will compute:
# dp[u][k]: number of ways to select k connected components (non-empty, vertex-disjoint), all inside u's subtree
# We use two arrays at each node:
# dp0[k]: ways without including u in any connected component
# dp1[k]: ways with u included in exactly one connected component (which includes u)
# Then dp[u] = dp0 + dp1

# Initialization at leaf:
# dp0[0] = 1 (empty selection)
# dp1[1] = 1 (the singleton component consisting only of u)

def combine(a0, a1, b0, b1):
    # combine dp states of parent(a) and child(b)
    # a0,a1,b0,b1 are arrays length K+1
    # returns (c0,c1)
    c0 = [0]*(K+1)
    c1 = [0]*(K+1)
    for ka in range(K+1):
        va0 = a0[ka]
        va1 = a1[ka]
        if va0==0 and va1==0:
            continue
        for kb in range(K+1 - ka):
            vb0 = b0[kb]
            vb1 = b1[kb]
            if vb0==0 and vb1==0:
                continue
            ways = (va0 * vb0)%MOD
            c0[ka+kb] = (c0[ka+kb] + ways)%MOD
            ways = (va0 * vb1)%MOD
            c1[ka+kb] = (c1[ka+kb] + ways)%MOD
            ways = (va1 * vb0)%MOD
            c1[ka+kb] = (c1[ka+kb] + ways)%MOD
            # merge the component including u with child's component including child is impossible since they share nodes only if child's component includes u's child 
            # but since child's component including child is separate component and child's subtree is disjoint of parent's components except at u, 
            # the child component including child and parent's component including u are distinct,
            # so they remain separate components, so combine counts as two components (sum)
            ways = (va1 * vb1)%MOD
            if ka + kb +1 <= K:
                c1[ka+kb+1] = (c1[ka+kb+1] + ways)%MOD
    return c0, c1

visited = [False]*N

def dfs(u):
    visited[u]=True
    dp0 = [0]*(K+1)
    dp1 = [0]*(K+1)
    dp0[0] = 1
    dp1[1] = 1

    for v in graph[u]:
        if visited[v]:
            continue
        c0, c1 = dfs(v)

        ndp0 = [0]*(K+1)
        ndp1 = [0]*(K+1)

        # combine dp[u] and dp[v]
        for i in range(K+1):
            va0 = dp0[i]
            va1 = dp1[i]
            if va0==0 and va1==0:
                continue
            for j in range(K+1 - i):
                vb0 = c0[j]
                vb1 = c1[j]
                if vb0==0 and vb1==0:
                    continue

                # case dp0 and c0: all outside u, disjoint
                ways = (va0 * vb0)%MOD
                ndp0[i+j] = (ndp0[i+j] + ways)%MOD

                # case dp0 and c1: parent's no u, child's includes v, disjoint sets
                ways = (va0 * vb1)%MOD
                ndp1[i+j] = (ndp1[i+j] + ways)%MOD

                # case dp1 and c0: parent's includes u, child's no component, disjoint
                ways = (va1 * vb0)%MOD
                ndp1[i+j] = (ndp1[i+j] + ways)%MOD

                # case dp1 and c1: both have components including u and v resp
                # these components can be merged forming one component including u
                # number of connected components decreases by 1
                if i + j + 1 <= K:
                    ways = (va1 * vb1)%MOD
                    ndp1[i+j+1] = (ndp1[i+j+1] + ways)%MOD

        dp0, dp1 = ndp0, ndp1
    return dp0, dp1

dp0, dp1 = dfs(0)
ans = (dp0[K] + dp1[K])%MOD
print(ans)