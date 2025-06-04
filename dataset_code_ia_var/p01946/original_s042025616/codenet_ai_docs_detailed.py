def main():
    """
    Lecture des entrées depuis l'utilisateur, exécution de la logique principale pour déterminer
    le nombre minimal d'étapes nécessaires afin que la valeur initiale (S-T avec des incréments/décréments W)
    devienne inférieure ou égale à zéro, en tenant compte de cycles complets éventuels.
    Affiche le nombre d'étapes ou -1 si ce n'est pas possible.
    """

    # Lire les valeurs de base S (initial), T (objectif), D (nombre d'étapes dans un cycle)
    S, T, D = map(int, input().split())

    # Calculer la différence initiale à dépasser/atteindre
    S -= T

    # Lire les D variations pour chaque étape du cycle et les stocker dans la liste W
    W = list(map(int, input().split()))

    # Calculer la somme totale des variations sur un cycle
    F = sum(W)

    # Cas où la somme des variations sur un cycle est nulle ou positive
    if F >= 0:
        su = S  # Valeur courante du compteur modifiée à chaque étape

        # Parcourir chaque étape et appliquer l'incrément correspondant
        for i, w in enumerate(W):
            su += w
            # Si la valeur devient <= 0, afficher le numéro de l'étape (1-indexé)
            if su <= 0:
                print(i + 1)
                break
        else:
            # S'il n'est jamais possible d'atteindre la condition, afficher -1
            print(-1)
        # Sortir du programme car la réponse a été trouvée
        return

    # Si la somme sur un cycle est négative, il faut peut-être faire plusieurs cycles complets

    su = 0  # Somme partielle des incréments lors d'un cycle complet
    mi = 0  # Valeur minimale atteinte durant un cycle

    # Calculer la valeur la plus basse atteinte à l'intérieur d'un cycle
    for d in W:
        su += d
        mi = min(mi, su)

    # Calculer combien de cycles complets sont nécessaires avant d'espérer franchir le seuil avec un reste d'étapes
    # k = max((S + mi - F - 1) // -F, 0)
    # (S + mi - F - 1) // -F permet d'obtenir le nombre d'itérations entières nécessaires pour passer sous zéro
    k = max((S + mi - F - 1) // -F, 0)

    # Mettre à jour S après k cycles complets
    S += k * F

    # Parcourir ensuite le prochain cycle d'étapes pour voir à quel moment on franchit le seuil
    for i, w in enumerate(W):
        S += w
        if S <= 0:
            # Afficher le nombre total d'étapes réalisées (incluant tous les cycles complets + position courante)
            print(i + 1 + k * D)
            break
    else:
        # This state should never be reached si la logique est correcte
        assert False

if __name__ == "__main__":
    main()