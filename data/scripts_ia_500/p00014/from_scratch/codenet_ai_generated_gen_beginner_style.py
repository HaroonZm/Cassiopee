while True:
    try:
        d = int(input())
        s = 0
        for i in range(1, 600 // d + 1):
            x = i * d
            s += x * x * d
        print(s)
    except:
        break