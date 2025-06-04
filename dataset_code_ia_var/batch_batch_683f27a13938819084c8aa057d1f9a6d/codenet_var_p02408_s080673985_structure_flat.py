N = int(input())
cards = []
suits = ('S', 'H', 'C', 'D')
for s in suits:
    for r in range(1, 14):
        cards.append(f"{s} {r}")
j = 0
while j < N:
    card = input()
    cards.remove(card)
    j += 1
i = 0
while i < len(cards):
    print(cards[i])
    i += 1