n = int(input())
m = int(input())

cards = []
for i in range(1, 2*n + 1):
    cards.append(i)

for i in range(m):
    ope = int(input())
    if ope == 0:
        first_part = cards[:n]
        second_part = cards[n:]
        new_cards = []
        for j in range(n):
            new_cards.append(first_part[j])
            new_cards.append(second_part[j])
        cards = new_cards
    else:
        first_part = cards[:ope]
        second_part = cards[ope:]
        cards = second_part + first_part

for card in cards:
    print(card)