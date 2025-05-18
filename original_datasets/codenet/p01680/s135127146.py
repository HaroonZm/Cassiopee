from collections import deque
MOD = 10**9 + 7
while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    G = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    que = deque()
    used = [0]*N
    r = 0; k = 0
    for i in range(N):
        if used[i]:
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
    if r > 0:
        print((pow(2, k, MOD) + 1) % MOD)
    else:
        print(pow(2, N, MOD))