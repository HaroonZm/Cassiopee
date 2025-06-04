from collections import deque
MOD = 10**9 + 7
while 1:
    line = input()
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break
    G = []
    i = 0
    while i < N:
        G.append([])
        i += 1
    i = 0
    while i < M:
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
        i += 1
    used = []
    i = 0
    while i < N:
        used.append(0)
        i += 1
    que = deque()
    r = 0
    k = 0
    i = 0
    while i < N:
        if used[i]:
            i += 1
            continue
        k += 1
        used[i] = 1
        c = 1
        que.append(i)
        while que:
            v = que.popleft()
            for w in G[v]:
                if used[w]:
                    continue
                que.append(w)
                used[w] = 1
                c += 1
        if c > 1:
            r += 1
        i += 1
    if r > 0:
        print((pow(2, k, MOD) + 1) % MOD)
    else:
        print(pow(2, N, MOD))