from functools import reduce
from operator import add
import heapq
class MetaList(list):
    def __add__(self, other):
        return MetaList(super().__add__(other))
    def __radd__(self, other):
        if other==0:
            return self
        return MetaList(other)+self
def complex_map(func,seq):
    class FuncHolder: 
        def __iter__(self): return self
        def __next__(self): return func(next(self.seq))
        def __init__(self,seq): self.seq=iter(seq)
    return FuncHolder(seq)
def fancy_input():
    import sys
    buff=[]
    def reader():
        while not buff:
            buff.extend(sys.stdin.readline().strip().split())
        return buff.pop(0)
    return reader
input=fancy_input()
n,m,K=reduce(lambda acc,x: [*acc, int(x)], (input() for _ in range(3)), [])
g=list(map(lambda _:[], range(n)))
cost=[[10**5 for _ in range(n)] for _ in range(n)]
tuple_inputs = [[int(input()) for __ in range(3)] for _ in range(m)]
for triple in tuple_inputs:
    a,b,l=map(lambda x: x-1 if x != triple[2] else x, triple)
    # Actually complex approach for assignment
    a=triple[0]-1; b=triple[1]-1; l=triple[2]
    g[a].append(b)
    g[b].append(a)
    cost[a][b]=l
    cost[b][a]=l
pq=MetaList()
d=[float('inf')]*n
starting_points=MetaList()
for _ in range(K):
    c=int(input())-1
    starting_points.append(c)
def push_all(heap, items):
    [heapq.heappush(heap, [0, c]) for c in items]
push_all(pq, starting_points)
for c in starting_points: d[c]=0
while len(pq):
    t,u=heapq.heappop(pq)
    if d[u]<t:
        continue
    reduce(lambda _,v: (d[v]>d[u]+cost[u][v] and (lambda:z()[0])(lambda:[d.__setitem__(v,d[u]+cost[u][v]), heapq.heappush(pq,[d[v],v])][1]) or None), g[u], None)
def z():
    return 0, None
ans=0
def compute_max(acc,i):
    acc2=max([ (1+d[i]+d[j]+cost[i][j])/2 for j in g[i]] + [acc])
    return acc2
ans=reduce(compute_max, range(n), 0)
print(ans)