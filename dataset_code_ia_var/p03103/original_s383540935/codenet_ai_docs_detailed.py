def calculate_minimum_cost():
    """
    Lit les données d'entrée, trie les offres disponibles, puis calcule le coût minimum
    pour acheter une quantité donnée de produits en achetant d'abord les moins chers.

    Entrées attendues sur l'entrée standard :
    - La première ligne contient deux entiers, N (nombre d'offres) et M (quantité totale à acheter).
    - Les N lignes suivantes contiennent chacune deux entiers : le prix unitaire et la quantité disponible pour chaque offre.

    Exemple d'appel :
    > calculate_minimum_cost()
    (et renseigner les entrées attendues)
    """
    # Lecture de la première ligne : N = nombre d'offres, M = quantité à acheter
    N, M = map(int, input().split())

    # Initialisation d'une liste pour stocker chaque offre sous forme [prix, quantité]
    offers = [list(map(int, input().split())) for _ in range(N)]

    # Trie les offres selon le prix unitaire croissant
    # Cela permet d'acheter chez les vendeurs les moins chers en priorité
    offers.sort(key=lambda x: x[0])

    # Initialise les variables pour suivre la quantité restante à acheter et le coût total
    remain = M  # Quantité de produit restante à acheter
    cost = 0    # Coût total accumulé

    # Parcours des offres triées
    for i in range(N):
        price, available = offers[i]  # Prix unitaire et quantité disponible de l'offre actuelle

        # Si on peut tout prendre dans cette offre
        if remain >= available:
            cost += price * available   # Calcule le coût pour toute la quantité disponible
            remain -= available        # Met à jour la quantité restante à acheter
        else:
            # Sinon, on achète juste ce qu'il reste à acheter
            cost += price * remain
            remain = 0   # Plus rien à acheter

        # Si on a acheté tout ce qui était nécessaire, on sort de la boucle
        if remain == 0:
            break

    # Affiche le coût total pour acheter la quantité demandée
    print(cost)

# Appel de la fonction principale
calculate_minimum_cost()