while True:
    total = int(input())
    if total == 0:
        break
    prices = [int(input()) for _ in range(9)]
    print(total - sum(prices))