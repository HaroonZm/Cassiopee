# Lecture d'un nombre entier à partir de l'entrée standard (habituellement le clavier)
# Il s'agit de la taille de la chaîne de caractères
N = int(input())

# Lecture de la chaîne de caractères, toujours depuis l'entrée standard
C = input()

# Conversion de la chaîne de caractères 'C' en liste de caractères
# Cela donne une liste où chaque élément est un caractère de 'C'
S = list(C)

# Création de la table de programmation dynamique (DP)
# dp[i][j] représente le nombre de façons d'atteindre l'état j à la position i de la chaîne
# La table contient (N+1) lignes (pour 0 à N), et 8 colonnes (pour les états 0 à 7, bien que l'indice 0 ne soit pas utilisé)
# Chaque élément est initialisé à 0
dp = [[0 for i in range(8)] for j in range(N + 1)]

# Initialisation de l'état de départ de la DP
# On part de la position 0 (avant de lire tout caractère de la chaîne), avec l'état 1 mis à 1
# Cela signifie qu'il y a 1 façon d'être à la position 0 dans l'état 1 (c'est l’état initial)
dp[0][1] = 1

# Début d'une boucle pour parcourir tous les caractères de la chaîne C
for i in range(N):
    # Si le caractère courant à la position i est 'J'
    if C[i] == "J":
        # Mise à jour de la DP pour la position suivante (i+1) pour chaque état
        # L'état 1 peut être atteint depuis les états 1 à 4 à l'étape précédente
        dp[i + 1][1] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4]
        # L'état 2 peut être atteint depuis les états 1 à 6 à l'étape précédente
        dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6]
        # L'état 3 peut être atteint depuis les états 1 à 4 et 6, 7 à l'étape précédente
        dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]
        # L'état 4 peut être atteint depuis tous les états (1 à 7) à l'étape précédente sauf l’état 0
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
        # Les états 5, 6, 7 ne peuvent pas être atteints à cette étape
        dp[i + 1][5] = 0
        dp[i + 1][6] = 0
        dp[i + 1][7] = 0
    # Si le caractère courant est 'O'
    if C[i] == 'O':
        # L'état 1 ne peut pas être atteint à cette étape
        dp[i + 1][1] = 0
        # L'état 2 peut être atteint depuis les états 1 à 6 à l'étape précédente
        dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6]
        # L'état 3 ne peut pas être atteint à cette étape
        dp[i + 1][3] = 0
        # L'état 4 peut être atteint depuis tous les états à l’étape précédente (états 1 à 7)
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
        # L'état 5 peut être atteint seulement depuis les états 2, 4, 5, 6
        dp[i + 1][5] = dp[i][2] + dp[i][4] + dp[i][5] + dp[i][6]
        # L'état 6 peut être atteint depuis les états 2, 3, 4, 5, 6, 7
        dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
        # L'état 7 ne peut pas être atteint à cette étape
        dp[i + 1][7] = 0
    # Si le caractère courant est 'I'
    if C[i] == 'I':
        # Les états 1 et 2 ne peuvent pas être atteints à cette étape
        dp[i + 1][1] = 0
        dp[i + 1][2] = 0
        # L'état 3 peut être atteint depuis les états 1 à 4 et 6, 7
        dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]
        # L'état 4 peut être atteint depuis tous les états 1 à 7
        dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
        # L'état 5 ne peut pas être atteint à cette étape
        dp[i + 1][5] = 0
        # L'état 6 peut être atteint depuis les états 2, 3, 4, 5, 6, 7
        dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
        # L'état 7 peut être atteint depuis les états 3, 4, 6, 7
        dp[i + 1][7] = dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]

# A la fin de la boucle, nous avons rempli toute la table dp
# On souhaite connaître le nombre total de façons de terminer à la fin de la chaîne (position N)
# dans n'importe lequel des états possibles (de 1 à 7 inclus)
# On additionne donc dp[N][1], dp[N][2], ..., dp[N][7]
# Puis on prend le reste modulo 10007 pour éviter d'avoir un nombre trop grand (c'est courant dans les problèmes d'algorithmique)
print((dp[N][1] + dp[N][2] + dp[N][3] + dp[N][4] + dp[N][5] + dp[N][6] + dp[N][7]) % 10007)