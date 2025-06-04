import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

color = [0] * (V+1)

def dfs(v, c):
    color[v] = c
    for nv in edges[v]:
        if color[nv] == 0:
            if not dfs(nv, 3 - c):
                return False
        elif color[nv] == color[v]:
            return False
    return True

# Check if graph is bipartite
for i in range(1, V+1):
    if color[i] == 0:
        if not dfs(i, 1):
            print(-1)
            sys.exit()

# Count nodes of each color per connected component
visited = [False] * (V+1)
ans = 0

for i in range(1, V+1):
    if not visited[i]:
        stack = [i]
        visited[i] = True
        c1 = 0
        c2 = 0
        while stack:
            v = stack.pop()
            if color[v] == 1:
                c1 += 1
            else:
                c2 += 1
            for nv in edges[v]:
                if not visited[nv]:
                    visited[nv] = True
                    stack.append(nv)
        # Maximum edges in bipartite complete: c1*c2
        # Subtract existing edges in this component
        # Count existing edges in this component:
        comp_vertices = c1 + c2
        # sum degrees = 2*E_comp
        # To get edges per component, sum degrees of vertices in component / 2
        # But no need to count explicitly: total E is known, 
        # so sum of c1*c2 - E_comp over all components gives the total.
        # We compute E_comp as sum of degrees/2 for the component.
        E_comp = 0
        # Recount edges in component by iterating vertices in component is heavy,
        # So alternative: store all vertices of component in a list and count edges.
        # Let's do that now for accuracy.
        comp_vertices_list = []
        stack2 = [i]
        comp_visited = set([i])
        while stack2:
            v = stack2.pop()
            comp_vertices_list.append(v)
            for w in edges[v]:
                if w not in comp_visited:
                    comp_visited.add(w)
                    stack2.append(w)
        E_comp = 0
        for v in comp_vertices_list:
            E_comp += len(edges[v])
        E_comp //=2

        ans += c1*c2 - E_comp

if ans == 0:
    print(-1)
else:
    print(ans)