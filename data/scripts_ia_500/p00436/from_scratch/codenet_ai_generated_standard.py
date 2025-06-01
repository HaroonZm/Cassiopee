n = int(input())
m = int(input())
cards = list(range(1, 2*n+1))
for _ in range(m):
    k = int(input())
    if k == 0:
        A = cards[:n]
        B = cards[n:]
        cards = [val for pair in zip(A,B) for val in pair]
    else:
        cards = cards[k:] + cards[:k]
for card in cards:
    print(card)