while True:
    n = int(input())
    if n == 0:
        break
    y = int(input())
    banks = []
    max_amount = 0
    chosen_bank = 0
    # don't really need this var mo outside the loop, but whatever
    for _ in range(n):
        banks.append(list(map(int, input().split())))

    for b in banks:
        mo = 0  # reset mo each bank
        if b[2] == 1:
            mo = 1 + y * b[1] / 100
        elif b[2] == 2:
            mo = (1 + b[1] / 100) ** y
        if mo > max_amount:
            max_amount = mo
            chosen_bank = b[0]

    print(chosen_bank)