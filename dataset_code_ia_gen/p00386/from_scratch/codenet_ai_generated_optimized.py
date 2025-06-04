import sys
import threading
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N,Q = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    LOG = 1
    while (1 << LOG) <= N:
        LOG += 1

    depth = [0]*(N+1)
    dist = [0]*(N+1)
    parent = [[-1]*(N+1) for _ in range(LOG)]

    def dfs(u,p):
        for nx,w in adj[u]:
            if nx != p:
                depth[nx] = depth[u]+1
                dist[nx] = dist[u]+w
                parent[0][nx] = u
                dfs(nx,u)

    dfs(1,-1)

    for k in range(LOG-1):
        for v in range(1,N+1):
            if parent[k][v] < 0:
                parent[k+1][v] = -1
            else:
                parent[k+1][v] = parent[k][parent[k][v]]

    def lca(u,v):
        if depth[u] > depth[v]:
            u,v = v,u
        diff = depth[v]-depth[u]
        for i in range(LOG):
            if diff & (1 << i):
                v = parent[i][v]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if parent[i][u] != parent[i][v]:
                u = parent[i][u]
                v = parent[i][v]
        return parent[0][u]

    def dist_uv(u,v):
        return dist[u]+dist[v]-2*dist[lca(u,v)]

    for _ in range(Q):
        a,b,c = map(int,input().split())
        abc = [a,b,c]
        abc.sort()
        a,b,c = abc
        # Calculate pairwise distance
        dab = dist_uv(a,b)
        dbc = dist_uv(b,c)
        dac = dist_uv(a,c)

        # The minimal maximum distance after meeting in some city
        # The best meeting city is one of the three nodes or LCA points that minimize max distances
        # The cost is (dab + dbc + dac) / 2 - min_distance among pairs
        # To avoid float, use exact evaluation:
        # The minimal max dist = max( (dab+dbc+dac)/2 - min pair dist )

        # We can try all meeting points on the path of these three nodes
        # Explanation (known from problem editorial): answer = (dab+dbc+dac)//2

        # But be careful to choose max distance: the minimal max distance is:
        # = max((dab+dbc-dac)/2, (dab+dac-dbc)/2, (dbc+dac-dab)/2)
        x = (dab+dbc-dac)//2
        y = (dab+dac-dbc)//2
        z = (dbc+dac-dab)//2
        print(max(x,y,z))

threading.Thread(target=main).start()