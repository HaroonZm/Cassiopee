while 42:
    try:
        z = int(input())
        if not z:
            break
        k = [input() for _ in range(z//4)]
        T = 0
        x = 0
        while x < len(k):
            T = T + int(k[x])
            x += 1
        print(T)
    except:
        pass