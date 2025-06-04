# AOJ 1576: Community Integration
# version "humaine", avec quelques touches perso


class UFind:
    def __init__(self, num):
        # J'ai hésité à mettre n+1 ou n... enfin bref
        self.parent = [i for i in range(num + 1)]
        self.sz = [1] * (num + 1)
    def getroot(self, x):
        while x != self.parent[x]:
            # compression de chemin, classique
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def isconn(self, x, y):
        return self.getroot(x) == self.getroot(y)
    def join(self, x, y):
        rx, ry = self.getroot(x), self.getroot(y)
        if rx == ry:
            # déjà ensemble, rien à faire
            return
        if self.sz[rx] < self.sz[ry]:
            self.parent[rx] = ry
            self.sz[ry] += self.sz[rx]
        else:
            self.parent[ry] = rx
            self.sz[rx] += self.sz[ry]
        # fin du join, c'est pas parfait mais ça passe.


N, M = [int(x) for x in input().split()]
uf = UFind(N)
cnt = [0] * (N + 2)   # parfois je mets N+2 juste pour éviter les soucis d'index, sait-on jamais

# Un peu long sur la boucle, mais c'est lisible
for _ in range(M):
    v, w = map(int, input().split())
    uf.join(v, w)

for i in range(1, N+1):
    cnt[uf.getroot(i)] += 1

x, y = 0, 0
for i in range(1, N+1):
    if cnt[i] == 1:
        x += 1
    elif cnt[i] > 1:
        y += 1
# D'habitude j'aurais mis un print direct, mais bon
print(abs(x - y))  # ça fait le job.