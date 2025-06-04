while True:
    w = int(input())
    if w == -1:
        break
    base = 1150
    charge = base
    if w <= 10:
        pass
    elif w <= 20:
        charge += (w -10) * 125
    elif w <= 30:
        charge += 10 * 125
        charge += (w -20) * 140
    else:
        charge += 10 * 125
        charge += 10 * 140
        charge += (w -30) * 160
    diff = 4280 - charge
    print(diff)