coins = [500,100,50,10,5,1]
while True:
    p = int(input())
    if p == 0:
        break
    change = 1000 - p
    count = 0
    for c in coins:
        count += change // c
        change %= c
    print(count)