import sys
sys.setrecursionlimit(10**7)

def min_cost_arborescence(n, edges, root):
    INF = 10**9
    E = edges[:]
    res = 0
    while True:
        in_edge = [INF]*n
        pre = [-1]*n
        for s, t, w in E:
            if w < in_edge[t] and t != root:
                in_edge[t] = w
                pre[t] = s
        for i in range(n):
            if i == root:
                continue
            if in_edge[i] == INF:
                return None
        res += sum(in_edge[i] for i in range(n) if i!=root)
        # Detect cycle
        id = [-1]*n
        vis = [-1]*n
        cnt = 0
        for i in range(n):
            if i == root:
                continue
            v = i
            path = []
            while vis[v]<0 and v!=root:
                vis[v] = i
                v = pre[v]
            if v!=root and vis[v]==i:
                u = pre[v]
                id[v] = cnt
                while u!=v:
                    id[u] = cnt
                    u = pre[u]
                cnt +=1
        if cnt == 0:
            break
        for i in range(n):
            if id[i]<0:
                id[i] = cnt
                cnt+=1
        newE = []
        for s, t, w in E:
            ns = id[s]
            nt = id[t]
            if ns != nt:
                newE.append((ns, nt, w - in_edge[t]))
        n = cnt
        root = id[root]
        E = newE
    return res

n, m, r = map(int, input().split())
edges = [tuple(map(int,input().split())) for _ in range(m)]
print(min_cost_arborescence(n, edges, r))