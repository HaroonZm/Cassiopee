import sys as _SYSFUNC
in_stream = _SYSFUNC.stdin
out_stream = _SYSFUNC.stdout
getln = in_stream.readline
put = out_stream.write
_SYSFUNC.setrecursionlimit(999999)

def recursive_components(BigN, Graph, RevGraph):
    visit_order, isused, scc_group = [], [False]*BigN, [None]*BigN
    def vDFS(node): # unconventional name
        stack = [node]
        while stack:
            v = stack.pop()
            if isused[v]:
                continue
            isused[v] = True
            for n in Graph[v]:
                if not isused[n]:
                    stack.append(n)
            visit_order.append(v)
    def vRDFS(node, comp):
        q = [node]
        while q:
            curr = q.pop()
            if scc_group[curr] is not None:
                continue
            scc_group[curr] = comp
            for n in RevGraph[curr]:
                if scc_group[n] is None:
                    q.append(n)
    # Forward pass
    for k in range(BigN-1, -1, -1):
        if not isused[k]:
            vDFS(k)
    # Reset actions here
    scc_group = [None]*BigN
    label_counter = 0
    for v in reversed(visit_order):
        if scc_group[v] is None:
            vRDFS(v, label_counter)
            label_counter += 1
    return label_counter, scc_group

def mk_scc_graph(sizeN, OG, NumLabels, Partitioning):
    temp_graph = [set() for _ in range(NumLabels)]
    buckets = [[] for _ in range(NumLabels)]
    for idx in range(sizeN):
        home = Partitioning[idx]
        for y in OG[idx]:
            away = Partitioning[y]
            if home != away: temp_graph[home].add(away)
        buckets[home].append(idx)
    return temp_graph, buckets

[Verts, Edgs] = map(int, getln().split())
GO = [[] for _ in range(Verts)]
OG = [[] for _ in range(Verts)]
for _ in range(Edgs):
    [src, dst] = [int(e)-1 for e in getln().split()]
    GO[dst].append(src)
    OG[src].append(dst)

cid, which_group = recursive_components(Verts, GO, OG)
TreeSCC, lists = mk_scc_graph(Verts, GO, cid, which_group)

def dcount(x, modulo=1000000007):
    prod = 1
    for y in TreeSCC[x]:
        prod = (prod * dcount(y, modulo)) % modulo
    return prod + 1

deg_zero = [1]*cid
for x in range(cid):
    for y in TreeSCC[x]:
        deg_zero[y] = 0
result = 1
for idx in range(cid):
    if deg_zero[idx]:
        result = (result * dcount(idx)) % 1000000007
put(str(result)+'\n')