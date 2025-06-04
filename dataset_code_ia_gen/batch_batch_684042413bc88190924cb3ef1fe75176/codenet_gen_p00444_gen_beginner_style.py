while True:
    n = int(input())
    if n == 0:
        break
    change = 1000 - n
    coins = 0
    coins += change // 500
    change = change % 500
    coins += change // 100
    change = change % 100
    coins += change // 50
    change = change % 50
    coins += change // 10
    change = change % 10
    coins += change // 5
    change = change % 5
    coins += change
    print(coins)