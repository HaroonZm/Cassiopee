n, m = tuple(map(int, input().split()))
cards = []
for _ in range(m):
    cards.append(list(map(int, input().split())))

cards.sort(key=lambda x: x[0])
cards.reverse()

cost = 0
i = 0
while i < len(cards) - 1:
    card = cards[i]
    if card[0] < n:
        cost = cost + (n - card[0])
    i += 1

print(cost)