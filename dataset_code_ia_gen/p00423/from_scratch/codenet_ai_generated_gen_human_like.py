while True:
    n = int(input())
    if n == 0:
        break
    a_score = 0
    b_score = 0
    for _ in range(n):
        a_card, b_card = map(int, input().split())
        if a_card > b_card:
            a_score += a_card + b_card
        elif b_card > a_card:
            b_score += a_card + b_card
        else:
            a_score += a_card
            b_score += b_card
    print(a_score, b_score)