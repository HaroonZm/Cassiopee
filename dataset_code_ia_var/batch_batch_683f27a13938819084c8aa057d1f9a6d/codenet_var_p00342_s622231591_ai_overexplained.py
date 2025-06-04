# Demander à l'utilisateur de saisir un entier, puis convertir la saisie (qui est une chaîne de caractères) en type int.
n = int(input())  # n représente le nombre d'éléments qu'on va lire ensuite

# Demander à l'utilisateur de saisir une liste de nombres séparés par des espaces.
# On utilise input() pour lire la chaîne, puis split() pour la découper en morceaux (chaînes représentant des nombres).
# map(int, ...) applique la fonction int à chaque élément, transformant chaque chaîne en entier.
# sorted(...) trie la liste d'entiers par ordre croissant et retourne une nouvelle liste triée (ne modifie pas l'original).
a = sorted(map(int, input().split()))  # La liste 'a' contient les n nombres triés par ordre croissant.

# On va créer une nouvelle liste 'b'.
# b sera une liste de tuples (différence consécutive, indice du premier élément de la paire).
# Pour chaque indice i, où i varie de 0 à n-2 inclus (parce qu'on regarde des paires a[i], a[i+1]),
# on calcule la différence entre a[i+1] et a[i] (donc l'écart entre deux éléments consécutifs),
# et on stocke l'indice i pour référence ultérieure.
b = [(a[i + 1] - a[i], i) for i in range(n - 1)]

# Trier la liste 'b' selon la première composante du tuple, c'est-à-dire par la différence croissante.
# La fonction clé lambda x:x[0] signifie qu'on trie selon la première valeur (l'écart).
b.sort(key=lambda x: x[0])

# On va maintenant procéder à une série de conditions complexes pour choisir quel calcul réaliser et afficher.
# Rappel : la liste 'b' est maintenant triée par différence croissante.
# b[0][0] est donc la plus petite différence entre deux éléments consécutifs,
# b[0][1] est l'indice du début de cette paire ayant la plus petite différence.

# Si l'indice de la plus petite différence est strictement inférieur à n-2 (c'est-à-dire qu'il n'est pas tout à la fin)
if b[0][1] < n - 2:
    # On affiche le résultat du calcul suivant :
    # somme des deux plus grands éléments (a[-1] et a[-2]), divisée par la plus petite différence (b[0][0]).
    # a[-1] est le plus grand, a[-2] le deuxième plus grand car a est triée
    print((a[-1] + a[-2]) / b[0][0])
# Sinon, si l'indice de la plus petite différence est exactement égal à n-3 (donc tout près de la fin)
elif b[0][1] == n - 3:
    # On regarde si la DEUXIÈME plus petite différence de 'b' (b[1][1]) est exactement à la fin (n-2)
    if b[1][1] == n - 2:
        # Dans ce cas, on effectue trois calculs différents et on prend le maximum :
        # 1. (a[-1] + a[-2]) / b[2][0] : somme des deux plus grands / troisième plus petite différence
        # 2. (a[-1] + a[-4]) / b[0][0] : somme du plus grand et du quatrième plus grand / plus petite différence
        # 3. (a[-3] + a[-4]) / b[1][0] : somme des troisième et quatrième plus grands / deuxième plus petite différence
        # On utilise max(...) pour choisir la valeur la plus grande parmi ces trois calculs
        print(max(
            (a[-1] + a[-2]) / b[2][0],
            (a[-1] + a[-4]) / b[0][0],
            (a[-3] + a[-4]) / b[1][0]
        ))
    else:
        # Sinon, on fait deux calculs possibles et on affiche le maximum :
        # 1. (a[-1] + a[-2]) / b[1][0] : somme des deux plus grands / deuxième plus petite différence
        # 2. (a[-1] + a[-4]) / b[0][0] : somme du plus grand et du quatrième plus grand / plus petite différence
        print(max(
            (a[-1] + a[-2]) / b[1][0],
            (a[-1] + a[-4]) / b[0][0]
        ))
# Si aucune des conditions précédentes n'est remplie (c'est-à-dire si b[0][1] > n-3)
else:
    # On vérifie si la deuxième plus petite différence dans 'b' est positionnée à l'avant-dernière place (n-3)
    if b[1][1] == n - 3:
        # On fait trois calculs et on en prend le maximum :
        # 1. (a[-1] + a[-2]) / b[2][0]
        # 2. (a[-1] + a[-4]) / b[1][0]
        # 3. (a[-3] + a[-4]) / b[0][0]
        print(max(
            (a[-1] + a[-2]) / b[2][0],
            (a[-1] + a[-4]) / b[1][0],
            (a[-3] + a[-4]) / b[0][0]
        ))
    else:
        # Dernier cas : on calcule seulement deux possibilités et on prend le maximum :
        # 1. (a[-1] + a[-2]) / b[1][0]
        # 2. (a[-3] + a[-4]) / b[0][0]
        print(max(
            (a[-1] + a[-2]) / b[1][0],
            (a[-3] + a[-4]) / b[0][0]
        ))