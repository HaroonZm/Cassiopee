while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    prices = list(map(int, input().split()))
    prices.sort(reverse=True)
    total = 0
    for i, price in enumerate(prices):
        if (i + 1) % m != 0:
            total += price
    print(total)