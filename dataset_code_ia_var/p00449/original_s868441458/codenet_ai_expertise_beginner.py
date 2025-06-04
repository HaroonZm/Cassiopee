import heapq

def dijkstra(start, end, links):
    # Initialisation du tas (file de priorité)
    heap = []
    for cost, neighbor in links[start]:
        heapq.heappush(heap, (cost, neighbor))
    visited = set()
    while heap:
        cur_cost, node = heapq.heappop(heap)
        if node == end:
            return cur_cost
        if node in visited:
            continue
        visited.add(node)
        for next_cost, next_node in links[node]:
            if next_node not in visited:
                heapq.heappush(heap, (cur_cost + next_cost, next_node))
    return -1

while True:
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    if n == 0:
        break
    links = []
    for i in range(n):
        links.append(set())
    for _ in range(k):
        values = list(map(int, input().split()))
        if len(values) == 3:
            c = values[0] - 1
            d = values[1] - 1
            e = values[2]
            links[c].add((e, d))
            links[d].add((e, c))
        else:
            a = values[0] - 1
            b = values[1] - 1
            result = dijkstra(a, b, links)
            print(result)