while True:
    try:
        C1, C2, C3 = map(int, input().split())
    except:
        break

    used_cards = [C1, C2, C3]
    total = C1 + C2
    count_ok = 0
    count_total = 0

    for card in range(1, 11):
        if card in used_cards:
            continue
        if total + card <= 20:
            count_ok += 1
        count_total += 1

    if count_total == 0:
        print("NO")
    else:
        if count_ok / count_total >= 0.5:
            print("YES")
        else:
            print("NO")