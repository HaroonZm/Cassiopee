n = int(input())
m = int(input())
ks = []
for i in range(m):
    ks.append(int(input()))

cards = []
for i in range(1, n * 2 + 1):
    cards.append(i)

for k in ks:
    if k == 0:
        new_cards = []
        part1 = cards[:n]
        part2 = cards[n:]
        for i in range(n):
            new_cards.append(part1[i])
            new_cards.append(part2[i])
        cards = new_cards
    else:
        cards = cards[k:] + cards[:k]

for v in cards:
    print(v)