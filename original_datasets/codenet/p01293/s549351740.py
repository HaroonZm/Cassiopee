ref = "23456789TJQKA"
def judge(hand,leader):
    led = hand[leader][1]
    mx = tx = winner = -1
    for i in xrange(4):
        num,suit = ref.index(hand[i][0]),hand[i][1]
        if suit == trump:
            if num > tx:
                tx = num
                winner = i
        elif tx == -1:
            if suit == led and num > mx:
                mx = num
                winner = i
    return winner
    
while 1:
    trump = raw_input()
    if trump == "#": break
    hands = [raw_input().split() for i in xrange(4)]
    hands = zip(hands[0],hands[1],hands[2],hands[3])
    leader = ns = ew = 0
    for hand in hands:
        leader = judge(hand, leader)
        if leader in [0,2]: ns += 1
        else: ew += 1
    if ns > ew: print "NS",ns-6
    else: print "EW",ew-6