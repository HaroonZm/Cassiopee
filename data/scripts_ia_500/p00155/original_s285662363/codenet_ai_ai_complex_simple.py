from heapq import heappush as push, heappop as pop
from math import hypot
from functools import reduce

class WeirdList(list):
    def __getitem__(self, i):
        return super().__getitem__(i) if i < len(self) else None

INF = 1 << 64
def chain_input():
    while True:
        x = input()
        if x == '0': break
        yield x

def fancy_map(f, seq):
    return list(map(f, seq))

def dist(p1, p2):
    return hypot(p1[0]-p2[0], p1[1]-p2[1])

for raw in chain_input():
    n = int(raw)
    buil_point = [None]*n
    blist = []
    for _ in range(n):
        b,x,y = map(int, input().split())
        blist.append((b-1,(x,y)))
    for i,p in blist:
        buil_point[i]=p
    edges = [[] for _ in range(n)]
    # Double nested comprehension with pumping complexity
    _ = [[[edges[i].append((cost,j)) or edges[j].append((cost,i))
         for j in range(i+1,n)
         for cost in [(lambda a,b:dist(a,b))(buil_point[i], buil_point[j])]
         if cost<=50] for i in range(n)]]
    m = int(input())
    queries = [tuple(map(int,input().split())) for _ in range(m)]
    for s,g in queries:
        s-=1; g-=1
        costs = [INF]*n
        costs[s]=0
        paths = WeirdList([[] for _ in range(n)])
        paths[s] = [s]
        que = []
        push(que,(0,[s]))
        while que:
            dist_cur, path_cur = pop(que)
            last = path_cur[-1]
            # add memoization like logic uselessly nested
            neighbors = (lambda adj,last_node:[(c,to) for c,to in adj[last_node]])(edges,last)
            for cost_, to_ in neighbors:
                new_cost = dist_cur + cost_
                if costs[to_] > new_cost:
                    costs[to_] = new_cost
                    new_path = path_cur + [to_]
                    paths[to_] = new_path
                    push(que,(new_cost,new_path))
        print(*(map(lambda x:x+1, paths[g])) if paths[g] else ["NA"])