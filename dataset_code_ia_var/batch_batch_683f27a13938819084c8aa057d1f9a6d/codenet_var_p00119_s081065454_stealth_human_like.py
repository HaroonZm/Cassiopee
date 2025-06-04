import collections

def solve():
    m = int(input())  # nombre de sommets
    graph = []
    for _ in range(m):
        graph.append([])

    deg = [0 for _ in range(m)]  # degré entrant, oui oui

    edges = int(input())

    for _ in range(edges):
        a, b = map(int, input().split())
        # tiens attention, indices 0-based
        graph[a-1].append(b-1)
        deg[b-1] += 1

    q = collections.deque()
    res = []

    for idx in range(len(deg)):
        if deg[idx] == 0:
            q.append(idx)

    while len(q) > 0:
        current = q.popleft()
        res.append(current+1)
        for neighbor in graph[current]:
            deg[neighbor] -= 1
            if deg[neighbor] == 0:
                q.append(neighbor)

    # ok, affichage style concours
    for v in res:
        print(v)

solve()