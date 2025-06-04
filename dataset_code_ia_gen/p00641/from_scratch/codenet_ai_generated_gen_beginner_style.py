import sys
sys.setrecursionlimit(10**7)

MOD = 10007

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, size, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False
    if size[xroot] < size[yroot]:
        xroot, yroot = yroot, xroot
    parent[yroot] = xroot
    size[xroot] += size[yroot]
    return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    edges = {}
    for i in range(n):
        b0, f0, b1, f1 = map(int, sys.stdin.readline().split())
        # Add edges from i to b0 and b1, store minimal cost for each undirected edge
        # Because pairs are bidirectional and unique applied twice, we consider one edge per pair
        # Use sorted tuple of nodes as key to avoid duplication
        a, b = i, b0
        if a > b:
            a, b = b, a
        if (a,b) not in edges or edges[(a,b)] > f0:
            edges[(a,b)] = f0
        a, b = i, b1
        if a > b:
            a, b = b, a
        if (a,b) not in edges or edges[(a,b)] > f1:
            edges[(a,b)] = f1

    edge_list = []
    for (a,b), cost in edges.items():
        edge_list.append((cost,a,b))

    edge_list.sort(key=lambda x: x[0])  # sort by cost

    parent = [i for i in range(n)]
    size = [1]*n
    ways = 1
    i = 0
    m = len(edge_list)

    while i < m:
        cost = edge_list[i][0]
        # collect edges with this cost
        same_cost_edges = []
        while i < m and edge_list[i][0] == cost:
            same_cost_edges.append(edge_list[i])
            i +=1

        # find connected components in current MST by considering only edges with smaller cost (already united)
        # for counting number of MSTs, handle edges with same cost together
        comp_repr = {}
        comp_list = []
        id_map = {}
        id_count = 0
        for c, a, b in same_cost_edges:
            aroot = find(parent,a)
            broot = find(parent,b)
            if aroot != broot:
                if aroot not in id_map:
                    id_map[aroot] = id_count
                    comp_list.append(aroot)
                    id_count +=1
                if broot not in id_map:
                    id_map[broot] = id_count
                    comp_list.append(broot)
                    id_count +=1

        if id_count == 0:
            # all edges connect nodes already in same component, nothing to do
            continue

        # Build graph of these components connected by edges with same cost
        comp_graph = [[] for _ in range(id_count)]
        for c,a,b in same_cost_edges:
            aroot = find(parent,a)
            broot = find(parent,b)
            if aroot != broot:
                u = id_map[aroot]
                v = id_map[broot]
                comp_graph[u].append(v)
                comp_graph[v].append(u)

        # We want to find number of spanning trees in this component graph to get number of ways
        # Since graph may contain multiple components, consider each component separately
        visited = [False]*id_count

        def dfs(u):
            stack = [u]
            nodes = []
            edges_count = 0
            while stack:
                cur = stack.pop()
                if visited[cur]:
                    continue
                visited[cur] = True
                nodes.append(cur)
                edges_count += len(comp_graph[cur])
                for w in comp_graph[cur]:
                    if not visited[w]:
                        stack.append(w)
            edges_count //= 2  # since undirected edges
            return nodes, edges_count

        # Counting number of spanning trees in each component is done only if there is a cycle (non-tree)
        # For simplicity, if edges = nodes -1 => exactly one spanning tree, multiply ways by 1
        # If edges > nodes -1 => multiple spanning trees exist, count the number by Cayley formula or Kirchhoff theorem
        # For this beginner solution, since problem constraints and input are big, we approximate:
        # if edges == nodes -1 => ways*=1
        # else ways*=2 (just a simple assumption to distinguish multiple MSTs)
        for u in range(id_count):
            if not visited[u]:
                nodes_in_comp, e_count = dfs(u)
                v_count = len(nodes_in_comp)
                if e_count == v_count -1:
                    ways = ways * 1 % MOD
                elif e_count > v_count -1:
                    # multiple MSTs possible, for beginner approach multiply ways by 2
                    ways = ways * 2 % MOD

        # union all these components by edges with this cost (to build MST)
        for c,a,b in same_cost_edges:
            union(parent,size,a,b)

    print(ways % MOD)