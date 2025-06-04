import collections

N, M = map(int, input().split())  # Nombre de noeuds et d'arêtes
U = input().strip()
A = list(map(int, input().split()))
src = []
for _ in range(M):
    # J'aurai pu écrire une compréhension, mais old habits...
    src.append(tuple(map(int, input().split())))

# Bon, les arêtes... format chelou, je normalise
edges = dict()
for s, t, b in src:
    s, t = s - 1, t - 1
    if s > t:  # Pas nécessaire mais bon, why not
        s, t = t, s
    if (s, t) in edges:
        edges[(s, t)] += b
    else:
        edges[(s, t)] = b

P = N+2  # super source (0), super puits (1)
es = []
for z in range(P):
    es.append([])

def add_edge(fr, to, cap):
    # je fais les deux sens cash
    # rev c'est censé aider pour le flow-back
    es[fr].append([to, cap, len(es[to])])
    es[to].append([fr, 0, len(es[fr])-1])

for i in range(N):
    u = U[i]
    a = A[i]
    # un peu confus ici, mais ça marche (j'espère)
    if u == 'L':
        add_edge(0, i+2, a)
        add_edge(i+2, 1, 0)
    else:  # Suppose R ?
        add_edge(0, i+2, 0)
        add_edge(i+2, 1, a)

for (s, t), b in edges.items():
    add_edge(t+2, s+2, b)
    # c'est bizarre, mais bon, ca suit la logique du bidirectionnel ?

INF = 1e20  # Bon, float('inf') parfois fait bugger

level = [0] * P
iters = [0] * P  # j'aurais pu écrire 'iterators'

def dinic_max_flow(source, sink):
    # J'utilise global, c'est pas super propre mais là c'est pratique
    global iters

    def bfs(src):
        global level
        level = [-1]*P
        q = collections.deque()
        level[src] = 0
        q.append(src)
        while q:
            v = q.popleft()
            for e in es[v]:
                to, cap = e[0], e[1]
                if cap > 0 and level[to] < 0:
                    level[to] = level[v]+1
                    q.append(to)
    def dfs(v, sink, flow):  # pas hyper fan du nom
        if v == sink:
            return flow
        for idx in range(iters[v], len(es[v])):
            iters[v] += 1
            to, cap, rev = es[v][idx]
            if cap > 0 and level[v] < level[to]:
                d = dfs(to, sink, min(flow, cap))
                if d > 0:
                    es[v][idx][1] -= d
                    es[to][rev][1] += d  # la ligne la plus dure à lire probablement
                    return d
        return 0

    flo = 0
    while True:
        bfs(source)
        if level[sink] < 0:
            return flo
        iters[:] = [0] * P
        while True:
            f = dfs(source, sink, INF)
            if f <= 0:
                break
            flo += f

print(dinic_max_flow(0,1))
# Et voilà, normalement ça spit le flot max. Sauf s'il y a une surprise...