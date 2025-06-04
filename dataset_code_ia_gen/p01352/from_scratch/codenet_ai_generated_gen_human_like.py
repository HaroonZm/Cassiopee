import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())

# Pour gérer les suppressions efficaces, on traite le problème en offline :
# On enregistre les intervalles de temps pendant lesquels chaque arête existe.
# Puis on effectue une recherche divisée sur l'intervalle de requêtes.

edges = dict()
queries = []
# Chaque arête est identifiée par (min(u,v), max(u,v)) pour éviter doublons
for i in range(k):
    t, u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    queries.append((t, u, v))

intervals = dict()  # edge -> list of (start, end)

active = dict()  # edge -> start_time

for i, (t, u, v) in enumerate(queries):
    if t == 1:
        # construction
        # l'arête u-v commence à exister à i
        active[(u,v)] = i
    elif t == 2:
        # destruction
        start = active.pop((u,v))
        if (u,v) not in intervals:
            intervals[(u,v)] = []
        intervals[(u,v)].append( (start, i) )
    else:
        # question, pas d'update sur edge
        pass
# Les arêtes encore actives à la fin continuent jusqu'à k
for e, start in active.items():
    if e not in intervals:
        intervals[e] = []
    intervals[e].append( (start, k) )

# DSU (Union-Find) avec rollback
class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1]*n
        self.history = []
        self.comp = n
    
    def find(self, x):
        while self.par[x]!=x:
            x=self.par[x]
        return x
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.history.append((-1, -1, -1))
            return
        if self.sz[a]<self.sz[b]:
            a,b=b,a
        # a is root of bigger set
        self.history.append((b, self.par[b], self.sz[a]))
        self.par[b] = a
        self.sz[a] += self.sz[b]
        self.comp -= 1
    
    def rollback(self):
        b, pb, sa = self.history.pop()
        if b == -1:
            return
        a = self.par[b]
        self.par[b] = pb
        self.sz[a] = sa
        self.comp += 1

dsu = DSU(n)

# Segment tree pour appliquer les arêtes sur les intervalles
# On stocke dans chaque noeud les arêtes qui sont actives totalement dans l'intervalle du noeud
# Puis on descend dans l'arbre et finalement on répond aux queries 

seg_size = 1
while seg_size < k:
    seg_size <<= 1
tree = [[] for _ in range(seg_size*2)]

def add_edge(l, r, e, x, lx, rx):
    if r<=lx or rx<=l:
        return
    if l<=lx and rx<=r:
        tree[x].append(e)
        return
    m = (lx+rx)//2
    add_edge(l,r,e,2*x+1,lx,m)
    add_edge(l,r,e,2*x+2,m,rx)

for e, intervals_list in intervals.items():
    for (start, end) in intervals_list:
        add_edge(start, end, e, 0, 0, seg_size)

ans = []
def dfs(i, lx, rx):
    for u, v in tree[i]:
        dsu.union(u,v)
    if rx - lx == 1:
        t, u, v = queries[lx]
        if t == 3:
            if dsu.find(u) == dsu.find(v):
                ans.append("YES")
            else:
                ans.append("NO")
    else:
        m = (lx + rx)//2
        dfs(2*i+1, lx, m)
        dfs(2*i+2, m, rx)
    for _ in tree[i]:
        dsu.rollback()

dfs(0,0,seg_size)

print("\n".join(ans))