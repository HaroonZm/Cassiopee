coins = list(map(int, input().split()))
values = [1, 5, 10, 50, 100, 500]

total = sum(c * v for c, v in zip(coins, values))

if total >= 1000:
    print(1)
else:
    print(0)