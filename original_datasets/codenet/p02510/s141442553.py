while True:
    card = input().strip()
    if card == '-':
        break

    no_shuffles = int(input())
    for _ in range(no_shuffles):
        h = int(input())
        card = card[h:] + card[:h]

    print(card)