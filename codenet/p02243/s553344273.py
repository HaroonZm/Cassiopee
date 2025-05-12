import heapq

INFINITY = 10 ** 10
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
dict_adjacency = {}

for _ in range(n):
    u, k, *list_num = map(int, input().split())

    list_temp = []

    dict_adjacency[str(u)] = {}

    for i in range(0, k * 2, 2):
        dict_adjacency[str(u)][str(list_num[i])] = list_num[i + 1]

d = [INFINITY] * n

def dijkstra(top_start):
    color = [WHITE] * n

    d[top_start] = 0
    h = []

    heapq.heappush(h, (d[top_start], top_start))

    while len(h) >= 1:
        cost_now, top_now = heapq.heappop(h)

        color[top_now] = BLACK

        if d[top_now] < cost_now:
            continue

        for top_next in dict_adjacency[str(top_now)].keys():
            top_next = int(top_next)
            if color[top_next] == BLACK:
                continue

            cost_next = d[top_now] + dict_adjacency[str(top_now)][str(top_next)]
            if cost_next < d[top_next]:
                d[top_next] = cost_next
                color[top_next] = GRAY
                heapq.heappush(h, (d[top_next], top_next))

dijkstra(top_start = 0)

for i, cost in enumerate(d):
    print(i, cost)