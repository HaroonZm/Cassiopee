while True:
    hands = [int(input()) for _ in range(5)]
    if hands[0] == 0:
        break
    s = set(hands)
    if len(s) == 1 or len(s) == 3:
        for _ in hands:
            print(3)
        continue
    win_map = {1: 2, 2: 3, 3: 1}
    win_hand = None
    for h in s:
        if win_map[h] in s:
            win_hand = h
            lose_hand = win_map[h]
            break
    for h in hands:
        if h == win_hand:
            print(1)
        elif h == lose_hand:
            print(2)