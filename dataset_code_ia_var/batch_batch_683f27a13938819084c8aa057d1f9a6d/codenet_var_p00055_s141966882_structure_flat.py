while True:
    try:
        a = float(input())
    except:
        break
    total = a
    i = 2
    while i < 11:
        if i % 2:
            tmp = (a / 3)
        else:
            tmp = (a * 2)
        total += tmp
        a = tmp
        i += 1
    print(total)