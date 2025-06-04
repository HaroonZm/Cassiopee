from heapq import heappush, heappop
from collections import defaultdict

class Dijkstra:
    """高効率なダイクストラ法実装。隣接リストにdefaultdictを利用。"""

    __slots__ = ('_G', '_V', '_E')

    def __init__(self, V):
        self._V = V
        self._E = 0
        self._G = defaultdict(list)

    @property
    def V(self): return self._V

    @property
    def E(self): return self._E

    def add(self, u, v, cost):
        self._G[u].append((v, cost))
        self._E += 1

    def shortest_path(self, start):
        dist = [float('inf')] * self._V
        dist[start] = 0
        hq = [(0, start)]
        visited = [False] * self._V
        while hq:
            cost, v = heappop(hq)
            if visited[v]: continue
            visited[v] = True
            for to, w in self._G[v]:
                if dist[to] > cost + w:
                    dist[to] = cost + w
                    heappush(hq, (dist[to], to))
        return dist

n, m, s, t = map(int, input().split())
yen = Dijkstra(n)
snuke = Dijkstra(n)
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1; v -= 1
    yen.add(u, v, a); yen.add(v, u, a)
    snuke.add(u, v, b); snuke.add(v, u, b)

s -= 1; t -= 1
yen_dist = yen.shortest_path(s)
snuke_dist = snuke.shortest_path(t)

answer = []
min_cost = float('inf')
for y, s in zip(reversed(yen_dist), reversed(snuke_dist)):
    min_cost = min(min_cost, y + s)
    answer.append(min_cost)

offset = 10 ** 15
for v in reversed(answer):
    print(offset - v)