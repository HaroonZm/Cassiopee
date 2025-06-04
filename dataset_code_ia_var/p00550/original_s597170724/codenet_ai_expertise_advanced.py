from collections import deque
from typing import List, Tuple, Dict

def make_DAG(s: int, n: int, g: List[List[int]]) -> Tuple[List[List[int]], List[int], List[int]]:
    newg = [[] for _ in range(n)]
    dist = [float('inf')] * n
    dist[s] = 0
    dq = deque([s])
    visited = [False] * n
    visited[s] = True
    indeg = [0] * n
    while dq:
        now = dq.popleft()
        for nx in g[now]:
            if dist[nx] >= dist[now] + 1:
                if not visited[nx]:
                    visited[nx] = True
                    dq.append(nx)
                newg[now].append(nx)
                dist[nx] = dist[now] + 1
                indeg[nx] += 1
    return newg, dist, indeg

def bfs_count(s: int, DAG: List[List[int]], indeg: List[int], ok: Dict[Tuple[int, int], bool]) -> int:
    local_indeg = indeg[:]  # ensure isolation for concurrent queries
    dq = deque([s])
    cnt = 0
    while dq:
        now = dq.popleft()
        cnt += 1
        for nx in DAG[now]:
            if (now, nx) in ok:
                continue
            ok[(now, nx)] = True
            local_indeg[nx] -= 1
            if local_indeg[nx] == 0:
                dq.append(nx)
    return cnt

import sys

def main():
    input = sys.stdin.readline
    n, m, q = map(int, input().split())
    e = []
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        e.append((u, v))
    DAG, dist, indeg = make_DAG(0, n, g)
    ans = 0
    ok = dict()
    for _ in range(q):
        r = int(input())
        u, v = e[r - 1]
        if dist[u] == dist[v]:
            print(ans)
            continue
        if dist[u] < dist[v]:
            edge = (u, v)
            if edge not in ok:
                ans += bfs_count(v, DAG, indeg, ok)
        else:
            edge = (v, u)
            if edge not in ok:
                ans += bfs_count(u, DAG, indeg, ok)
        print(ans)

if __name__ == '__main__':
    main()