import sys

while True:
    X, Y, Z = map(int, input().split())
    if X | Y | Z == 0:
        sys.exit()
    V = list(map(int, input().split()))
    E = [0] * 100
    A = [0] * 100
    for _ in range(Z):
        n, e, a = map(int, input().split())
        E[n] = e
        if e == 3:
            A[n] = -a
        else:
            A[n] = a

    dp = [[0.0] * 6001 for _ in range(Y + 11)]
    dp[0][0] = 1.0
    i = 0
    while i < Y:
        j = 0
        while j < 5001:
            if dp[i][j] > 0.0:
                for k in V:
                    t = i + k
                    if t > Y:
                        dp[Y][j] += dp[i][j] / X
                    elif E[t] == 1:
                        tt = min(Y, t + A[t])
                        dp[tt][j] += dp[i][j] / X
                    else:
                        tt = t
                        jj = max(0, j + A[t])
                        dp[tt][jj] += dp[i][j] / X
            j += 1
        i += 1

    s = 0
    i = 0
    while i < 5001:
        if dp[Y][i] > 0.0:
            s += i * dp[Y][i]
        i += 1
    print(int(s))