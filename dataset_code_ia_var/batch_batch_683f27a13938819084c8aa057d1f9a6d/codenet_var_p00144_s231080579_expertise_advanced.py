from collections import defaultdict, deque
import sys

def input():
    return sys.stdin.readline()

n = int(input())
router = defaultdict(list)
for _ in range(n):
    r, k, *neighbors = map(int, input().split())
    router[r] = neighbors

def transport(s, g):
    if s == g:
        return 1
    visited = [False] * (n + 2)
    queue = deque([(s, 0)])
    visited[s] = True
    while queue:
        node, dist = queue.popleft()
        for neighbor in router[node]:
            if not visited[neighbor]:
                if neighbor == g:
                    return dist + 2
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    return float('inf')

p = int(input())
for _ in range(p):
    s, d, v = map(int, input().split())
    steps = transport(s, d)
    print(steps if steps <= v else "NA")