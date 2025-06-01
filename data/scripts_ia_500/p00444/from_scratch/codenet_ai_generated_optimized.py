coins = [500, 100, 50, 10, 5, 1]
while True:
    n = int(input())
    if n == 0:
        break
    change = 1000 - n
    count = 0
    for c in coins:
        count += change // c
        change %= c
    print(count)