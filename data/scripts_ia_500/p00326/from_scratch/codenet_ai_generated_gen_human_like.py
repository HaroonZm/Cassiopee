import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

D = int(input())
indegree = [0] * N
graph = [[] for _ in range(N)]
for _ in range(D):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    indegree[b] += 1

initial_order = list(map(int, input().split()))
R = int(input())
changes = []
for _ in range(R):
    tmp = list(map(int, input().split()))
    m_i = tmp[0]
    e_i = tmp[1:]
    changes.append((m_i, e_i))

changes_index = 0

# Current evaluation order: map from attribute index (starting from 0) to priority order
# We will use this order to sort tasks: we want to compare tasks by the attributes in order,
# but for the heap (min-heap) we need to transform the values so that the "largest" attribute becomes the smallest key
# since heapq is min-heap, we will invert the attribute values by negation.

# To quickly get the sorted key for each task, define a function to generate the sort key tuple
def make_key(task_attr, order):
    # order has K elements, each 1-based index of attribute
    # For sorting descending by attribute value, use negative values
    return tuple(-task_attr[o-1] for o in order)

# Initialize priority queue with tasks that have indegree 0
pq = []
for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(pq, (make_key(tasks[i], initial_order), i))

executed_count = 0
evaluation_order = initial_order
result = []

while pq:
    key, t = heapq.heappop(pq)
    result.append(t+1)
    executed_count += 1

    # Check if we need to update evaluation order
    while changes_index < R and changes[changes_index][0] == executed_count:
        evaluation_order = changes[changes_index][1]
        changes_index += 1
        # After changing evaluation order, keys in the queue are outdated,
        # we need to rebuild the priority queue with the new keys.
        # Extract all tasks from pq, recompute keys, re-heapify.
        tmp = []
        while pq:
            _, x = heapq.heappop(pq)
            heapq.heappush(tmp, (make_key(tasks[x], evaluation_order), x))
        pq = tmp

    for nxt in graph[t]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(pq, (make_key(tasks[nxt], evaluation_order), nxt))

print('\n'.join(map(str, result)))