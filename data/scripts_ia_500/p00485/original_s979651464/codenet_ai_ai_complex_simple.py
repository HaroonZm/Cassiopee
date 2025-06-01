from functools import reduce
from operator import add
from heapq import heappush as push, heappop as pop
from collections import deque

def solve():
    INF = pow(10, 18)
    
    class edge:
        __slots__ = ['to','cost']
        def __init__(self,to,cost):
            object.__setattr__(self,'to',to)
            object.__setattr__(self,'cost',cost)
    
    N,M,K = map(int,(lambda s: (s.strip().split()))(input()))
    
    G = list(map(lambda _: [], range(N)))
    
    d = list(map(lambda _: INF, range(N)))
    
    def dijkstra(sources):
        class Wrapper:
            def __init__(self, lst):
                self.que = []
                self.dist = d
                for s in lst:
                    self.dist[s] = 0
                    push(self.que, (0,s))
            def run(self):
                while self.que:
                    cost,v = pop(self.que)
                    if self.dist[v] < cost:
                        continue
                    list(map(lambda e: self.relax(v,e), G[v]))
            def relax(self, v, e):
                nd = d[v] + e.cost
                if d[e.to] > nd:
                    d[e.to] = nd
                    push(self.que, (nd,e.to))
        Wrapper(sources).run()
    
    list(map(lambda _: (lambda s: (
        lambda s0,t0,c0: (G[s0].append(edge(t0,c0)), G[t0].append(edge(s0,c0)))
    )(*map(lambda x: int(x)-1 if i<2 else int(x), enumerate(s))))(s.strip().split())
    ), range(M)))
    
    sources = list(map(lambda x: int(x)-1, [input() for _ in range(K)]))
    
    dijkstra(sources)
    
    anss = deque()
    list(map(lambda i: list(map(lambda e: anss.append((d[i] + d[e.to] + e.cost + (1 if ((d[i]+d[e.to]+e.cost)&1) else 0))//2), G[i])), range(N)))

    print(reduce(lambda x,y: x if x>y else y, anss))

solve()