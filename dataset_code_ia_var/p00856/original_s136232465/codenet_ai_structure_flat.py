while 1:
    N, T, L, B = map(int, raw_input().split(" "))
    if N == 0 and T == 0 and L == 0 and B == 0:
        break

    dp = []
    for i in range(T+1):
        dp.append([0]*(N+1))

    Lose = set()
    for _ in range(L):
        Lose.add(int(raw_input()))
    Back = set()
    for _ in range(B):
        Back.add(int(raw_input()))

    dp[0][0] = 1

    i = 0
    while i < T:
        j = 0
        while j < N:
            if j in Lose:
                rank = i-1
            else:
                rank = i
            d = 1
            while d <= 6:
                next = j + d
                if next > N:
                    next = N - (next - N)
                if next in Back:
                    dp[i+1][0] += dp[rank][j] / 6.0
                else:
                    dp[i+1][next] += dp[rank][j] / 6.0
                d += 1
            j += 1
        i += 1

    s = 0.0
    i = 1
    while i <= T:
        s += dp[i][N]
        i += 1

    print "%6f" % s