import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
m = int(input())

# edges: i -> j means team i beat team j
graph = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)

for _ in range(m):
    i_, j_ = map(int, input().split())
    graph[i_].append(j_)
    in_degree[j_] += 1

from collections import deque

def topological_sort_check_unique():
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    res = []
    unique = True
    while q:
        if len(q) > 1:
            unique = False  # more than one candidate means multiple orders possible
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(res) < n:
        # cycle detected, no valid order
        return [], False

    return res, unique

order, unique = topological_sort_check_unique()

for team in order:
    print(team)
print(0 if unique else 1)