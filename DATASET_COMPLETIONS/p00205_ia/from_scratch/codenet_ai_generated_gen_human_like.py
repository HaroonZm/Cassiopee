while True:
    hands = []
    for _ in range(5):
        h = input()
        if h == '0':
            exit()
        hands.append(int(h))
    unique = set(hands)
    if len(unique) == 1 or len(unique) == 3:
        # all same or all three present -> draw for all
        for _ in range(5):
            print(3)
        continue
    # only two unique hands present
    # determine winning hand
    # rules: 1 beats 2, 2 beats 3, 3 beats 1
    if 1 in unique and 2 in unique:
        win = 1
        lose = 2
    elif 2 in unique and 3 in unique:
        win = 2
        lose = 3
    else: # 1 and 3
        win = 3
        lose = 1
    for h in hands:
        if h == win:
            print(1)
        else:
            print(2)