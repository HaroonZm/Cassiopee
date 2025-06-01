Q = int(input())
for _ in range(Q):
    c, a, n = map(int, input().split())
    max_teams = 0
    # essayer toutes les combinaisons de 3 types d'équipes
    for ccc in range(c // 3 + 1):
        for cca in range(min((c - 3 * ccc) // 2, a) + 1):
            # nombre d' équipes CAN possibles avec le reste
            c_left = c - 3 * ccc - 2 * cca
            a_left = a - cca
            n_left = n
            can = min(c_left, a_left, n_left)
            total = ccc + cca + can
            if total > max_teams:
                max_teams = total
    print(max_teams)