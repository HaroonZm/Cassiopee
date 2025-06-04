while True:
    data = input().split()
    if not data:
        break
    P = int(data[0])
    if P == 0:
        break
    coins_num = list(map(int, data[1:7]))
    coin_values = [1,5,10,50,100,500]

    # Precompute the minimal number of coins needed to make change for any amount up to max change
    max_amount = 10000  # As max total coins * max coin value can be large, but problem constraints allow
    INF = 10**9

    # Compute total money he has
    total_money = sum(c*v for c,v in zip(coins_num,coin_values))
    change_max = total_money - P

    # Prepare minimal coins for change (greedy works since coins are canonical)
    # So for change, minimal number of coins returned = greedy algorithm
    def min_coins_change(x):
        remain = x
        cnt = 0
        for v in reversed(coin_values):
            cnt += remain//v
            remain %= v
        return cnt

    # To find minimal total coins (paid + change)
    # Paid coins must sum atleast P (pay amount >=P)
    # Paid coins chosen from limited number of coins

    # We'll do subset sum DP with limited coins (bounded knapsack):
    # dp[i] = minimal number of coins used to form sum i, or INF if impossible
    dp = [INF]*(total_money+1)
    dp[0] = 0
    for c,v in zip(coins_num, coin_values):
        if c == 0:
            continue
        # Use bounded knapsack optimization - binary representation
        k = 1
        while c > 0:
            use = min(k,c)
            c -= use
            val = use * v
            for i in range(total_money - val, -1, -1):
                if dp[i] != INF and dp[i] + use < dp[i+val]:
                    dp[i+val] = dp[i] + use
            k <<= 1

    res = INF
    # Try all sums >= P, compute total coins = paid + change coins
    for paid in range(P, total_money+1):
        if dp[paid] == INF:
            continue
        change = paid - P
        ccoins = min_coins_change(change)
        total_coins = dp[paid] + ccoins
        if total_coins < res:
            res = total_coins

    print(res)