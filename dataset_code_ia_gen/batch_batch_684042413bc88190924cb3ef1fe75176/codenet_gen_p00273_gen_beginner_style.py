N = int(input())
for _ in range(N):
    x, y, b, p = map(int, input().split())
    min_cost = 10**9
    # Acheter de 0 à 6 billets de bain (max 6 comme dans l'énoncé)
    for buy_b in range(7):
        # Acheter de 0 à 6 billets piscine
        for buy_p in range(7):
            # Vérifier qu'on a au moins besoin d'acheter les billets utilisés
            if buy_b < b or buy_p < p:
                continue
            total_tickets = buy_b + buy_p
            # Calcul prix sans remise
            cost = buy_b * x + buy_p * y
            # Vérifier si remise applicable
            if buy_b >= 5 and buy_p >= 2:
                cost = int(cost * 0.8)
            if cost < min_cost:
                min_cost = cost
    print(min_cost)