def solve(X, Y, Z, V, E, A):
    dp = []
    # dp[i][j] means the probability when at position i with score j
    for _ in range(Y + 11):
        dp.append([0.0] * 6001)
    dp[0][0] = 1.0
    for i in range(Y):
        for j in range(5001):
            if dp[i][j] == 0.0:
                continue
            for step in V:
                new_pos = i + step
                if new_pos > Y:
                    dp[Y][j] += dp[i][j] / X
                elif E[new_pos] == 1:
                    # If this is type 1, jump ahead by A[new_pos]
                    next_pos = min(Y, new_pos + A[new_pos])
                    dp[next_pos][j] += dp[i][j] / X
                else:
                    new_score = max(0, j + A[new_pos])
                    dp[new_pos][new_score] += dp[i][j] / X

    total = 0.0
    for score_val in range(5001):
        if dp[Y][score_val] > 0:
            total += score_val * dp[Y][score_val]
    print(int(total))


if __name__ == "__main__":
    import sys
    while True:
        line = input()
        if not line:
            break
        X, Y, Z = map(int, line.split())
        if X == 0 and Y == 0 and Z == 0:
            sys.exit()
        V = list(map(int, input().split()))
        E = [0] * 100  # event types
        A = [0] * 100  # adjustments
        for _ in range(Z):
            n, e, a = map(int, input().split())
            E[n] = e
            if e == 3:
                # Subtract 'a' instead of adding it, special case
                A[n] = -a
            else:
                A[n] = a
        solve(X, Y, Z, V, E, A)