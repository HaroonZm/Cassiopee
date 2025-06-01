def getid(node, m, n):
    if node == 'H':
        return 0
    elif node == 'D':
        return m + n + 1
    elif node[0] == 'C':
        return int(node[1:])
    else:
        return m + int(node[1:])
import heapq
def ex_dijkstra(graph, m, size, start=0):
    distance = [float('inf')] * size
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while len(que):
        _, u = heapq.heappop(que)
        for length, vi in graph[u]:
            if distance[vi] > distance[u] + length:
                distance[vi] = distance[u] + length
                if 1 <= vi <= m:
                    continue
                heapq.heappush(que, (distance[vi], vi))
    return distance
import sys
f = sys.stdin
from collections import defaultdict
from itertools import permutations
from itertools import chain
while True:
    m,n,k,d = map(int, f.readline().split())
    if m == 0:
        break
    cake = [0] + list(map(int, f.readline().split()))
    graph = defaultdict(list)
    for a, b, dist in [f.readline().split() for _ in range(d)]:
        a, b, dist = getid(a,m,n), getid(b,m,n), int(dist) * k
        graph[a].append((dist,b))
        graph[b].append((dist,a))
    compressed_graph = [ex_dijkstra(graph, m, m + n + 2, i) for i in range(m + 1)]
    calorie = []
    for combination in chain(*[permutations(range(1,m + 1), i) for i in range(m + 1)]):
        combination = (0,) + combination + (m + n + 1,)
        temp = -sum(cake[i] for i in combination[:-1])
        for s, e in zip(combination,combination[1:]):
            temp += compressed_graph[s][e]
        calorie.append(temp)
    print(min(calorie))