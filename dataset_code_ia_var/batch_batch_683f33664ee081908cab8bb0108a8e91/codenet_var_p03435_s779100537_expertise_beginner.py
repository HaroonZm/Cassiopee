def ans():
    # On crée une "grille" vide C, on ignore l'indice 0 pour faciliter l'indexation à partir de 1
    C = [[], [], [], []]
    # On lit les 3 lignes d'entrées utilisateur, on ajoute un zéro devant pour gérer l'indexation à partir de 1
    ligne1 = input()
    ligne2 = input()
    ligne3 = input()
    C[1] = [0] + [int(x) for x in ligne1.split()]
    C[2] = [0] + [int(x) for x in ligne2.split()]
    C[3] = [0] + [int(x) for x in ligne3.split()]

    # On crée deux listes pour A et B (leurs valeurs commencent à l'indice 1)
    A = [0, 0, 0, 0]
    B = [0, 0, 0, 0]

    # On fixe A[1] à 0
    A[1] = 0

    # On calcule les B[i] en utilisant la première ligne de C et A[1]
    for i in range(1, 4):
        B[i] = C[1][i] - A[1]

    # On calcule les A[i] (de 2 à 3) en utilisant la première colonne de C et B[1]
    for i in range(2, 4):
        A[i] = C[i][1] - B[1]

    # On vérifie si C[i][j] == A[i] + B[j] pour chaque case (sauf la ligne et colonne 0)
    for i in range(1, 4):
        for j in range(1, 4):
            if C[i][j] != (A[i] + B[j]):
                print('No')
                return
    print('Yes')

ans()