def calc_meeting_time():
    """
    Lit deux ensembles d'entiers depuis l'entrée standard, puis calcule et affiche un résultat lié à leur rencontre.

    Entrée:
        Première ligne: deux entiers séparés par un espace (a et b)
        Deuxième ligne: trois entiers séparés par des espaces (p, q, r)

    Calcul effectué:
        - Calcule une valeur 'd' selon la formule: d = p*b - (b-a)*q
        - Affiche le résultat de: (d / (q + r) ) + b
          Ceci peut correspondre à un calcul du temps ou de la position d'une rencontre selon certains paramètres.

    Sortie:
        Affiche un nombre flottant, résultat du calcul décrit ci-dessus.
    """
    # Lecture du premier ensemble d'entrées : deux entiers
    a, b = map(int, input().split())

    # Lecture du second ensemble d'entrées : trois entiers
    p, q, r = map(int, input().split())

    # Calcul du terme intermédiaire 'd'
    # - p * b : multiplie p par b
    # - (b - a) * q : multiplie la différence entre b et a par q
    # - Soustrait le second terme au premier pour obtenir 'd'
    d = p * b - (b - a) * q

    # Calcule le résultat final
    # - Divise 'd' par la somme de q et r
    # - Ajoute b au résultat
    # - Affiche le résultat obtenu
    print(d / (q + r) + b)

# Appelle la fonction principale pour effectuer le calcul
calc_meeting_time()