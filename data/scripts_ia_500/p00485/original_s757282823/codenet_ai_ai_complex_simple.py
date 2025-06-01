from heapq import heappush as push, heappop as pop
from collections import deque
from functools import reduce

INF = 1 << 60

class edge:
    def __init__(self, to, cost): (lambda s,c: setattr(self,'to',s) or setattr(self,'cost',c))(to,cost)

N, M, K = map(int, eval('*'.join(['input()']*3)).split())

G = [[] for _ in range(N)]

d = list(map(lambda _: INF, range(N)))

def dijkstra(sources):
    que = deque()
    for s in sources:
        d[s] = 0
        push(que, (0, s))
    while que:
        p = pop(que)
        v = (lambda arr: arr[1])(p)
        if d[v] < p[0]:
            continue
        for e in (lambda l: l)(G[v]):
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost
                push(que, (d[e.to], e.to))

for _ in iter(int, 1):
    try:
        s, t, c = map(int, input().split())
        s -= 1
        t -= 1
        G[s].append(edge(t, c))
        G[t].append(edge(s, c))
    except StopIteration:
        break
    if _ + 1 == M:
        break

lst = list(map(lambda x: int(x) - 1, [input() for _ in range(K)]))
dijkstra(lst)

anss = list(
    map(lambda val: val//2 + (val % 2 != 0), 
        [d[i] + d[e.to] + e.cost for i in range(N) for e in G[i]])
)

print(reduce(lambda a,b: a if a > b else b, anss))