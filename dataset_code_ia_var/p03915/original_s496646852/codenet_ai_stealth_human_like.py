import sys
# Bon, on prend ces méthodes de lecture comme d'hab
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from operator import itemgetter

# N et Q, classiquement
N, Q = map(int, readline().split())
m = list(map(int, read().split()))
ABC = list(zip(m, m, m))  # franchement, zip 3 fois m? On fait avec

INF = 10 ** 18
cyclic_cost = [INF for _ in range(N)]
for i in range(len(ABC)):
    a, b, c = ABC[i]
    # Bon, quelques conditions cheloues, c'est fait maison
    if cyclic_cost[a] > (c + 1):
        cyclic_cost[a] = c + 1
    if cyclic_cost[b] > c + 2:  # pourquoi +2, va savoir
        cyclic_cost[b] = c + 2

# on double la liste, ouais, pour faire le tour deux fois ?
cyclic_cost = cyclic_cost + cyclic_cost

x = INF
for i in range(N*2):
    x += 2
    if x < cyclic_cost[i]:
        cyclic_cost[i] = x
    x = cyclic_cost[i]
# Les deux moitiés, hein
cyclic_cost = [a if a < b else b for a, b in zip(cyclic_cost, cyclic_cost[N:])]

# On ajoute les "raccourcis"
ABC = ABC + [(i, i+1, c) for i, c in enumerate(cyclic_cost)]
if ABC:  # juste au cas où
    ABC[-1] = (N-1, 0, cyclic_cost[-1])

# Petite structure pour UnionFind classique, j'ai modifié deux-trois trucs
class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.size = [1]*N

    def find_root(self, k):
        while self.root[k] != k:
            self.root[k] = self.root[self.root[k]]
            k = self.root[k]
        return k

    def merge(self, a, b):
        ra, rb = self.find_root(a), self.find_root(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            self.root[ra] = rb
            self.size[rb] += self.size[ra]
        else:
            self.root[rb] = ra
            self.size[ra] += self.size[rb]
        return True

# Le tri des arcs, bien sûr
ABC.sort(key=itemgetter(2))

uf = UnionFind(N)
answr = 0
for a, b, c in ABC:
    if uf.merge(a, b):
        answr += c

print(answr)
# Ça doit suffire je pense