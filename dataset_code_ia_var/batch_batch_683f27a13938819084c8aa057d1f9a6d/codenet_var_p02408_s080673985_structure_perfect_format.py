N = int(input())
cards = ["{} {}".format(s, r) for s in ('S', 'H', 'C', 'D') for r in range(1, 14)]
for j in range(N):
    card = input()
    cards.remove(card)
for n in cards:
    print(n)