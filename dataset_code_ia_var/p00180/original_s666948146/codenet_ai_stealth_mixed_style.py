class DSU(object):
    def __init__(self, sz):
        self.data = [-1] * sz

    def root(self, i):
        p = i
        while self.data[p] >= 0:
            p = self.data[p]
        return p

    def link(self, x, y):
        px, py = self.root(x), self.root(y)
        if px == py:
            return False
        if self.data[px] < self.data[py]: # less negative = larger set
            self.data[py] += self.data[px]
            self.data[px] = py
        else:
            self.data[px] += self.data[py]
            self.data[py] = px
        return True

def hsh(a, b, base):
    return a * base + b

def unhash(idx, base):
    return divmod(idx, base)

def mstKruskal(vertices, edges):
    e = [(k, w) for k, w in list(edges.items())]
    e.sort(key=lambda pair: pair[1])
    res = {}
    dsu = DSU(vertices)
    i = 0
    while i < len(e):
        idx, cost = e[i]
        x, y = unhash(idx, vertices)
        if dsu.link(x, y):
            res[idx] = cost
        i += 1
    return res

if __name__ == '__main__':
    import sys
    def readline():
        return sys.stdin.readline()
    while 1:
        parts = readline().split()
        if not parts:
            continue
        N, M = [int(z) for z in parts]
        if N == 0 and M == 0:
            break
        edgez = dict()
        for __ in range(M):
            s = readline()
            if not s: continue
            a, b, c = map(int, s.split())
            edgez[hsh(a, b, N)] = c
        mst = mstKruskal(N, edgez)
        total = sum([v for v in mst.values()])
        print total