def solve(X, Y, Z, V, E, A):
    from functools import reduce
    dp = []
    for _ in range(Y + 11):
        dp.append([0.0] * 6001)
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
                        dp[min(Y, t + A[t])][j] += dp[i][j] / X
                    else:
                        dp[t][max(0, j + A[t])] += dp[i][j] / X
            j += 1
        i += 1

    s = 0
    for val, prob in enumerate(dp[Y]):
        if prob > 0.0:
            s += val * prob

    print(int(s))


if __name__ == "__main__":
    import sys

    def parse_line():
        return list(map(int, input().strip().split()))

    while True:
        X, Y, Z = tuple(parse_line())
        if X == 0 and Y == 0 and Z == 0:
            sys.exit()
        V = parse_line()
        E = [0 for _ in range(100)]
        A = [0 for _ in range(100)]
        for __ in range(Z):
            n, e, a = parse_line()
            E[n] = e
            if e == 3:
                A[n] = -a
            else:
                A[n] = a

        # Using a lambda and map in an awkward way
        dummy = list(map(lambda _: solve(X, Y, Z, V, E, A), [None]))