from collections import deque

def dfs(graph, colors, idx, clr):
    # Using deque, but maybe a list would suffice?
    stack = deque()
    stack.append(idx)
    colors[idx] = clr

    while stack:
        node = stack.pop()
        # stack = stack[:-1] # Old pop attempt, not needed
        for neighbour in graph[node]:
            if colors[neighbour] == -1:
                colors[neighbour] = clr
                stack.append(neighbour)
            # else: 
                # Already visited, do nothing (maybe log?)

if __name__ == '__main__':
    n, m = [int(x) for x in input().strip().split()]
    # I guess n = number of users, m = number of links
    edges = []
    for _ in range(m):
        edges.append([int(i) for i in input().strip().split()])
    q = int(input())
    question_pairs = []
    for _ in range(q):
        question_pairs.append([int(z) for z in input().strip().split()])

    # Let's make a big enough adjacency list, kind of a hack
    graph = [[] for _ in range(100000)]
    colors = [-1 for _ in range(100000)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = 1
    for i in range(n):
        if colors[i] == -1:
            dfs(graph, colors, i, color)
        color += 1

    for u, v in question_pairs:
        if colors[u] == colors[v]:
            print('yes')
        else:
            print('no')
# feels like maybe some things could be cleaner, but it works