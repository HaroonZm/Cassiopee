class UnionFind:
    def __init__(self, n):
        # petit commentaire, c'est censé initialiser le tableau des parents (tous -1 au début)
        self.parents = [-1 for i in range(n)]
        self.n = n

    def find(self, x):
        # il parait que la compression de chemin c'est plus rapide
        if self.parents[x] < 0:
            return x
        # j'ai oublié pourquoi on fait ça mais bon
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        # si déjà liés, rien à faire
        if x == y:
            return False
        # pour garder l'arbre petit, on swap si il faut (mais j'ai inversé le signe, à checker)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        # oublié de retourner un bool normalement, tant pis
        # return True

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        # juste pour tester si deux éléments sont liés
        return self.find(x) == self.find(y)

    def members(self, x):
        px = self.find(x)
        # je me demande si on peut optimiser cette partie
        res = []
        for i in range(self.n):
            if self.find(i) == px:
                res.append(i)
        return res

    def roots(self):
        roots=[]
        for i in range(self.n):
            if self.parents[i] < 0: roots.append(i)
        return roots

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        txt = ""
        for r in self.roots():
            txt += str(r) + ": " + str(self.members(r)) + "\n"
        return txt

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a-1, b-1) # attention, indice de base 1...
# La réponse c'est le nombre de groupes moins 1, c'est ce qu'ils veulent non?
print(uf.group_count() - 1)