# Demander à l'utilisateur de saisir un entier qui sera utilisé comme taille de la matrice à traiter
N = int(input())  # Lecture d'une valeur entière au clavier pour déterminer le nombre de matrices à traiter

# Créer une liste 'input_' contenant initialement la valeur de N à la première position
input_ = [N]  # Utiliser une liste car nous allons y stocker les entrées suivantes relatives aux matrices

# Utiliser une boucle for pour demander à l'utilisateur de saisir N lignes de texte
for n in range(N):  # La variable n prendra successivement les valeurs de 0 à N-1
    input_.append(input())  # Ajouter chaque ligne saisie par l'utilisateur à la fin de la liste input_

# Créer une liste vide 'P' qui contiendra les dimensions des matrices
P = []  # Cette liste stockera les dimensions extraites des entrées utilisateur

# Extraire la première dimension de chaque matrice depuis chaque ligne de 'input_'
for n in range(N):  # Parcourir les N lignes d'entrée restante
    # La ligne input_[n+1] (on ajoute 1 car input_[0] contient la valeur de N) contient deux entiers représentant les dimensions de la matrice
    # On sépare la ligne par les espaces puis on prend l'élément d'indice 0 (la première dimension)
    P.append(int(input_[n + 1].split()[0]))  # Convertir l'élément en entier puis l'ajouter à la liste P

# Ajouter la deuxième dimension de la dernière matrice (car il s'agit de la dimension partagée par toutes les chaînes de matrices)
P.append(int(input_[n + 1].split()[1]))  # Le dernier n de la boucle précédente vaut N-1 donc n+1 == N

# Créer une matrice carrée M de taille N x N, initialisée avec des zéros
# M[i][j] va stocker le coût minimal pour multiplier la séquence de matrices allant de i à j inclus
M = [[0] * (N) for x in range(N)]  # Génère une liste de N listes, chacune de taille N, remplies de zéros

# Cette partie effectue une programmation dynamique pour remplir la matrice M
# On cherche le coût minimal de multiplication d'une chaîne de matrices
for n in range(1, N):  # n représente la longueur de la chaîne de matrices - 1
    for i in range(N - n):  # i représente l'indice de départ de la sous-chaîne de matrices
        # Initialiser la case M[i][i+n] avec une valeur très grande (ici 10^100) car on cherche un minimum ensuite
        M[i][i + n] = 10 ** 100
        # Examiner chaque possible position de coupure k entre i et i+n
        for k in range(i, i + n):  # k prend chaque valeur possible de coupure
            # Récupérer les dimensions pertinentes pour le calcul du coût d'une multiplication de matrices
            P_0 = P[i]          # Dimension de ligne de la première matrice de la sous-chaîne
            P_1 = P[k + 1]      # Dimension colonne/ligne à la jonction
            P_2 = P[i + n + 1]  # Dimension de colonne de la dernière matrice de la sous-chaîne
            # Calculer le coût total pour ce choix de k : coût des deux sous-chaînes + coût de la multiplication finale
            M_ = M[i][k] + M[k + 1][i + n] + P_0 * P_1 * P_2
            # Conserver le minimum : comparer le coût actuel à la valeur stockée, et conserver la plus petite
            M[i][i + n] = min(M[i][i + n], M_)

# Afficher le résultat final (coût minimal pour multiplier toutes les matrices dans l'ordre donné)
# M[0][-1] donne la valeur dans le coin supérieur droit de la matrice, c'est-à-dire le coût minimal global
print(M[0][-1])  # Afficher le résultat à l'utilisateur