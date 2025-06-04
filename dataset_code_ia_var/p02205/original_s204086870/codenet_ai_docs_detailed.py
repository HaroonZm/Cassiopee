def process_values():
    """
    Ce programme lit un entier N, puis deux entiers A et B.
    Il applique ensuite une opération répétée N % 12 fois sur A et B :
        - Pour chaque itération impaire, on soustrait B à A.
        - Pour chaque itération paire, on additionne A et B et met le résultat dans B.
    Enfin, il affiche les valeurs finales de A et B.
    """
    # Lecture du nombre de répétitions à effectuer
    N = int(input())  # nombre total d'itérations

    # Lecture des deux entiers A et B séparés par un espace
    A, B = map(int, input().split())  # valeurs initiales de A et B

    # On réduit le nombre d'itérations entre 0 et 11 inclus (cycle de 12)
    N %= 12

    # Boucle principale, effectue N itérations des opérations décrites
    for i in range(1, N + 1):
        # Si l'itération est impaire (i % 2 == 1)
        if i % 2 == 1:
            # On soustrait B à A
            A = A - B
        else:
            # Si l'itération est paire, on additionne A et B, résultat dans B
            B = A + B

    # Affichage du résultat final : valeurs de A puis de B
    print(A, B)

# Appel de la fonction principale du programme
process_values()