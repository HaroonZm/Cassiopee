while True:
    # Lire le nombre de légumes à acheter (n) et la capacité du sac (m)
    n, m = map(int, input().split())
    # Condition d'arrêt : deux zéros consécutifs
    if n == 0 and m == 0:
        break

    # Lire les prix des n légumes
    prices = list(map(int, input().split()))
    
    # Tri des prix en ordre décroissant pour maximiser les économies
    prices.sort(reverse=True)

    total = 0
    # Parcourir la liste par groupe de taille m
    for i in range(0, n, m):
        group = prices[i:i+m]
        # Si le groupe est complet (taille m), le légume le moins cher est gratuit
        if len(group) == m:
            total += sum(group) - min(group)
        else:
            # Sinon, pas de réduction
            total += sum(group)

    # Afficher le prix total minimum après remise
    print(total)