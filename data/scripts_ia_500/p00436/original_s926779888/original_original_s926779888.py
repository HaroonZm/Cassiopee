n = int(input())
m = int(input())
card = list(range(1, 2*n+1))

for _ in range(m):
    ope = int(input())
    if ope == 0:
        card1 = card[:n]
        card2 = card[n:]
        card = []
        for c1, c2 in zip(card1, card2):
            card.append(c1)
            card.append(c2)
    else:
        card1 = card[:ope]
        card2 = card[ope:]
        card = []
        card.extend(card2)
        card.extend(card1)

for c in card:
    print(c)