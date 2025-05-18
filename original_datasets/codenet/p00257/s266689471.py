from collections import deque
while 1:
    M = int(input())
    if M == 0:
        break
    N = int(input())
    D = [0] + [int(input()) for i in range(N)] + [0]
    G = [[] for i in range(N+2)]

    u = [0]*(N+2)
    que = deque([0])
    u[0] = 1
    while que:
        v = que.popleft()
        for j in range(1, M+1):
            if D[min(v+j, N+1)] != 0:
                to = max(min(v+j+D[v+j], N+1), 0)
            else:
                to = min(v+j, N+1)
            if not u[to]:
                que.append(to)
                u[to] = 1
            G[to].append(v)

    z = [0]*(N+2)
    que = deque([N+1])
    z[N+1] = 1
    while que:
        v = que.popleft()
        for w in G[v]:
            if z[w]:
                continue
            z[w] = 1
            que.append(w)
    print("OK" if u == z else "NG")