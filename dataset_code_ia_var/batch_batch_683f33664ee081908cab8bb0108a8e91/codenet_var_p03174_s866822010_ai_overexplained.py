# Demander à l'utilisateur d'entrer un entier, qui sera stocké dans la variable 'n'
# La fonction input() lit une chaîne depuis l'entrée standard (typiquement le clavier)
# La fonction int() convertit la chaîne en entier
n = int(input())

# Créer une liste 'a' contenant 'n' sous-listes
# Chaque sous-liste représente une ligne d'entrée, convertie en une liste d'entiers
# La compréhension de liste parcourt une plage de taille n et lit à chaque fois une entrée
# map(int, ... ) convertit chaque élément en entier
# list(...) transforme l'itérable map en liste ordinaire
a = [list(map(int, input().split())) for _ in range(n)]

# Définir une constante 'mod' utilisée pour conserver les résultats dans un intervalle raisonnable
# Pour éviter le débordement d'entier et généralement utilisé dans les problèmes de combinatoire
mod = 10 ** 9 + 7  # Cela signifie 1 000 000 007

# Créer une liste 'dp' ("dynamic programming"), initialisée avec des zéros
# Sa taille est 2^n, c'est-à-dire tous les sous-ensembles possibles d'un ensemble de n éléments
# [0] * k crée une liste contenant k fois la valeur 0
dp = [0] * (1 << n)  # L'opérateur << réalise un décalage binaire à gauche

# Initialiser la valeur de dp[0] à 1
# Cela signifie qu'il y a exactement une façon de ne rien assigner (l'ensemble vide)
dp[0] = 1

# Préparer une table 'bitcount' pour stocker le nombre de bits à 1 (bit de valeur 1) pour chaque nombre jusqu'à 2^n
# Cette table accélèrera le calcul du nombre d'éléments sélectionnés dans le masque binaire
# Initialiser la liste avec le seul élément 0, signifiant que le nombre '0' a zéro bit à 1
bitcount = [0]

# Répéter ce bloc 'n' fois pour remplir la table 'bitcount'
for _ in range(n):
    # À chaque itération, pour le contenu actuel de bitcount,
    # ajouter 1 à chaque valeur et les concaténer à la liste
    # Cela double la taille de la liste à chaque fois
    # [i+1 for i in bitcount] : Par exemple, si bitcount=[0,1], ceci donne [1,2]
    bitcount += [i+1 for i in bitcount]

# Boucle de programmation dynamique pour peupler dp
# Nous considérons tous les masques de bits allant de 1 à 2^n - 1, où chaque bit actif représente une sélection
for bit in range(1, 1 << n):  # Parcourt tous les masques non vides
    # Le nombre d'éléments sélectionnés est le nombre de bits à 1 dans 'bit', grâce à 'bitcount'
    # Par convention, cela correspond à l'indice de la ligne dans la matrice a
    i = bitcount[bit]

    # Boucler sur toutes les positions possibles (de 0 à n-1)
    for j in range(n):
        # Vérifier si le j-ième élément est inclus dans le masque 'bit'
        # (bit >> j) & 1 extrait le j-ième bit de 'bit'
        # ET logique pour déterminer si la position est active dans ce masque
        if (bit >> j) & 1 and a[i - 1][j]:
            # Si la condition est vraie, cela signifie :
            # - Le j-ième élément n'est PAS encore assigné dans le masque précédent
            # - Il peut être apparié avec i-1, puisque a[i-1][j] == 1 (autorisé dans la matrice d'adjacence)

            # Ajouter au nombre de façons d'atteindre le nouvel état ('bit'), le nombre de façons d'atteindre l'ancien état
            # 'bit ^ (1 << j)' désactive le j-ième bit de 'bit' (masque précédent)
            dp[bit] += dp[bit ^ (1 << j)]

    # Après avoir terminé la boucle interne, on prend le reste de la division par 'mod'
    # Cela garantit que les nombres ne deviennent pas trop grands
    dp[bit] %= mod

# Afficher le résultat final
# (1 << n) - 1 est le masque 'plein', où tous les éléments ont été sélectionnés
print(dp[(1 << n) - 1])