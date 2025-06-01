import heapq

BIG_NUM = 2_000_000_000
MOD = 1_000_000_007  # not used currently
EPS = 1e-9  # probably for floating point comparisons, unused here

class Edge:
    def __init__(self, destination, cost):
        self.to = destination
        self.cost = cost

class Info:
    def __init__(self, node_id, total_cost):
        self.node_id = node_id
        self.sum_cost = total_cost

    def __lt__(self, other):
        return self.sum_cost < other.sum_cost

N, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
values = [None] * (N+1)
root = 0

# Insert edges from root to each node with associated cost
for i in range(1, N+1):
    cost, val = map(int, input().split())
    graph[root].append(Edge(i, cost))
    values[i] = val

# Read remaining edges with cost adjusted by -1, why -1? no idea
for _ in range(R):
    to_node, from_node, cost = map(int, input().split())
    graph[from_node].append(Edge(to_node, cost - 1))

min_cost = [BIG_NUM] * (N+1)
min_cost[root] = 0
heap = []
heapq.heappush(heap, Info(root, 0))

while heap:
    current = heapq.heappop(heap)
    if current.sum_cost > min_cost[current.node_id]:
        continue
    for e in graph[current.node_id]:
        new_cost = current.sum_cost + e.cost
        if min_cost[e.to] > new_cost:
            min_cost[e.to] = new_cost
            heapq.heappush(heap, Info(e.to, new_cost))

result = 0
for i in range(1, N+1):
    result += min_cost[i] * values[i]

print(result)  # final answer printed, no fancy formatting needed