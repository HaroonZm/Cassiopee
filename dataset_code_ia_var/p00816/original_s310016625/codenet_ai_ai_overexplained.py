#!/usr/bin/env python3

# Entrée dans une boucle infinie afin de traiter plusieurs lignes d'entrée utilisateur jusqu'à une condition d'arrêt explicite
while True:
    # Lecture d'une ligne depuis l'entrée standard (clavier). L'utilisateur doit saisir deux valeurs séparées par un espace
    t, n = input().split()  # 't' est une chaîne représentant une valeur entière, 'n' est une chaîne représentant un nombre

    # Conversion de 't' de chaîne de caractère à entier
    t = int(t)

    # Si l'utilisateur saisit 0 pour 't', le programme doit s'arrêter immédiatement (condition d'arrêt)
    if t == 0:
        exit()  # Fin du programme

    # Calcul de la longueur de la chaîne 'n', c'est-à-dire le nombre de chiffres dans le nombre fourni
    L = len(n)

    # Initialisation de la variable qui va garder la valeur maximale trouvée pour la somme des parties
    m = 0

    # Initialisation de la liste qui contiendra la combinaison de parties conduisant à la somme maximale acceptable
    parts = []

    # Initialisation d'un indicateur booléen pour déterminer s'il y a plusieurs décompositions donnant la même somme maximale
    f = False

    # Début d'une boucle sur toutes les possibilités de coupures entre les chiffres de 'n'
    # Il y a 2^(L-1) possibilités pour placer ou non une coupure entre chaque chiffre, où chaque possibilité est représentée par un entier 'b'
    for b in range(1 << (L - 1)):
        # Démarre avec le premier chiffre de 'n', converti en entier (pour reconstituer des nombres à partir de morceaux de chiffres)
        c = int(n[0])

        # Variable pour additionner les valeurs des parties formées
        s = 0

        # Liste temporaire pour garder les valeurs des différents morceaux pour cette configuration de coupures
        li = []

        # Boucle pour examiner chaque position où une coupure pourrait être faite, sauf avant le premier chiffre
        for k in range(L - 1):
            # Vérifie si la coupure doit être faite après la position 'k'
            # 'b >> k' décale le bit k tout à droite, '& 1' isole la valeur de ce bit
            if b >> k & 1 == 1:
                # Si le bit correspondant vaut 1, on fait une coupure après le chiffre actuel
                # On ajoute la valeur courante de 'c' à la somme totale
                s += c

                # On enregistre ce morceau dans la liste temporaire
                li.append(c)

                # Redémarre le morceau suivant avec la valeur du chiffre à la position suivante
                c = 0

            # Dans tous les cas, on ajoute le chiffre suivant à 'c'
            # Multiplie 'c' par 10 (décalage décimal) et ajoute l'entier correspondant au chiffre suivant dans 'n'
            c = 10 * c + int(n[k + 1])

        # Après la boucle, il reste une dernière partie à ajouter (car il n'y a pas de coupure à droite du dernier chiffre)
        s += c
        li.append(c)
        c = 0  # (Remise à zéro de 'c' même si ce n'est plus utile après la boucle)

        # Si la somme totale des morceaux dépasse la limite 't', cette configuration est ignorée (car non valide)
        if s > t:
            continue  # Passe à la configuration suivante

        # Si la somme obtenue est meilleure ou égale à la meilleure trouvée jusqu'à présent, on doit mettre à jour le meilleur résultat
        if s >= m:
            # Détecte si on obtient une autre façon d'atteindre au moins la même somme maximale (égalité stricte)
            f = (s == m)

            # Met à jour la meilleure somme trouvée
            m = s

            # Stocke la configuration actuelle comme étant la meilleure trouvée jusqu'à présent
            parts = li

    # Après avoir exploré toutes les coupures possibles, il faut afficher le résultat selon ce qui a été détecté

    # Si 'f' est vrai (il y a eu ambiguité : plusieurs découpages donnent la même somme maximale), afficher 'rejected'
    if f:
        print('rejected')
    # Si aucune configuration valide n'a été trouvée (valeur maximale restée à 0), afficher 'error'
    elif m == 0:
        print('error')
    # Sinon, on affiche la meilleure somme trouvée, suivie de la décomposition correspondante (tous séparés par des espaces)
    else:
        print(m, *parts, sep=' ')