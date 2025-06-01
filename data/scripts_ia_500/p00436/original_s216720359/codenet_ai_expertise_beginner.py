n = int(input())
m = int(input())

cards = list(range(1, 2 * n + 1))

for _ in range(m):
    op = int(input())
    if op == 0:
        # mélange
        new_cards = []
        for i in range(n):
            new_cards.append(cards[i])
            new_cards.append(cards[i + n])
        cards = new_cards
    else:
        # coupe
        k = op
        cards = cards[k:] + cards[:k]

for card in cards:
    print(card)