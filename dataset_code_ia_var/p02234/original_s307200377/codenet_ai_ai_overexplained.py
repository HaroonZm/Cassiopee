# Ce programme implémente l'algorithme d'optimisation de la chaîne de multiplication de matrices (Matrix Chain Multiplication).
# L'objectif est de déterminer l'ordre optimal pour multiplier une séquence de matrices afin de minimiser le nombre total de multiplications scalaires.

# On commence par lire un entier depuis l'entrée utilisateur.
n = int(input())  # 'n' représente le nombre de matrices à multiplier.

# On va stocker dans la liste 'p' les dimensions des matrices de la chaîne.
# Pour 'n' matrices, il faut 'n+1' dimensions.
# Initialement, on met des zéros partout pour réserver la place pour 'n+1' entiers.
p = [0] * (n + 1)

# Maintenant, on lit les dimensions de chaque matrice.
# On répète cela 'n' fois, c'est-à-dire une fois pour chaque matrice.
# Les matrices sont notées M1, M2, ..., Mn.
for i in range(1, n + 1):
    # On lit les deux entiers de la ligne correspondant à la dimension de la matrice courante.
    # Ces deux entiers représentent le nombre de lignes et de colonnes de la i-ème matrice.
    # On utilise 'map(int, input().split())' pour transformer l'entrée texte directement en deux entiers.
    # On range la première dimension dans p[i-1] et la seconde dimension dans p[i].
    # Ainsi, si la i-ème matrice a des dimensions A x B, alors p[i-1]=A et p[i]=B.
    p[i - 1], p[i] = map(int, input().split())

# On définit la matrice 'm' qui va contenir les coûts minimaux pour multiplier des sous-séquences de matrices.
# 'm[i][j]' contiendra le nombre minimal de multiplications nécessaires pour multiplier les matrices de i à j (inclus).
# On crée une liste à deux dimensions (tableau de listes) d'entiers, initialisée à 0.
# Il y a (n+1) lignes et (n+1) colonnes car les indices vont de 0 à n inclut.
m = [[0] * (n + 1) for _ in range(n + 1)]

# On applique la programmation dynamique pour remplir la table 'm'.
# La variable 'l' représente la longueur de la sous-chaîne de matrices considérée (au moins 2 puisqu’il n'y a rien à optimiser pour une seule matrice).
for l in range(2, n + 1):
    # Pour toutes les sous-chaînes de longueur 'l', on itère sur leur point de départ 'i'.
    # 'i' commence à 1 et doit s'arrêter de sorte que la sous-chaîne ne déborde pas de la séquence complète.
    # Le dernier départ possible est à 'n-l+1', car 'i+l-1' doit être <= n.
    for i in range(1, n - l + 2):
        # 'i' est le point de départ de la sous-chaîne.
        # On calcule 'j', qui est le point d'arrivée de la sous-chaîne de longueur 'l' débutant en 'i'.
        j = i + l - 1  # 'j' est inclus.

        # On initialise le coût minimal de cette sous-chaîne à l'infini,
        # car on souhaite trouver le minimum et toute valeur réelle sera inférieure à l'infini.
        m[i][j] = float("inf")

        # On essaye tous les points possibles pour couper la sous-chaîne (c'est-à-dire choisir où faire la dernière multiplication).
        # Cela correspond à multiplier d'abord les matrices i à k puis k+1 à j, puis combiner le résultat.
        for k in range(i, j):
            # Calculons le coût total :
            # - m[i][k] = coût pour multiplier les matrices de i à k (sous-problème de gauche)
            # - m[k+1][j] = coût pour multiplier les matrices de k+1 à j (sous-problème de droite)
            # - p[i-1]*p[k]*p[j] = coût pour multiplier le résultat des deux sous-problèmes (convention connue)
            cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

            # On garde le coût minimal parmi toutes les possibilités de coupure
            if cost < m[i][j]:
                m[i][j] = cost  # On met à jour si on trouve un coût inférieur

# À la fin, m[1][n] contient le coût minimal pour multiplier toute la chaîne de matrices de 1 à n.
# On affiche donc le résultat.
print(m[1][n])