def search(a_cards, b_cards, left, right, turn):
    # Utilisation d'expressions ternaires et recursion imbriquée
    if not a_cards:
        return True
    if not b_cards:
        return False

    if turn == 0:
        if left not in a_cards and right not in a_cards:
            return search(a_cards, b_cards, left, right, 1)
        res = False
        if left in a_cards:
            reduced_a = list(filter(lambda x: x != left, a_cards))
            res = res or search(reduced_a, b_cards, left - 1, right, 1)
        if right in a_cards:
            reduced_a = [x for x in a_cards if x != right]
            res = res or search(reduced_a, b_cards, left, right + 1, 1)
        return res
    else:
        # boucle imperativement les conditions left/right
        ret = True
        if left not in b_cards and right not in b_cards:
            return search(a_cards, b_cards, left, right, 0)
        for side in ['left', 'right']:
            card = left if side == 'left' else right
            if card in b_cards:
                new_b = [x for x in b_cards if x != card]
                new_left = left - 1 if side == 'left' else left
                new_right = right + 1 if side == 'right' else right
                ret = ret and search(a_cards, new_b, new_left, new_right, 0)
        return ret

n = int(input())
all_cards = []
i = 1
while i <= 13:
    if i != 7:
        all_cards.append(i)
    i += 1

for _ in range(n):
    a_cards = list(map(int, input().strip().split()))
    b_cards = []
    for card in all_cards:
        if card not in a_cards:
            b_cards.append(card)

    result = search(a_cards, b_cards, 6, 8, 0)
    print("yes" if result else "no")