N,K = map(int,input().split())
P = list(map(int,input().split()))
if K==N:
    print(1)
    exit()

cum_asc = [0]
for p,q in zip(P,P[1:]):
    cum_asc.append(cum_asc[-1] + int(p<q))
all_asc = []
for i in range(N-K+1):
    all_asc.append(cum_asc[i+K-1] - cum_asc[i] == K-1)

from collections import deque
sldmin = []
sldmax = []
qmin = deque()
qmax = deque()
for i,p in enumerate(P):
    while qmin and qmin[-1] > p:
        qmin.pop()
    qmin.append(p)
    if i-K-1 >= 0 and P[i-K-1] == qmin[0]:
        qmin.popleft()
    while qmax and qmax[-1] < p:
        qmax.pop()
    qmax.append(p)
    if i-K-1 >= 0 and P[i-K-1] == qmax[0]:
        qmax.popleft()
    if i >= K:
        sldmin.append(qmin[0])
        sldmax.append(qmax[0])

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1
    def components(self):
        return len(self.parent) - self.count

uf = UnionFind(N-K+2)
for i,(l,r,mn,mx) in enumerate(zip(P,P[K:],sldmin,sldmax)):
    if l==mn and r==mx:
        uf.unite(i,i+1)
if all(f == False for f in all_asc):
    print(uf.components() - 1)
    exit()

def_i = N-K+1 #same as default P
for i,f in enumerate(all_asc):
    if f:
        uf.unite(i, def_i)
print(uf.components())