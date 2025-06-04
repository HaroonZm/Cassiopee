import sys
import heapq

V, E, r = map(int, input().split())
edges = []
for _ in range(E):
    s, t, w = map(int, input().split())
    edges.append([s, t, w])

def find_minimum_arborescence(V, edges, root):
    # Si un seul sommet
    if V == 1:
        return 0
    # On prépare les arêtes entrantes de chaque sommet
    incoming = [[] for _ in range(V)]
    for s, t, w in edges:
        heapq.heappush(incoming[t], (w, s))
    # Sélectionne la plus petite arête entrante pour chaque sommet sauf la racine
    min_edge = [(0, -1) for _ in range(V)]
    for t in range(V):
        if t == root:
            continue
        if incoming[t]:
            w, s = heapq.heappop(incoming[t])
            min_edge[t] = (w, s)
    used = [False]*V
    history = []
    cycle = []
    for t in range(V):
        if used[t] or min_edge[t][1] == -1:
            continue
        cur = t
        path = []
        while not used[cur]:
            used[cur] = True
            path.append(cur)
            next_s = min_edge[cur][1]
            if next_s == -1:
                path = []
                break
            cur = next_s
        if path and cur in path:
            idx = path.index(cur)
            cycle = path[idx:]
            break
    if not cycle:
        total = 0
        for w, s in min_edge:
            total += w
        return total
    # Compression du cycle
    parent = min(cycle)
    relabel = [0]*V
    k = 0
    for i in range(V):
        if i == parent:
            continue
        if i in cycle:
            relabel[i] = parent
        else:
            k += 1
            relabel[i] = k
    V2 = V - len(cycle) + 1
    new_edges = []
    for s, t, w in edges:
        s2 = relabel[s]
        t2 = relabel[t]
        if s in cycle and t in cycle:
            continue
        if t in cycle:
            w = w - min_edge[t][0]
            t2 = parent
        if s in cycle:
            s2 = parent
        new_edges.append([s2, t2, w])
    new_root = relabel[root]
    # Appel récursif sur le graphe contracté
    answer = find_minimum_arborescence(V2, new_edges, new_root)
    # On ajoute les poids des arêtes sélectionnées du cycle
    sum_cycle = 0
    for i in cycle:
        sum_cycle += min_edge[i][0]
    return answer + sum_cycle

print(find_minimum_arborescence(V, edges, r))