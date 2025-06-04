cards = []
suits = ['S', 'H', 'C', 'D']
for suit in suits:
    for num in range(1, 14):
        cards.append(suit + ' ' + str(num))

N = int(raw_input())
for i in range(N):
    line = raw_input()
    parts = line.split()
    suit = parts[0]
    number = parts[1]
    card = suit + ' ' + number
    cards.remove(card)

for card in cards:
    print card