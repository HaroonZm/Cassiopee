import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, K = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

size = [0]*N
dp = [0]*N
ans = 0

def dfs1(u, p):
    sz = 1
    c = 0
    for w in adj[u]:
        if w==p: continue
        dfs1(w,u)
        if size[w]>=K:
            c +=1
        else:
            sz += size[w]
    size[u] = sz
    dp[u] = c

dfs1(0,-1)
ans = max(dp)

parent = [-1]*N
def dfs2(u):
    for w in adj[u]:
        if w==parent[u]: continue
        parent[w]=u
        dfs2(w)
dfs2(0)

# calculate up arrays for rerooting
upsize = [0]*N
updp = [0]*N

def reroot(u):
    global ans
    prefix_sizes = [0]
    prefix_dp = [0]
    children = []
    for w in adj[u]:
        if w==parent[u]: continue
        children.append(w)
        prefix_sizes.append(prefix_sizes[-1]+(size[w] if size[w]<K else 0))
        prefix_dp.append(prefix_dp[-1]+(dp[w] if size[w]>=K else 0))
    suffix_sizes = [0]*(len(children)+1)
    suffix_dp = [0]*(len(children)+1)
    for i in range(len(children)-1,-1,-1):
        w = children[i]
        suffix_sizes[i] = suffix_sizes[i+1]+(size[w] if size[w]<K else 0)
        suffix_dp[i] = suffix_dp[i+1]+(dp[w] if size[w]>=K else 0)

    total_sz_underK = prefix_sizes[-1] + (upsize[u] if upsize[u]<K else 0)
    total_dp_K = prefix_dp[-1] + (updp[u] if upsize[u]>=K else 0)

    ans = max(ans, total_dp_K)

    for i, w in enumerate(children):
        # Remove child's subtree contribution
        below_sz = prefix_sizes[i]+suffix_sizes[i+1]+(upsize[u] if upsize[u]<K else 0)
        below_dp = prefix_dp[i]+suffix_dp[i+1]+(updp[u] if upsize[u]>=K else 0)

        old_size_u = size[u]
        old_dp_u = dp[u]
        old_upsize_w = upsize[w]
        old_updp_w = updp[w]

        # update upsize and updp for child w
        # child w's up part includes entire tree except child's subtree and node u itself
        # size[u] - (size[w] if size[w]<K else 0) + (upsize[u] if upsize[u]<K else 0)
        new_upsize = below_sz + 1
        new_updp = below_dp
        if new_upsize>=K:
            new_updp +=1

        upsize[w]=new_upsize
        updp[w]=new_updp

        reroot(w)

        upsize[w] = old_upsize_w
        updp[w] = old_updp_w

reroot(0)
print(ans)