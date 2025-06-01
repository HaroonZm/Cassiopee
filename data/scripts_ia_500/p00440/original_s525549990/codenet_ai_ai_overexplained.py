# Boucle infinie pour traiter plusieurs séries de données jusqu'à une condition d'arrêt
while True:
    # Lecture d'une ligne contenant deux entiers séparés par un espace, puis conversion de chacun en int
    # map applique la fonction int à chaque élément résultant du split de la chaîne input
    n, k = map(int, input().split())

    # Condition de sortie de la boucle infinie : si n vaut 0, on arrête le traitement
    if not n:
        break

    # Lecture successive de k entiers provenant de l'entrée standard, stockés dans une liste appelée cards
    # L'expression [int(input()) for _ in range(k)] est une compréhension de liste qui répète k fois
    # la lecture et conversion d'une entrée.
    cards = [int(input()) for _ in range(k)]

    # Tri des éléments de la liste cards en ordre décroissant, c'est-à-dire du plus grand au plus petit
    cards.sort(reverse=True)

    # Initialisation d'un booléen pour marquer la présence éventuelle de la carte "blanche"
    white = False

    # Vérification de la présence d'une carte "blanche" qui serait représentée par l'entier 0 en dernière position
    # puisque la liste est triée en ordre décroissant, le plus petit élément est en fin de liste (index -1)
    if not cards[-1]:
        # On indique qu'il y a une carte blanche
        white = True
        # Suppression de la carte blanche de la liste cards
        cards.pop()

    # Si après suppression de la carte blanche, la liste cards est vide,
    # cela signifie qu'il n'y avait que la carte blanche
    if not cards:
        # Dans ce cas, on imprime 1 car la plus longue séquence de cartes consécutives est 1
        print(1)
        # On passe à la prochaine itération de la boucle principale
        continue

    # Extraction du dernier élément de la liste cards qui est le plus petit encore présent
    prev = cards.pop()
    # Initialisation du compteur courant de suite consécutive
    cnt = 1
    # Initialisation du compteur précédent de suite consécutive utilisée pour combiner avec la blanche
    precnt = 0

    # Initialisation de la variable réponse à 1, la plus petite suite possible
    ans = 1

    # Tant que la liste cards n'est pas vide, on continue d'examiner les cartes
    while cards:
        # Prendre la prochaine carte la plus petite
        cur = cards.pop()
        # Calcul de la différence entre la carte actuelle et la précédente pour détecter une suite consécutive
        diff = cur - prev

        if diff == 1:
            # Si la différence est exactement 1, cela signifie que les cartes sont consécutives
            # On incrémente le compteur courant de cartes consécutives
            cnt += 1
        else:
            # Si les cartes ne sont plus consécutives, on met à jour la réponse maximale
            # avec la somme du compteur précédent et du compteur courant
            ans = max(ans, precnt + cnt)

            # On prépare le compteur précédent : si on a une carte blanche et l'écart est de 2, on peut "sauter"
            # une valeur grâce à la blanche, donc on prépare precnt = cnt + 1
            # Sinon, on réinitialise precnt à 0
            precnt = (cnt + 1) if white and diff == 2 else 0

            # Réinitialisation du compteur courant à 1 (pour la nouvelle suite commençant avec cur)
            cnt = 1

        # On met à jour la variable prev à la carte actuelle pour la prochaine itération
        prev = cur

    # Après la boucle, on vérifie une ultime fois si la combinaison des compteurs est la meilleure
    ans = max(ans, precnt + cnt)

    # Affichage du résultat final : la longueur maximale possible de la séquence de cartes consécutives
    print(ans)