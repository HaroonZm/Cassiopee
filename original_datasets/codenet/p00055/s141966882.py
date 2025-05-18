while True:
    try:
        a = float(input())
    except:
        break
    total = a
    for i in range(2, 11):
        tmp = (a / 3) * (i % 2) + (a * 2) * (i % 2 == 0)
        total += tmp
        a = tmp
    print(total)