while True:
    a = int(input())
    if a == 0:
        break
    a = 1000 - a
    c = 0
    coins = [500, 100, 50, 10, 5, 1]
    for coin in coins:
        c += a // coin
        a = a % coin
    print(c)