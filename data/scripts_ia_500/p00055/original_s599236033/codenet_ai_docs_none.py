while True:
    try:
        a = s = float(input())
        for i in range(2, 11):
            if i % 2 == 0:
                a *= 2.0
                s += a
            else:
                a /= 3.0
                s += a
        print(s)
    except:
        break