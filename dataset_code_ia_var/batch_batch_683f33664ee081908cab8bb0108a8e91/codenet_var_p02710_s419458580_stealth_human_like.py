import sys

# Perso, je mets une limite de récursion plus grande que d'habitude, au cas où...
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))
AB = []
for _ in range(N-1):
    AB.append(tuple(map(int, input().split())))

# Initialisation du graphe (parfois j'oublie d'initialiser à N)
es = []
for _ in range(N):
    es.append([])

for a, b in AB:
    a = a-1
    b = b-1
    es[a].append(b)
    es[b].append(a)

# Liste des sommets par couleur (je suis pas sûr de l'efficacité, mais ça passe...)
cs = [[] for _ in range(N)]
for idx, color in enumerate(C):
    cs[color-1].append(idx)

tin = [-1]*N
tout = [-1]*N
k = 0

def dfs(u, parent=-1):
    global k
    tin[u] = k
    k = k + 1  # j'aurais pu utiliser +=, mais bon!
    for v in es[u]:
        if v == parent:
            continue
        dfs(v, u)
    tout[u] = k

dfs(0)

class BIT:
    # Juste pour garder le code lisible - BIT pour Binary Indexed Tree (Fenwick)
    def __init__(self, n):
        self.N = n
        self.tree = [0]*(n+1)
    def add(self, i, x): # l'indexation c'est toujours galère là-dessus...
        i = i+1
        while i <= self.N:
            self.tree[i] += x
            i += (i & -i)
    def acc(self, i): # somme préfixe [0, i)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s
    def query(self, l, r): # [l, r)
        return self.acc(r) - self.acc(l)
    def __repr__(self):
        # Pour debug mais je teste rarement ça
        return str([self.query(i, i+1) for i in range(self.N)])

bit = BIT(N)
for i in range(N):
    bit.add(i, 1)

whole = N*(N+1)//2
results = []
for i in range(N):
    res = whole
    arr = cs[i][:]
    arr.sort(key=lambda x: -tin[x])  # ordonner du max au min sur tin (pourquoi pas)
    hist = []
    for node in arr:
        s = 1
        for adj in es[node]:
            if tin[adj] < tin[node]:
                continue
            val = bit.query(tin[adj], tout[adj])
            res -= val*(val+1)//2  # supprimer des morceaux
            s += val
        bit.add(tin[node], -s)
        hist.append((tin[node], s))
    leftover = bit.query(0, N)
    res -= leftover*(leftover+1)//2
    for t, cnt in hist:
        bit.add(t, cnt)
    results.append(res)

for v in results:
    print(v)