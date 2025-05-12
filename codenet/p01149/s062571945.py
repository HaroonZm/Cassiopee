N=int(raw_input())
for i in range(N):
    hand=raw_input().split()
    deck=raw_input().split()
    #defaulthand
    d=0
    points=0
    for i in range(len(hand)):
        if hand[i] in ['T','J','Q','K']:
            hand[i]=10
        elif hand[i]=='A':
            hand[i]=11
        else:
           hand[i]=int(hand[i])
    for i in range(len(deck)):
        if deck[i] in ['T','J','Q','K']:
            deck[i]=10
        elif deck[i]=='A':
            deck[i]=11
        else:
           deck[i]=int(deck[i])
    points=sum(hand)
    if points==21:
        print 'blackjack'
    else:
        while(1):
            if points>21 and 11 in hand:
                hand.remove(11)
                hand.append(1)
                points=points-10
            if (points<17) or (points<18 and 11 in hand):
            	hand.append(deck[d])
            	points=points+deck[d]
                d=d+1
            else:
                break
        if points>21:
            print 'bust'
        else:
            print points