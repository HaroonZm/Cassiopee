def solve(X, Y, Z, V, E, A):
    from collections import defaultdict
    dp = defaultdict(lambda: defaultdict(float))
    dp[0][0] = 1.0
    for i in range(Y):
        for j in list(dp[i].keys()):
            if dp[i][j] <= 0.0:
                continue
            p = dp[i][j] / X
            for k in V:
                t = i + k
                if t > Y:
                    dp[Y][j] += p
                elif E[t] == 1:
                    nxt = t + A[t]
                    if nxt > Y:
                        nxt = Y
                    dp[nxt][j] += p
                else:
                    dp[t][max(0, j + A[t])] += p
    total = 0
    for score, prob in dp[Y].items():
        if prob > 0:
            total += score * prob
    print(int(total))


if __name__ == "__main__":
    import sys
    inputfunc = sys.stdin.readline

    def readints():
        return list(map(int, inputfunc().split()))

    while True:
        try:
            X, Y, Z = map(int, inputfunc().split())
            if X == 0 and Y == 0 and Z == 0:
                break
            V = list(map(int, inputfunc().split()))
            E = [0 for _ in range(101)]
            A = [0 for _ in range(101)]
            for _ in range(Z):
                n, e, a = [int(x) for x in inputfunc().strip().split()]
                E[n] = e
                A[n] = -a if e == 3 else a
            solve(X, Y, Z, V, E, A)
        except Exception:
            break