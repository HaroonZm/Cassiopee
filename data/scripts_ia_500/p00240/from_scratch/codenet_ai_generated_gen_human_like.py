while True:
    n = int(input())
    if n == 0:
        break
    y = int(input())
    max_amount = -1
    max_bank = -1
    for _ in range(n):
        b, r, t = map(int, input().split())
        if t == 1:
            amount = 100 * (1 + r/100 * y)
        else:
            amount = 100 * ((1 + r/100) ** y)
        if amount > max_amount:
            max_amount = amount
            max_bank = b
    print(max_bank)