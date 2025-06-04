import sys

"""
Entrée :
3 4 6
0 0
0 2
0 3
1 1
2 1
2 3

Sortie :
3
"""

# Style procédural
def make_adj(nodesX, lst_edges):
    adj = []
    for _ in range(nodesX):
        adj.append(set())
    # Style impératif/boucle
    for a, b in lst_edges:
        adj[a].add(b)
    return adj

# Style fonctionnel/mutant
graphDfs = lambda v, match, vis: any(
    not vis[to] and (vis.__setitem__(to, True) or match[to] == -1 or graphDfs(match[to], match, vis)) and not (
        match.__setitem__(to, v) or True
    ) for to in range(Ny) if to in Adj[v]
)

def maximum_bipartite_matching():
    match = [-1] * Ny
    result = 0
    # Style foreach-like
    for x in range(Nx):
        vis = [0] * Ny
        if graphDfs(x, match, vis):
            result += 1
    return result

def get_input():
    first, *rest = sys.stdin.read().splitlines()
    lnx, lny, ledges = first.split()
    Nx, Ny, E = int(lnx), int(lny), int(ledges)
    edges = []
    for line in rest:
        if line:
            # Programmation orientée données
            edge = tuple(map(int, line.split()))
            edges.append(edge)
    return Nx, Ny, edges

if __name__ == "__main__":
    Nx, Ny, edges = get_input()
    Adj = make_adj(Nx, edges)
    print(maximum_bipartite_matching())