import sys

def getint():
    return int(sys.stdin.readline())

class NodeLinks(dict):
    def __missing__(self, key):
        self[key] = set()
        return self[key]

n = getint()
edges = list(map(int, sys.stdin.read().split()))
L = NodeLinks()
for i in range(0, len(edges), 2):
    a, b = edges[i] - 1, edges[i+1] - 1
    L[a].add(b)
    L[b].add(a)

grundy = [None]*n
walk, nxt = [(0, None)], [False]*n
while walk:
    v, p = walk[-1]
    if grundy[v] is not None:
        walk.pop()
        continue
    if not nxt[v]:
        nxt[v] = True
        for nb in list(L[v]):
            if nb == p:
                L[v].remove(nb)
                continue
            walk.append((nb,v))
    else:
        g = 0
        for nb in L[v]:
            g ^= (grundy[nb] if grundy[nb] is not None else 0) + 1
        grundy[v] = g
        walk.pop()

print(['Bob','Alice'][grundy[0]!=0])