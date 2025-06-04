h = [input() for i in range(3)]
hand = {'a': h[0], 'b': h[1], 'c': h[2]}
count = {'a': 0, 'b': 0, 'c': 0}

def who_is_the_winner(ch):
    if ch == 'a':
        winner = 'A'
    elif ch == 'b':
        winner = 'B'
    else:
        winner = 'C'
    return winner

ch = 'a'
while True:
    count[ch] += 1
    if count[ch] == len(hand[ch]) + 1:
        winner = who_is_the_winner(ch)
        print(winner)
        break
    ch = hand[ch][count[ch] - 1]