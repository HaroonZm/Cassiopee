def calculate_jumps():
    """
    Calcule le nombre total de sauts nécessaires pour parcourir une distance D
    en utilisant deux types de sauts :
    - Sauts de longueur L (sauts longs)
    - Sauts de longueur 1 (sauts courts) pour parcourir la distance restante

    La fonction lit deux entiers depuis l'entrée standard séparés par un espace :
    - D : la distance totale à parcourir
    - L : la longueur de chaque saut long

    Elle affiche ensuite le nombre total de sauts effectués pour atteindre exactement 
    la distance D.
    """
    # Lecture des valeurs D (distance totale) et L (longueur d'un saut long)
    D, L = map(int, input().split())
    
    # Initialisation du compteur de sauts
    jump = 0
    
    # Effectuer autant de sauts longs que possible
    while True:
        # Si la distance restante est inférieure à la longueur du saut long,
        # on sort de cette boucle car on ne peut plus faire de saut long complet
        if D < L:
            break
        # Réduire la distance restante en faisant un saut long
        D -= L
        # Incrémenter le nombre total de sauts
        jump += 1
    
    # Effectuer les sauts courts pour parcourir la distance restante
    while True:
        # Si la distance restante est nulle, on a fini
        if D == 0:
            break
        # Réduire la distance restante d'un saut court (distance 1)
        D -= 1
        # Incrémenter le nombre total de sauts
        jump += 1
    
    # Afficher le nombre total de sauts nécessaires pour atteindre la distance D
    print(jump)

# Appel de la fonction principale pour exécuter le calcul
calculate_jumps()