while True:
    m = int(input())
    if m == 0:
        break

    cards = []
    for _ in range(m):
        a, b = map(int, input().split())
        cards.append((a, b))

    g = int(input())
    targets = [int(input()) for _ in range(g)]

    # maximum sum possible
    max_sum = sum(a * b for a, b in cards)

    # dp[i][j]: number of ways to get sum j using first i types of cards
    # Initialize dp
    dp = [[0] * (max_sum + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(1, m + 1):
        a, b = cards[i - 1]
        for j in range(max_sum + 1):
            if dp[i-1][j] != 0:
                # use k cards of current type where 0 <= k <= b and j + k*a <= max_sum
                for k in range(b + 1):
                    nj = j + k * a
                    if nj <= max_sum:
                        dp[i][nj] += dp[i-1][j]
                    else:
                        break

    for target in targets:
        if target <= max_sum:
            print(dp[m][target])
        else:
            print(0)