import sys
sys.setrecursionlimit(10**6)

class G:
    def __init__(self, nodes):
        self.g = {}
        for j in range(1, nodes+1):
            self.g[j] = []

def search(g, vis, node, color):
    vis[node] = color
    for nb in g[node]:
        if vis[nb] == color:
            return 0
        if not vis[nb]:
            if not search(g, vis, nb, -color):
                return 0
    return 1

def process():
    while 1:
        a, b = map(int, input().split())
        if not a: break
        S = G(a)
        for _ in range(b):
            x, y = [int(u) for u in input().split()]
            S.g[x].append(y)
            S.g[y].append(x)
        V = [0]*(a+1)
        z = search(S.g, V, 1, 1)
        if not z:
            print(0)
        else:
            p,q=0,0
            for idx in range(1, a+1):
                if V[idx]==1:
                    p+=1
                elif V[idx]==-1:
                    q+=1
            X = []
            if p%2==0: X.append(p//2)
            if q%2==0: X.append(q//2)
            seen = {}
            print(len(set(X)))
            for item in sorted(set(X)):
                print(item)

process()