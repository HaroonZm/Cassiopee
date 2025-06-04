while True:
    try:
        rawhand = input().split(",")
        hand = [0]*14
        for card in rawhand:
            if card == "A":
                hand[1] += 1
            elif card == "J":
                hand[11] += 1
            elif card == "Q":
                hand[12] += 1
            elif card == "K":
                hand[13] += 1
            else:
                hand[int(card)] += 1
        pairs = 0
        three = False
        four = False
        minone = 0
        i = 0
        while i < 14:
            ranks = hand[i]
            if ranks == 1 and minone == 0:
                minone = i
            elif ranks == 2:
                pairs += 1
            elif ranks == 3:
                three = True
            elif ranks == 4:
                four = True
                break
            i += 1
        straight = False
        if minone and minone <= 10:
            if hand[minone] == 1 and hand[minone+1] == 1 and hand[minone+2] == 1 and hand[minone+3] == 1 and hand[minone+4] == 1:
                straight = True
        if hand[1] == 1 and hand[10] == 1 and hand[11] == 1 and hand[12] == 1 and hand[13] == 1:
            straight = True
        if four:
            print("four card")
        elif three and pairs == 1:
            print("full house")
        elif straight:
            print("straight")
        elif three:
            print("three card")
        elif pairs == 2:
            print("two pair")
        elif pairs == 1:
            print("one pair")
        else:
            print("null")
    except EOFError:
        break