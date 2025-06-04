while True:
    try:
        a = float(input())
        Sum = 0
        retu = 3 * a
        i = 0
        while i < 10:
            if i % 2 == 0:
                retu = retu / 3
            else:
                retu = retu * 2
            Sum += retu
            i += 1
        print(Sum)
    except EOFError:
        break