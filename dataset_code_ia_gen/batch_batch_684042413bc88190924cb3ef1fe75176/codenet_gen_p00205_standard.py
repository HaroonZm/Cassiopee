while True:
    hands = [int(input()) for _ in range(5)]
    if hands[0] == 0:
        break
    s = set(hands)
    if len(s) == 1 or len(s) == 3:
        for _ in range(5):
            print(3)
        continue
    if 1 not in s:
        win, lose = 2, 3
    elif 2 not in s:
        win, lose = 3, 1
    else:
        win, lose = 1, 2
    for h in hands:
        print(1 if h == win else 2)