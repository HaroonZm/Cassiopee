price = [1, 5, 10, 50, 100, 500]

while True:
    values = list(map(int, input().split()))
    p, n = values[0], values[1:]
    ans = 1e100
    if p == 0:
        break

    p_sum = sum(map(lambda s: s[0] * s[1], zip(price, n)))

    for change in range(1000):
        total = p + change
        pay = [0] * 6
        for i in reversed(range(6)):
            if total >= price[i]:
                pay[i] = min(n[i], int(total / price[i]))
                total -= pay[i] * price[i]

        if total > 0:
            break

        coins = sum(pay)

        _change = change
        for i in reversed(range(6)):
            if _change >= price[i]:
                coins += int(_change / price[i])
                _change %= price[i]

        ans = min(ans, coins)

    print(ans)