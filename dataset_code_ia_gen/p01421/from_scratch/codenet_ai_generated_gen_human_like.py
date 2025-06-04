import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
edges = []
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    edges.append((X-1, Y-1))
S, T = map(int, sys.stdin.readline().split())
S -= 1
T -= 1

# Construction d'un graphe avec pour chaque arête deux arcs (u->v) et (v->u) de capacité 1
# mais l'arête correspondante a une direction originale, et l'autre est "reverse possible".
# Le coût est la direction: on souhaite minimiser le nombre d'arêtes inversées.
# On peut modéliser le problème comme un flots à coût minimal:
# mettons:
# - capacité de chaque arc = 1
# - arc dans la direction originale coût 0
# - arc dans la direction inverse coût 1 (car on le "reverse")
# On cherche un flow maximal avec coût minimal.

# Implémentation d'un algorithme de flow min-cost max-flow:
from collections import deque

class Edge:
    def __init__(self, to, rev, capacity, cost, idx):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.cost = cost
        self.idx = idx  # id de l'arête origine, ou -1 pour mémo

INF = 10**9

graph = [[] for _ in range(N)]

def add_edge(fr, to, capacity, cost, idx):
    graph[fr].append(Edge(to, len(graph[to]), capacity, cost, idx))
    graph[to].append(Edge(fr, len(graph[fr])-1, 0, -cost, idx))

for i, (u, v) in enumerate(edges):
    # arc original: cout 0
    add_edge(u, v, 1, 0, i)
    # arc inverse possible: cout 1 (on retourne la route)
    add_edge(v, u, 1, 1, i)

def min_cost_max_flow(s, t):
    flow = 0
    cost = 0
    prevv = [0]*N
    preve = [0]*N
    while True:
        dist = [INF]*N
        dist[s] = 0
        inqueue = [False]*N
        queue = deque([s])
        while queue:
            v = queue.popleft()
            inqueue[v] = False
            for i,e in enumerate(graph[v]):
                if e.capacity > 0 and dist[e.to] > dist[v] + e.cost:
                    dist[e.to] = dist[v] + e.cost
                    prevv[e.to] = v
                    preve[e.to] = i
                    if not inqueue[e.to]:
                        inqueue[e.to] = True
                        queue.append(e.to)
        if dist[t] == INF:
            break
        # Ajouter un flow de 1 cheminement
        d = 1
        flow += d
        cost += dist[t]*d
        v = t
        while v != s:
            e = graph[prevv[v]][preve[v]]
            e.capacity -= d
            graph[v][e.rev].capacity += d
            v = prevv[v]
    return flow, cost

flow, cost = min_cost_max_flow(S, T)

# On veut afficher:
# Flow max : flow
# Nombre d'arêtes renversées : cost (car chaque inversion coute 1)
# IDs des arêtes renversées

# Pour retrouver les arêtes inversées, on analyse les arcs utilisés dans le flow :
# Un arc inversé est celui avec cost=1 et flow=1 (arc saturé dans le sens inverse).
# Le flow est implicite via une diminution capacity.

used_reverse = []
# Parcourir les arcs dans le graphe, chercher les arcs avec cost=1 (arcs inverses)
# et le fait qu'ils soient utilisés (capacity <1) donc capacity=0 pour capacity initial=1

for u in range(N):
    for e in graph[u]:
        if e.idx != -1 and e.cost == 1:
            # arc inversé possible
            # Si capacity < 1, c'est utilisé (car capacity initial=1)
            if e.capacity == 0:
                used_reverse.append(e.idx+1)

print(flow)
print(len(used_reverse))
for r in used_reverse:
    print(r)