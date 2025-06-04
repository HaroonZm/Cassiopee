def main():
    """
    Lecture de l'entrée utilisateur, tri des éléments, et calcul du coût minimum
    pour obtenir une quantité donnée d'articles à partir de différents fournisseurs
    aux prix unitaires respectifs.

    Entrées :
    - La première ligne contient deux entiers N (nombre de fournisseurs) et M (quantité totale à acheter).
    - Les N lignes suivantes contiennent chacune deux entiers a (prix unitaire) et b (quantité disponible).

    Affiche le coût minimum pour acheter M articles.
    """
    # Lecture du nombre de fournisseurs (N) et de la quantité totale à acheter (M)
    N, M = map(int, input().split())

    # Pour chaque fournisseur, lire le prix unitaire a et la quantité disponible b,
    # puis stocker ces tuples dans une liste. On trie ensuite la liste de tuples
    # par prix unitaire croissant afin d'acheter d'abord au meilleur prix.
    AB = sorted([tuple(map(int, input().split())) for _ in range(N)])

    count = 0  # Compteur pour le nombre d'articles achetés jusqu'à présent
    ans = 0    # Coût total accumulé

    # Parcours des fournisseurs triés par prix unitaire
    for a, b in AB:
        # Si on peut atteindre ou dépasser le nombre total d'articles requis avec ce fournisseur
        if count + b >= M:
            # N'acheter que le nombre exact d'articles restant nécessaires pour atteindre M
            ans += a * (M - count)
            break  # Objectif atteint ; arrêter les achats
        else:
            # Acheter tous les articles disponibles chez ce fournisseur
            ans += a * b
            count += b  # Mettre à jour le compteur d'articles achetés

    # Affichage du coût total minimum
    print(ans)

if __name__ == "__main__":
    main()