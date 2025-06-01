while True:
    m = int(input())
    if m == 0:
        break
    cards = []
    max_sum = 0
    for _ in range(m):
        a, b = map(int, input().split())
        cards.append((a, b))
        max_sum += a * b
    g = int(input())
    targets = [int(input()) for _ in range(g)]
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for a, b in cards:
        count = b
        for s in range(max_sum, -1, -1):
            if dp[s]:
                for k in range(1, count + 1):
                    ns = s + a * k
                    if ns > max_sum:
                        break
                    dp[ns] += dp[s]
    for n in targets:
        print(dp[n] if n <= max_sum else 0)