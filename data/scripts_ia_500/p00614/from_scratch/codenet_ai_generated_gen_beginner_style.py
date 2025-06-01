while True:
    data = input().split()
    if not data:
        break
    P = int(data[0])
    if P == 0:
        break
    coins = [int(x) for x in data[1:]]
    values = [1,5,10,50,100,500]

    # Generate all possible ways to pay with the given coins, brute force
    # Because max coins per type up to 1000, we can't try all combinations directly
    # So try from paying amount P to sum of all coins value

    max_pay = 0
    for i in range(6):
        max_pay += coins[i]*values[i]

    min_total = 10**9

    # We'll try all possible payment amounts from P to max_pay
    # For each amount, try to find if we can pay it with available coins
    # and calculate number of coins paid plus number of coins in change.

    # For finding payment, use a simple approach:
    # For each coin type start from largest to smallest,
    # use as many coins as possible without exceeding amount or coins available.

    # For change, the clerk returns change with least number of coins:
    # We can use greedy approach (largest coin to smallest coin).

    # Because max_pay can be large, we try all from P to max_pay,
    # but if max_pay is too large, it may be slow.
    # But problem says max of 100 data sets; coins up to 1000 each, so brute force is acceptable.

    for pay_amount in range(P, max_pay+1):
        remain = pay_amount
        used_coins = [0]*6
        for i in range(5,-1,-1):
            use = min(remain//values[i], coins[i])
            used_coins[i] = use
            remain -= use*values[i]
        if remain != 0:
            continue  # cannot pay this amount with available coins

        # calculate change
        change = pay_amount - P
        change_coins = 0
        for i in range(5,-1,-1):
            c = change // values[i]
            change_coins += c
            change -= c*values[i]

        paid_coins = sum(used_coins)
        total = paid_coins + change_coins
        if total < min_total:
            min_total = total

    print(min_total)