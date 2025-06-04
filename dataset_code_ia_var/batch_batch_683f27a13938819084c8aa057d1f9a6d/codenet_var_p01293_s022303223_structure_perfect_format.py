ref = "23456789TJQKA"

def judge(hand, led):
    l = hand[led][1]
    mx = tx = w = -1
    for i in xrange(4):
        num, s = ref.index(hand[i][0]), hand[i][1]
        if s == t and num > tx:
            tx, w = num, i
        elif tx == -1 and s == l and num > mx:
            mx, w = num, i
    return w

while 1:
    t = raw_input()
    if t == "#":
        break
    hands = [raw_input().split() for i in xrange(4)]
    hands = zip(hands[0], hands[1], hands[2], hands[3])
    led = 0
    win = [0] * 2
    for hand in hands:
        led = judge(hand, led)
        win[led % 2] += 1
    if win[0] > win[1]:
        print "NS", win[0] - 6
    else:
        print "EW", win[1] - 6