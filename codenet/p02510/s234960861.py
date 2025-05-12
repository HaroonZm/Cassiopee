def shuffle(card, h):
    card_list = list(card)
    new_card_list = card_list[h:]
    new_card_list.extend(card_list[0:h])
    return ''.join(new_card_list)

while True:
    card = raw_input().rstrip()
    if card == '-':
        break
    else:
        shuffles = int(raw_input())
        for i in range(shuffles):
            h = int(raw_input())
            card = shuffle(card, h)
        print card