while True:
    try:
        c1, c2, c3 = map(int, input().split())
        my_cards = [c1, c2]
        used_cards = set(my_cards + [c3])
        current_sum = sum(my_cards)
        count_valid = 0
        total_candidates = 0
        for card in range(1, 11):
            if card in used_cards:
                continue
            if current_sum + card <= 20:
                count_valid += 1
            total_candidates += 1
        if total_candidates == 0:
            print("NO")
        else:
            probability = count_valid / total_candidates
            if probability >= 0.5:
                print("YES")
            else:
                print("NO")
    except EOFError:
        break