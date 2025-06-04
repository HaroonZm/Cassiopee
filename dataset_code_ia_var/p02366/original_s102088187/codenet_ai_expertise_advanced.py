import sys

sys.setrecursionlimit(1 << 20)

from collections import defaultdict

def main():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        s, t = map(int, input().split())
        graph[s].append(t)
        graph[t].append(s)

    prenum = [None] * V
    parent = [None] * V
    lowest = [None] * V
    visited = [False] * V

    def DFS(u=0, prev=-1):
        stack = [(u, prev, 0, iter(graph[u]))]
        timer = 0
        while stack:
            node, par, state, children = stack[-1]
            if state == 0:
                prenum[node] = lowest[node] = timer
                visited[node] = True
                if par != -1:
                    parent[node] = par
                timer += 1
                stack[-1] = (node, par, 1, children)
            elif state == 1:
                for v in children:
                    if not visited[v]:
                        stack.append((v, node, 0, iter(graph[v])))
                        break
                    elif v != par:
                        lowest[node] = min(lowest[node], prenum[v])
                else:
                    stack[-1] = (node, par, 2, children)
            else:
                for v in graph[node]:
                    if parent[v] == node:
                        lowest[node] = min(lowest[node], lowest[v])
                stack.pop()

    DFS()

    ans = {p for u, p in enumerate(parent[1:], start=1) if prenum[p] <= lowest[u]}
    if parent.count(0) >= 2:
        ans.add(0)
    else:
        ans.discard(0)
    print(*sorted(ans), sep='\n')

if __name__ == '__main__':
    main()