from collections import deque
while 1:
    N = int(input())
    if N == 0:
        break

    T = [0]*N; C = [0]*N
    que0 = deque()
    que1 = deque()
    P = [list(map(int, input().split())) for i in range(N)]
    P.sort()
    for i in range(N):
        t, c = P[i]
        que0.append((i, t))
        T[i] = t
        C[i] = c

    INF = 10**18
    ans = 0
    rest = N
    while rest:
        t = min(que0[0][1] if que0 else INF, que1[0][1] if que1 else INF)
        st0 = []; st1 = []
        while que0 and que0[0][1] <= t:
            st0.append(que0.popleft()[0])
        st0.sort()
        for i in st0:
            que1.append((i, t+T[i]))
        while que1 and que1[0][1] <= t:
            st1.append(que1.popleft()[0])
        st1.sort()
        for i in st1:
            if C[i] == 1:
                rest -= 1
            else:
                que0.append((i, t+T[i]))
            C[i] -= 1
        ans = max(ans, t)
    print(ans)