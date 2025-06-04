import sys
sys.setrecursionlimit(10**7)

def read_polygon():
    coords = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '-1':
            break
        x,y = map(int,line.split())
        coords.append((x,y))
    return coords

def edges_of_polygon(poly):
    n = len(poly)
    edges = []
    for i in range(n):
        a,b = poly[i], poly[(i+1)%n]
        if a < b:
            edges.append((a,b))
        else:
            edges.append((b,a))
    return set(edges)

def polygons_touch(edges1, edges2):
    return len(edges1 & edges2) > 0

def color_map(adj, n):
    colors = [-1]*n
    def dfs(u):
        used = set()
        for w in adj[u]:
            if colors[w] != -1:
                used.add(colors[w])
        for c in range(1,5):
            if c not in used:
                colors[u] = c
                break

    # Try colors 1..4 greedy based on degree order
    deg = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -deg[x])
    for u in order:
        dfs(u)
    maxc = max(colors)
    # If maxc < 4, try to reduce colors. Because at most 10 countries, try all with backtracking
    def valid(u):
        for w in adj[u]:
            if colors[u]==colors[w]:
                return False
        return True
    countries = n
    best = maxc
    res = colors[:]
    def backtrack(i, maxcolor):
        nonlocal best,res
        if i==countries:
            if maxcolor<best:
                best = maxcolor
                res = colors[:]
            return
        for c in range(1,maxcolor+1):
            colors[i] = c
            if valid(i):
                backtrack(i, maxcolor)
        if maxcolor<4:
            colors[i] = maxcolor+1
            if valid(i):
                backtrack(i, maxcolor+1)
            colors[i] = -1
    colors = [-1]*countries
    backtrack(0,1)
    return best

while True:
    line = sys.stdin.readline()
    if not line:
        break
    n = int(line)
    if n==0:
        break
    territories = []
    countries_map = {}
    idx = 0
    for _ in range(n):
        country = sys.stdin.readline().strip()
        poly = read_polygon()
        territories.append( (country, poly) )
        if country not in countries_map:
            countries_map[country] = idx
            idx+=1
    country_count = len(countries_map)
    # Build adjacency graph between countries
    # For each country we store all edges of their territories
    country_edges = [set() for _ in range(country_count)]
    for ctry, poly in territories:
        cidx = countries_map[ctry]
        country_edges[cidx].update(edges_of_polygon(poly))
    adj = [set() for _ in range(country_count)]
    for i in range(country_count):
        for j in range(i+1,country_count):
            if polygons_touch(country_edges[i], country_edges[j]):
                adj[i].add(j)
                adj[j].add(i)
    # Find minimal coloring of graph with up to 4 colors
    result = color_map(adj, country_count)
    print(result)