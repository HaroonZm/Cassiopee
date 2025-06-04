N = int(raw_input())
for game in range(N):
    hand = raw_input().split()
    deck = raw_input().split()
    d = 0
    points = 0

    # Convert values in hand
    for j in range(len(hand)):
        if hand[j] == 'T' or hand[j] == 'J' or hand[j] == 'Q' or hand[j] == 'K':
            hand[j] = 10
        elif hand[j] == 'A':
            hand[j] = 11
        else:
            hand[j] = int(hand[j])

    # Convert values in deck
    for j in range(len(deck)):
        if deck[j] == 'T' or deck[j] == 'J' or deck[j] == 'Q' or deck[j] == 'K':
            deck[j] = 10
        elif deck[j] == 'A':
            deck[j] = 11
        else:
            deck[j] = int(deck[j])

    points = 0
    for card in hand:
        points = points + card

    if points == 21:
        print 'blackjack'
    else:
        while True:
            if points > 21 and 11 in hand:
                hand.remove(11)
                hand.append(1)
                points = points - 10
            if points < 17 or (points < 18 and 11 in hand):
                hand.append(deck[d])
                points = points + deck[d]
                d = d + 1
            else:
                break
        if points > 21:
            print 'bust'
        else:
            print points