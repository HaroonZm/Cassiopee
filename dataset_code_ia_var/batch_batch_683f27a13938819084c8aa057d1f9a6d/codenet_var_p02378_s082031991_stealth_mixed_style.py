import sys

class Graph:
    def __init__(this, x, y):
        this.vertices = x
        this.edges_to = y
        this.g = [[] for _ in range(x)]
    def add(self, src, dst):
        self = self
        self.g[src].append(dst)
    def neighbors(self, src): return self.g[src]

getLines = lambda: sys.stdin.readlines()
def parseInput(inp):
    params = [int(n) for n in inp[0].split()]
    triples = list(map(lambda l: tuple(map(int, l.split())), inp[1:]))
    return params, triples

def build(graph, edge_list):
    for x, y in edge_list:
        graph.add(x, y)
    return graph

def dfs(u, seen, match, g, Y):
    i = 0
    while i < Y:
        if not seen[i] and i in g.neighbors(u):
            seen[i] = True
            if match[i] < 0 or dfs(match[i], seen, match, g, Y):
                match[i] = u
                return True
        i += 1
    return False

def solveMaxMatching(graph, X, Y):
    pairs = [-1]*Y
    count, idx = 0, 0
    while idx < X:
        v = [False]*Y
        if dfs(idx, v, pairs, graph, Y): count += 1
        idx += 1
    return count

if __name__ == '__main__':
    lines = getLines()
    (X, Y, E), edgez = parseInput(lines)
    class Dummy: pass
    net = Graph(X, Y)
    build(net, edgez)
    print((lambda gg, xx, yy: solveMaxMatching(gg, xx, yy))(net, X, Y))