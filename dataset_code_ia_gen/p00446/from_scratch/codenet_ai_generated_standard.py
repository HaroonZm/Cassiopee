while True:
    n=int(input())
    if n==0:
        break
    taro=[int(input()) for _ in range(n)]
    all_cards = set(range(1,2*n+1))
    hanako = sorted(all_cards - set(taro))
    taro.sort()
    t = taro.copy()
    h = hanako.copy()
    turn = 0  # 0: taro, 1: hanako
    field = []
    while t and h:
        if turn == 0:
            hand = t
        else:
            hand = h
        if not field:
            # can play any card: play the smallest
            card = hand[0]
            hand.pop(0)
            field = [card]
            turn = 1 - turn
        else:
            last = field[-1]
            # find smallest card > last
            idx = 0
            while idx < len(hand) and hand[idx] <= last:
                idx += 1
            if idx == len(hand):
                # no card to put, pass, clear field
                field = []
                turn = 1 - turn
            else:
                card = hand[idx]
                hand.pop(idx)
                field.append(card)
                turn = 1 - turn
    # game over
    print(len(t))
    print(len(h))