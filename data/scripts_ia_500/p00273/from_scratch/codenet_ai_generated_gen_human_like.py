N = int(input())
for _ in range(N):
    x, y, b, p = map(int, input().split())
    # On calcule le prix minimal possible en testant toutes les combinaisons d'achat
    min_cost = float('inf')
    # On teste d'acheter de b à 6 billets d'entrée (au moins b pour couvrir la consommation, max 6)
    for buy_b in range(b, 7):
        # Idem pour billets piscine
        for buy_p in range(p, 7):
            total = buy_b * x + buy_p * y
            # Vérifier si la remise s'applique
            if buy_b >= 5 and buy_p >= 2:
                total = int(total * 0.8)
            if total < min_cost:
                min_cost = total
    print(min_cost)