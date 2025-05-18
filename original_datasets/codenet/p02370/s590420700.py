from collections import deque

class Graph(): #directed
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append(e[1] - indexed)
            self.rev[e[1] - indexed].append(e[0] - indexed)
            self.deg[e[1] - indexed] += 1

    def topological_sort(self):
        deg = self.deg[:]
        res = [i for i in range(self.n) if deg[i] == 0]
        queue = deque(res)
        used = [False for _ in range(self.n)]
        while queue:
            node = queue.popleft()
            for adj in self.graph[node]:
                deg[adj] -= 1
                if deg[adj] == 0:
                    queue.append(adj)
                    res.append(adj)
        return res

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

g = Graph(N, E, 0)
print('\n'.join(map(str, g.topological_sort())))