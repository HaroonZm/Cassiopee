import sys
from collections import deque

def strongly_connected_components(N, G, RG):
    order = []
    visited = [False] * N
    group = [None] * N

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)

    def reverse_dfs(u, label):
        group[u] = label
        visited[u] = True
        for v in RG[u]:
            if not visited[v]:
                reverse_dfs(v, label)

    for i in range(N):
        if not visited[i]:
            dfs(i)

    visited = [False] * N
    label = 0
    for u in reversed(order):
        if not visited[u]:
            reverse_dfs(u, label)
            label += 1
    return label, group

def build_new_graph(N, G, label, group):
    new_G = [set() for _ in range(label)]
    new_RG = [set() for _ in range(label)]
    nodes_in_group = [[] for _ in range(label)]
    for v in range(N):
        v_group = group[v]
        nodes_in_group[v_group].append(v)
        for w in G[v]:
            w_group = group[w]
            if v_group != w_group:
                new_G[v_group].add(w_group)
                new_RG[w_group].add(v_group)
    return new_G, new_RG, nodes_in_group

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M, T = map(int, readline().split())
    if N == 0 and M == 0 and T == 0:
        return False
    V = [0] * N
    W = [0] * N
    C = [0] * N
    for i in range(N):
        vals = list(map(int, readline().split()))
        V[i], W[i], C[i] = vals
    G = [[] for _ in range(N)]
    RG = [[] for _ in range(N)]
    single_loop = [0] * N
    for i in range(M):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        if a == b:
            single_loop[a] = 1
        else:
            G[a].append(b)
            RG[b].append(a)

    label, group = strongly_connected_components(N, G, RG)
    new_G, new_RG, nodes_in_group = build_new_graph(N, G, label, group)
    INF = 10 ** 18
    dp = [None] * label
    initial_dp = [0] + [-INF] * T

    deg = [0] * label
    queue = deque()
    for i in range(label):
        deg[i] = len(new_RG[i])
        if deg[i] == 0:
            queue.append(i)
            dp[i] = initial_dp[:]

    answer = 0
    while queue:
        v = queue.popleft()
        dp_v = dp[v]

        if len(nodes_in_group[v]) == 1 and single_loop[nodes_in_group[v][0]] == 0:
            e = nodes_in_group[v][0]
            value = V[e]
            weight = W[e]
            for i in range(T, weight - 1, -1):
                if dp_v[i] < dp_v[i - weight] + value:
                    dp_v[i] = dp_v[i - weight] + value
        else:
            for e in nodes_in_group[v]:
                value = V[e]
                weight = W[e]
                count = C[e]
                if weight > T:
                    continue
                if count == 1:
                    for i in range(T, weight - 1, -1):
                        if dp_v[i] < dp_v[i - weight] + value:
                            dp_v[i] = dp_v[i - weight] + value
                elif weight * count >= T:
                    for i in range(weight, T + 1):
                        if dp_v[i] < dp_v[i - weight] + value:
                            dp_v[i] = dp_v[i - weight] + value
                else:
                    for k in range(weight):
                        q = deque()
                        for j in range((T - k) // weight + 1):
                            pos = k + j * weight
                            s = dp_v[pos] - j * value
                            while q and q[-1][1] <= s:
                                q.pop()
                            q.append((j, s))
                            dp_pos = q[0][1] + j * value
                            if dp_v[pos] < dp_pos:
                                dp_v[pos] = dp_pos
                            if q[0][0] == j - count:
                                q.popleft()

        max_v = max(dp_v)
        if answer < max_v:
            answer = max_v

        for nv in new_G[v]:
            deg[nv] -= 1
            if dp[nv] is None:
                dp[nv] = dp_v[:]
            else:
                for i in range(T+1):
                    if dp[nv][i] < dp_v[i]:
                        dp[nv][i] = dp_v[i]
            if deg[nv] == 0:
                queue.append(nv)
    write(str(answer) + '\n')
    return True

while solve():
    pass