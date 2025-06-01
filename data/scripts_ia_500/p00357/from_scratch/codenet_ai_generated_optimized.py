import sys
sys.setrecursionlimit(10**7)

def can_reach_all(n, d):
    graph_forward = [[] for _ in range(n)]
    graph_backward = [[] for _ in range(n)]
    
    # Build edges using two pointers in O(n)
    j = 0
    for i in range(n):
        # from trampoline i, we can jump to all j where 10*(j - i) <= d[i] and j>i
        while j < n and 10*(j - i) <= d[i]:
            if j > i:
                graph_forward[i].append(j)
                graph_backward[j].append(i)
            j += 1
        if j < n:
            # Move j back for next i since i increases
            if j > i + 1:
                j -= 1

    def bfs(start, graph):
        visited = [False]*n
        from collections import deque
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return visited

    # Check if n-1 reachable from 0 forward
    visited_forward = bfs(0, graph_forward)
    if not visited_forward[n-1]:
        return "no"

    # Check if 0 reachable from n-1 backward
    visited_backward = bfs(n-1, graph_backward)
    if not visited_backward[0]:
        return "no"
    return "yes"


input = sys.stdin.readline
N = int(input())
d = [int(input()) for _ in range(N)]
print(can_reach_all(N, d))