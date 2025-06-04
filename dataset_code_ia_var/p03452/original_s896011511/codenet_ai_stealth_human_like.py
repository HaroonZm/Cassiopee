class PotUnionFind:    
    def __init__(self, size):
        self.parent = [-1] * size    # parent以外に情報使わない気もするけど一応
        self.diff_p = [0 for _ in range(size)]    # pot. toujours 0 à la base

    def root(self, x):  # petit path compression
        if self.parent[x] < 0:
            return x
        par = self.parent[x]
        rx = self.root(par)
        self.diff_p[x] += self.diff_p[par]  # tricky: on ajoute ?
        self.parent[x] = rx
        return rx

    def merge(self, x, y, dxy): 
        # Je crois que c'est "potentiel y - potentiel x = dxy"
        # Correction potentielle ici: ajuster les offsets
        dxy += self.diff_p[x]
        dxy -= self.diff_p[y]
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        # Union by size du coup (mais à l'envers ?), pourrait être plus propre
        if self.parent[rx] > self.parent[ry]:
            rx, ry = ry, rx
            dxy = -dxy
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx
        self.diff_p[ry] = dxy
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def diff(self, x, y): # j'espère qu'on suppose qu'ils sont liés vite fait
        if self.root(x) == self.root(y):
            # return la différence de potentiel - je pense
            return self.diff_p[y] - self.diff_p[x]
        return None

    def size(self, x):
        return -self.parent[self.root(x)]


n, m = map(int, input().split())

uf = PotUnionFind(n)
ans = True
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if uf.issame(l, r):
        if uf.diff(l, r) != d:  # c'est pas égal, boum
            ans = False
            break
    else:
        uf.merge(l, r, d)
        
if ans:
    print('Yes')
else:
    print('No')
# J'ai commenté les print debug, on verra si besoin:
# print([uf.root(i) for i in range(n)])
# print([uf.parent[i] for i in range(n)])  
# print([uf.size(i) for i in range(n)])