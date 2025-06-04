import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    edges = (map(lambda x: int(x)-1, line.split()) for line in sys.stdin)

    graph = [[] for _ in range(N)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * N
    par = [-1] * N
    ord = []
    dq = deque([0])
    visited[0] = True

    while dq:
        x = dq.pop()
        ord.append(x)
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                par[y] = x
                dq.append(y)
    
    from operator import ixor
    from functools import reduce

    G = [0]*(N+1)
    for x in reversed(ord[1:]):
        p = par[x]
        G[p] = ixor(G[p], G[x]+1)

    print('Alice' if G[0] else 'Bob')

if __name__ == "__main__":
    main()