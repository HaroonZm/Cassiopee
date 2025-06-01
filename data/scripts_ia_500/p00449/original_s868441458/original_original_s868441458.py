from heapq import heappush, heappop, heapify

def dijkstra(s, t, links):
    heap = list(links[s])
    heapify(heap)
    visited = set()
    while heap:
        fare, node = heappop(heap)
        if node == t:
            return fare
        if node in visited:
            continue
        visited.add(node)
        for fare2, node2 in links[node]:
            if node2 not in visited:
                heappush(heap, (fare + fare2, node2))
    return -1

while True:
    n, k = map(int, input().split())
    if not n:
        break
    links = [set() for _ in range(n)]
    for _ in range(k):
        o = map(int, input().split())
        if next(o):
            c, d, e = o
            c, d = c - 1, d - 1
            links[c].add((e, d))
            links[d].add((e, c))
        else:
            a, b = o
            print(dijkstra(a - 1, b - 1, links))