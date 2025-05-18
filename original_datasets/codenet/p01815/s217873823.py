import sys
sys.setrecursionlimit(10**6)
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    *W, = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    U = [0]*N
    L = [0]*N
    D = [0]*N
    R = [0]*N

    U[0] = 1
    stk = [0]
    it = [0]*N
    while stk:
        v = stk[-1]
        p = stk[-2] if len(stk) > 1 else -1
        if it[v] == 0:
            U[v] = 1
        else:
            w = G[v][it[v]-1]
            D[v] = max(D[v], D[w])
            if L[w]:
                L[v] = 1

        while it[v] < len(G[v]):
            w = G[v][it[v]]; it[v] += 1
            if U[w]:
                if w != p:
                    L[v] = 1
                continue
            U[w] = 1
            stk.append(w)
            break
        else:
            D[v] = D[v] + W[v]
            stk.pop()

    ans = su = 0
    for i in range(N):
        if L[i]:
            ans += W[i]
        else:
            su = max(su, D[i])
    write("%d\n" % (ans + su))
solve()