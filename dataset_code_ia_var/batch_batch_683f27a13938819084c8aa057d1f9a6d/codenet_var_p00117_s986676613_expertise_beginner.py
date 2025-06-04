import heapq

def dijkstra(n, graph, start, goal):
    INF = 2147483647
    dist = [INF] * n
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            break
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            total_cost = cost + next_cost
            if dist[next_node] > total_cost:
                dist[next_node] = total_cost
                heapq.heappush(queue, (total_cost, next_node))
    return dist[goal]

n = int(input()) + 1
graph = []
for i in range(n):
    graph.append([])

m = int(input())
for i in range(m):
    line = input()
    a, b, c, d = map(int, line.split(','))
    graph[a].append((b, c))
    graph[b].append((a, d))

line2 = input()
s, g, V, P = map(int, line2.split(','))

if s == g:
    print(V - P)
else:
    cost1 = dijkstra(n, graph, s, g)
    cost2 = dijkstra(n, graph, g, s)
    print(V - P - cost1 - cost2)