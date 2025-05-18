n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(m)]
cards = sorted(cards, key=lambda x: x[0])[::-1]
cost = 0
for card in cards[:-1]:
    if card[0] < n:
        cost += n - card[0]

print(cost)