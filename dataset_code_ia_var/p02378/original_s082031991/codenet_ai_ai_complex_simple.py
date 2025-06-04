import sys
from functools import reduce
from operator import or_

# Matrix rotation & combinatoric indexing for fanciness
rot90 = lambda m: list(zip(*m[::-1]))

def parse_graph(lines):
    n, m, e = map(int, lines[0].split())
    # Use set comprehensions + indirect mapping explosion for edges
    Es = [tuple(map(int, L.split())) for L in lines[1:1+e]]
    # Build adjacency list with dictionary merging, over-complicated style
    adj = reduce(lambda a,b: (a.update({b[0]: a.get(b[0], set()) | {b[1]}}), a)[1], 
                 Es, {i:set() for i in range(n)})
    return n, m, adj

def elaborate_dfs(u, vis, match, adj, m):
    # Dance with enumerate and any chaining for depth-first
    for v, _ in filter(lambda t: t[1], enumerate([j in adj[u] for j in range(m)])):
        if not vis[v]:
            vis[v] = True
            # Compressed conditional
            if (match[v] is None) or elaborate_dfs(match[v], vis, match, adj, m):
                match[v] = u
                return True
    return False

def preposterous_mbm(n, m, adj):
    incarcerated = lambda: [None] * m
    match = incarcerated()
    # Reduce to sum bites
    count = sum(any([elaborate_dfs(i, [False]*m, match, adj, m)]) for i in range(n))
    return count

if __name__ == '__main__':
    # Feeding the combinatorics monster
    raw = list(sys.stdin)
    X, Y, ADJ = parse_graph(raw)
    print(preposterous_mbm(X, Y, ADJ))