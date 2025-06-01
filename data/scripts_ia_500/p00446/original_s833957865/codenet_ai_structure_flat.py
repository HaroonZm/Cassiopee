while True:
    n = input()
    if n == 0:
        break
    card1 = []
    for _ in range(n):
        card1.append(input())
    card1.sort()
    card2 = []
    for i in range(1, 2 * n + 1):
        if i not in card1:
            card2.append(i)
    ba = 0
    turn = 1
    while len(card1) > 0 and len(card2) > 0:
        if turn == 1:
            card = card1
        else:
            card = card2
        found = False
        i = 0
        while i < len(card):
            if card[i] > ba:
                ba = card.pop(i)
                found = True
                break
            i += 1
        if not found:
            ba = 0
        if turn == 1:
            turn = 0
        else:
            turn = 1
    print len(card2)
    print len(card1)