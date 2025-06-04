while True:
    n, m, k = map(int, raw_input().split())
    if n == 0 and m == 0 and k == 0:
        break
    max_sum = m * n
    dice = []
    for i in range(n):
        dice.append([0] * (max_sum))
    for i in range(m):
        dice[0][i] = 1
    for i in range(n-1):
        for j in range(max_sum):
            if dice[i][j] == 0:
                continue
            for l in range(1, m+1):
                if j + l < max_sum:
                    dice[i+1][j+l] += dice[i][j]
    total = 0
    for i in range(n-1, max_sum):
        val = i + 1 - k
        if val > 1:
            total += val * dice[n-1][i]
        else:
            total += 1 * dice[n-1][i]
    all_poss = m ** n * 1.0
    print total / all_poss