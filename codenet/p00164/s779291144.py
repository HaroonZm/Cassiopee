while 1:
    n = int(input())
    if n == 0:
        break
    alist = list(map(int, input().split()))

    ohajiki = 32
    cnt = 0
    while ohajiki != 0:
        taro = (ohajiki - 1) % 5
        ohajiki -= taro
        print(ohajiki)

        jiro = alist[cnt % n]
        ohajiki -= jiro
        if ohajiki < 0:
            ohajiki = 0
        print(ohajiki)
        cnt += 1