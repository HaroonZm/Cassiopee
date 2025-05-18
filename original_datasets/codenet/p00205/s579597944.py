while 1:
    hands = []
    h = int(input())
    if h == 0:
        break
    hands.append(h)

    for _ in range(4):
        h = int(input())
        hands.append(h)

    h_uni = list(set(hands))
    if len(h_uni) != 2:
        for _ in range(5):
            print(3)
        continue

    h_uni.sort()
    if h_uni[0] == 1 and h_uni[1] == 2:
        for h in hands:
            if h == 1:
                print(1)
            else:
                print(2)
    elif h_uni[0] == 1 and h_uni[1] == 3:
        for h in hands:
            if h == 1:
                print(2)
            else:
                print(1)
    else:
        for h in hands:
            if h == 2:
                print(1)
            else:
                print(2)