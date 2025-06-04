import sys
from collections import deque

def main():
    while True:
        N, M = map(int, sys.stdin.readline().split())
        if N == 0 and M == 0:
            break

        edges = []
        degrees = [0 for _ in range(N)]
        adj = [[] for _ in range(N)]

        for _ in range(M):
            u, v = map(int, sys.stdin.readline().split())
            # Each edge will be a list with: [to, direction, reverse_edge]
            edge1 = [v-1, 1, None] # u -> v
            edge2 = [u-1, 0, edge1] # v -> u (reverse), initially direction=0 (i.e., backward)
            edge1[2] = edge2
            adj[u-1].append(edge1)
            adj[v-1].append(edge2)
            degrees[v-1] += 1

        prev = [0 for _ in range(N)]

        while True:
            used = [0 for _ in range(N)]
            que = deque()
            mini = min(degrees)
            maxi = max(degrees)
            for i in range(N):
                if degrees[i] == mini:
                    que.append(i)
                    used[i] = 1
                    prev[i] = None
            found = -1
            while que:
                v = que.popleft()
                if degrees[v] >= mini + 2:
                    found = v
                    break
                for edge in adj[v]:
                    w = edge[0]
                    d = edge[1]
                    rev = edge[2]
                    if d == 1 and not used[w]:
                        que.append(w)
                        prev[w] = rev
                        used[w] = 1
            if found == -1:
                break
            v = found
            while prev[v] is not None:
                edge = prev[v]
                edge[1] = 1
                edge[2][1] = 0
                v = edge[0]
            degrees[v] += 1
            degrees[found] -= 1

        while True:
            used = [0 for _ in range(N)]
            que = deque()
            mini = min(degrees)
            maxi = max(degrees)
            for i in range(N):
                if degrees[i] == maxi:
                    que.append(i)
                    used[i] = 1
                    prev[i] = None
            found = -1
            while que:
                v = que.popleft()
                if degrees[v] <= maxi - 2:
                    found = v
                    break
                for edge in adj[v]:
                    w = edge[0]
                    d = edge[1]
                    rev = edge[2]
                    if d == 0 and not used[w]:
                        que.append(w)
                        prev[w] = rev
                        used[w] = 1
            if found == -1:
                break
            v = found
            while prev[v] is not None:
                edge = prev[v]
                edge[1] = 0
                edge[2][1] = 1
                v = edge[0]
            degrees[v] -= 1
            degrees[found] += 1

        print(str(min(degrees)) + " " + str(max(degrees)))

main()