import sys
import heapq
from collections import defaultdict
from itertools import permutations, chain

f = sys.stdin

while True:
    m, n, k, d = map(int, f.readline().split())
    if m == 0:
        break
    cake = [0] + list(map(int, f.readline().split()))
    graph = defaultdict(list)
    i = 0
    while i < d:
        a, b, dist = f.readline().split()
        if a == 'H':
            aid = 0
        elif a == 'D':
            aid = m + n + 1
        elif a[0] == 'C':
            aid = int(a[1:])
        else:
            aid = m + int(a[1:])
        if b == 'H':
            bid = 0
        elif b == 'D':
            bid = m + n + 1
        elif b[0] == 'C':
            bid = int(b[1:])
        else:
            bid = m + int(b[1:])
        graph[aid].append((int(dist) * k, bid))
        graph[bid].append((int(dist) * k, aid))
        i += 1
    compressed_graph = []
    size = m + n + 2
    start_i = 0
    while start_i < m + 1:
        distance = [float('inf')] * size
        distance[start_i] = 0
        que = []
        heapq.heappush(que, (0, start_i))
        while len(que):
            _, u = heapq.heappop(que)
            for length, vi in graph[u]:
                if distance[vi] > distance[u] + length:
                    distance[vi] = distance[u] + length
                    if 1 <= vi <= m:
                        continue
                    heapq.heappush(que, (distance[vi], vi))
        compressed_graph.append(distance)
        start_i += 1
    calorie = []
    perm_i = 0
    perm_list = list(chain(*[permutations(range(1, m + 1), i) for i in range(m + 1)]))
    while perm_i < len(perm_list):
        combination = perm_list[perm_i]
        combination = (0,) + combination + (m + n + 1,)
        temp = -sum(cake[i] for i in combination[:-1])
        z = 0
        while z < len(combination) - 1:
            temp += compressed_graph[combination[z]][combination[z + 1]]
            z += 1
        calorie.append(temp)
        perm_i += 1
    print(min(calorie))