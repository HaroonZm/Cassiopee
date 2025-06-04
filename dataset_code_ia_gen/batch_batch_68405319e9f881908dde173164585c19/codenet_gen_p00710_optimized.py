while True:
    n, r = map(int, input().split())
    if n == 0 and r == 0:
        break
    deck = list(range(1, n + 1))
    for _ in range(r):
        p, c = map(int, input().split())
        cut = deck[-p:-p + c]
        del deck[-p:-p + c]
        deck.extend(cut)
    print(deck[-1])