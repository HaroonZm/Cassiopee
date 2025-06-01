while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    cards = []
    blank = False
    for _ in range(k):
        x = int(input())
        if x == 0:
            blank = True
        else:
            cards.append(x)

    cards = list(set(cards))
    cards.sort()

    max_len = 0
    # On parcourt les morceaux consécutifs possibles
    for i in range(len(cards)):
        length = 1
        blanks_used = 1 if blank else 0
        current = cards[i]

        for j in range(i+1, len(cards)):
            gap = cards[j] - current -1
            if gap <= blanks_used:
                blanks_used -= gap
                length += 1 + gap
                current = cards[j]
            else:
                length += blanks_used
                blanks_used = 0
                break
        else:
            length += blanks_used

        if length > max_len:
            max_len = length

    print(max_len)