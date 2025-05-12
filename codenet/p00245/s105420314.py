from heapq import heappush, heappop
from string import digits
import sys
readline = sys.stdin.readline
write = sys.stdout.write
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

INF = 10**9
while 1:
    X, Y = map(int, readline().split())
    if X == Y == 0:
        break
    MP = [readline().split() for i in range(Y)]
    N = int(readline())
    I = [[] for i in range(10)]
    for i in range(N):
        g, d, s, e = map(int, readline().split())
        if s < e:
            I[g].append((i, d, s, e))
    for ss in I:
        ss.sort(key=lambda x: x[1])
    V = [0]*(1 << N)
    for state in range(1 << N):
        v = 0
        for ss in I:
            x = 0
            for i, d, s, e in ss:
                if state & (1 << i):
                    x = d
            v += x
        V[state] = v

    U = [[None]*X for i in range(Y)]
    sx = sy = 0
    for i in range(Y):
        for j in range(X):
            c = MP[i][j]
            if c in digits:
                continue
            if c == 'P':
                sy = i; sx = j
            s = set()
            for dx, dy in dd:
                nx = j + dx; ny = i + dy
                if not 0 <= nx < X or not 0 <= ny < Y:
                    continue
                c = MP[ny][nx]
                if c in digits:
                    for e in I[int(c)]:
                        s.add(e)
            U[i][j] = s

    D = [[[INF]*(1 << N) for i in range(X)] for j in range(Y)]
    que = [(0, 0, sx, sy)]
    D[sy][sx][0] = 0
    while que:
        cost, state, x, y = heappop(que)
        D0 = D[y][x]
        t = D0[state]
        if t < cost:
            continue
        for i, d, s, e in U[y][x]:
            if t < e and state & (1 << i) == 0:
                t0 = max(s, t)
                n_state = state | (1 << i)
                if t0 < D0[n_state]:
                    D0[n_state] = t0
                    heappush(que, (t0, n_state, x, y))
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if not 0 <= nx < X or not 0 <= ny < Y or U[ny][nx] is None:
                continue
            if t+1 < D[ny][nx][state]:
                D[ny][nx][state] = t+1
                heappush(que, (t+1, state, nx, ny))
    ans = 0
    for x in range(X):
        for y in range(Y):
            D0 = D[y][x]
            for state in range(1 << N):
                if D0[state] < INF:
                    ans = max(ans, V[state])
    write("%d\n" % ans)