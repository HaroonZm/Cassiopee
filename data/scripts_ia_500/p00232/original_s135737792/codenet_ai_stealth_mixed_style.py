def solve(X, Y, Z, V, E, A):
    from functools import reduce
    dp = [[0.0 for _ in range(6001)] for _ in range(Y + 11)]
    dp[0][0] = 1.0
    i = 0
    while i < Y:
        for j in range(5001):
            val = dp[i][j]
            if val <= 0:
                continue
            for k in V:
                t = i + k
                if t > Y:
                    dp[Y][j] += val / X
                elif E[t] == 1:
                    idx = min(Y, t + A[t])
                    dp[idx][j] += val / X
                else:
                    dp[t][max(0, j + A[t])] += val / X
        i += 1
    s = sum(x * p for x, p in enumerate(dp[Y][:5001]))
    print(int(s))

if __name__ == "__main__":
    import sys
    def readints():
        return list(map(int, input().split()))
    while True:
        try:
            X, Y, Z = readints()
        except EOFError:
            break
        if (X | Y | Z) == 0:
            sys.exit()
        V = [*map(int, input().split())]
        E = [0]*100
        A = [0]*100
        for _ in range(Z):
            n, e, a = map(int, input().split())
            E[n] = e
            if e == 3:
                A[n] = -a
            else:
                A[n] = a
        solve(X, Y, Z, V, E, A)