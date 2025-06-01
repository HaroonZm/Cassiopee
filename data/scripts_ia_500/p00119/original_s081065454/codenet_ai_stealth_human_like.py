from collections import deque

def solve():
    M = int(input())  # number of nodes
    graph = [[] for _ in range(M)]
    indegree = [0] * M
    N = int(input())  # number of edges

    for _ in range(N):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1

    queue = deque()
    result = []
    # enqueue nodes with zero indegree
    for i in range(M):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node+1)  # back to 1-based indexing for output
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    # printing result - one per line, because problem probably wants that
    print(*result, sep='\n')

solve()