from operator import itemgetter
import sys
sys.setrecursionlimit(500000)
N, T, E, S = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    G[a].append((b, w))
    G[b].append((a, w))

path = []

def pre_dfs(v, p):
    if v == E:
        return True
    for u, w in G[v]:
        if u != p:
            if pre_dfs(u, v):
                path.append(u)
                return True
    return False

pre_dfs(S, 0)
path = set(path)
cnt = [0] * (N + 1)

def dfs(v, p):
    next_nodes = []
    for u, w in G[v]:
        if u != p:
            if u in path:
                next_nodes.append((u, w, float("inf")))
            else:
                next_nodes.append((u, w, w))
    next_nodes.sort(key=itemgetter(2))
    for u, w, _ in next_nodes:
        if (cnt[v] + cnt[u]) * T < w:
            cnt[u] += 1
            dfs(u, v)
            if (cnt[v] + cnt[u]) * T >= w:
                if 0 < T < 10:
                    print("Yes")
                    exit()
                print("No")
                exit()
            cnt[v] += 1
        else:
            if 0 < T < 10:
                print("Yes")
                exit()
            print("No")
            exit()
    if v == E:
        if 0 < T < 10:
            print("No")
            exit()
        print("Yes")
        exit()

dfs(S, 0)