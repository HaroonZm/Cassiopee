while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    ohajiki = 32
    idx = 0
    while ohajiki > 0:
        # 一郎君の番
        take_ichiro = (ohajiki - 1) % 5
        if take_ichiro == 0:
            take_ichiro = 1
        ohajiki -= take_ichiro
        print(ohajiki)
        if ohajiki == 0:
            break
        # 次郎君の番
        take_jirou = a[idx]
        if take_jirou > ohajiki:
            take_jirou = ohajiki
        ohajiki -= take_jirou
        print(ohajiki)
        idx = (idx + 1) % n