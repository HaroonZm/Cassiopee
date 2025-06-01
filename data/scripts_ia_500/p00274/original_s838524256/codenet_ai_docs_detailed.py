def process_input():
    """
    Cette fonction traite des séries d'entrées utilisateur en boucle infinie,
    jusqu'à ce qu'une valeur 0 soit entrée, ce qui arrête la boucle.

    Pour chaque entrée (autre que 0), elle lit une liste d'entiers,
    puis effectue les opérations suivantes :
    - Si la valeur maximale de la liste est inférieure à 2, elle affiche "NA".
    - Sinon, elle affiche 1 plus le nombre d'éléments de la liste qui sont strictement positifs.

    Aucun argument n'est nécessaire pour cette fonction.
    """

    while True:
        # Lecture de l'entrée utilisateur et conversion en entier
        n = int(input())

        # Condition d'arrêt : si l'entrée est 0, on quitte la boucle
        if n == 0:
            break

        # Lecture d'une ligne d'entiers séparés par des espaces, puis conversion en liste d'entiers
        t = list(map(int, input().split()))

        # Vérifie si la valeur maximale dans la liste est inférieure à 2
        if max(t) < 2:
            print("NA")
            continue  # Passe à l'itération suivante de la boucle

        # Calcule le nombre d'éléments strictement positifs dans la liste
        count_positive = len([i for i in t if i > 0])

        # Affiche 1 plus le nombre calculé
        print(1 + count_positive)


# Appel de la fonction pour démarrer le traitement
process_input()