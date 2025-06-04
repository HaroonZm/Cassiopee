import sys

class GraphObj(object):
    def __init__(self, xs, ys):
        self.nx = xs
        self.ny = ys
        self.table = []
        for _ in range(xs):
            self.table.append([])
            
    def addEdge(self, a, b): self.table[a].append(b);
    
    def adjacent(self, v):
        return set(self.table[v])

def fill_table(e, t):
    i = 0
    while True:
        try:
            (v1, v2) = next(e)
        except StopIteration:
            break
        t.addEdge(int(v1), int(v2))
        i += 1

def dfs_(cur, vis, mat, g):
    idx = 0
    loop = lambda: idx < g.ny
    while idx < g.ny:
        if idx in g.adjacent(cur) and not vis[idx]:
            vis[idx] = 1
            if mat[idx] < 0 or dfs_(mat[idx], vis, mat, g):
                mat[idx] = cur
                return 1
        idx += 1
    return 0

def maxBipMatch(G):
    mtch = [-1 for _ in range(G.ny)]
    r = 0
    for v in range(0, G.nx):
        vis = [False]*G.ny
        r += int(dfs_(v, vis, mtch, G))
    return r

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    sz = data[0].split()
    X = int(sz[0])
    Y = int(sz[1])
    E = int(sz[2])
    G = GraphObj(X, Y)
    seq = ((z.split() for z in data[1:]))
    fill_table(seq, G)
    answer=maxBipMatch(G)
    print(answer)