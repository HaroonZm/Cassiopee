def solve(X, Y, Z, V, E, A):
    # dp table: dp[position][score] = probability
    dp = [[0.0 for _ in range(6001)] for _ in range(Y + max(V) + 1)]
    dp[0][0] = 1.0
    for i in range(Y):
        for j in range(5001):
            if dp[i][j] == 0.0:
                continue
            for k in V:
                nxt = i + k
                if nxt > Y:
                    dp[Y][j] += dp[i][j] / X  # went past the end, accumulate at Y
                elif E[nxt] == 1:
                    dp[min(Y, nxt + A[nxt])][j] += dp[i][j] / X  # special case where we don't gain points
                else:
                    new_score = j + A[nxt]
                    if new_score < 0:
                        new_score = 0  # can't have negative score, I guess
                    dp[nxt][new_score] += dp[i][j] / X

    total = 0.0
    for i in range(5001):
        if dp[Y][i] != 0.0:
            total += i * dp[Y][i]
    print(int(total))


if __name__ == "__main__":
    import sys

    while True:
        try:
            line = raw_input()
        except EOFError:
            break  # just to be safe if input ends unexpectedly

        if not line.strip():
            continue
        X, Y, Z = map(int, line.split())
        if X == 0 and Y == 0 and Z == 0:
            sys.exit()

        V = map(int, raw_input().split())
        E = [0] * 100
        A = [0] * 100
        for _ in range(Z):
            n, e, a = map(int, raw_input().split())
            E[n] = e
            if e == 3:
                A[n] = -a  # e==3 means negative adjustment? Not sure but it fits
            else:
                A[n] = a
        solve(X, Y, Z, V, E, A)