while True:
    try:
        d = int(input())
        s = 0
        n = 600 // d
        for i in range(1, n + 1):
            height = (i * d) ** 2
            area = height * d
            s += area
        print(s)
    except:
        break