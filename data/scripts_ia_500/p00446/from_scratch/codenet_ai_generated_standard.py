while True:
    n=int(input())
    if n==0:
        break
    taro = [int(input()) for _ in range(n)]
    all_cards = set(range(1,2*n+1))
    hanako = sorted(all_cards - set(taro))
    taro.sort()
    t_idx, h_idx = 0, 0
    t_cards, h_cards = taro, hanako
    t_hand = t_cards[:]
    h_hand = h_cards[:]
    on_table = 0
    t_turn = True
    while t_hand and h_hand:
        hand = t_hand if t_turn else h_hand
        played = False
        for i,c in enumerate(hand):
            if c > on_table:
                on_table = c
                hand.pop(i)
                played = True
                break
        if not played:
            on_table = 0
        t_turn = not t_turn
    print(len(t_hand))
    print(len(h_hand))