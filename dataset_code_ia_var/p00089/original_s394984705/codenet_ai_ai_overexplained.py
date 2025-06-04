import sys  # Importe le module sys pour accéder à sys.stdin (entrée standard)

# Lis chaque ligne de l'entrée standard (sys.stdin), les sépare par lignes,
# puis pour chaque ligne, coupe la chaîne en morceaux séparés par une virgule,
# convertit chaque morceau en entier (avec int), emballe chaque ligne
# sous forme de liste d'entiers. Enfin, rassemble toutes ces listes dans une nouvelle liste s.
s = [
    list(
        map(
            int,      # Convertit chaque élément de la ligne (string) en entier
            e.split(',')  # Coupe la ligne en morceaux séparés par une virgule
        )
    )
    for e in sys.stdin  # Parcourt chaque ligne envoyée à l'entrée standard
]

# Parcourt chaque ligne 2 à n (donc à partir de l'indice 1, car l'indice 0 est la première), pour calculer cumulativement la valeur maximale
for i in range(1, len(s)):
    k = len(s[i])  # Stocke le nombre d'éléments (colonnes) dans la i-ème ligne

    # Parcourt chaque colonne j de la ligne courante
    for j in range(k):

        # Calcule un décalage t, afin d'aligner les index de la ligne précédente pour le calcul du max
        # Si k>len(s[i-1]), alors t = j-1, sinon t = j
        t = j - (k > len(s[i-1]))

        # (j>0) teste si la colonne n'est pas la première (indice 0) : True=1, False=0
        # Donc, si j>0, alors t*(j>0) = t, sinon 0.
        # t+2 fournit un "slice" qui prendra jusqu'à l'élément t+1 inclus (car upper bound exclue en Python).
        # max(...) calcule la valeur maximale dans la partie correspondante de la ligne précédente
        # On ajoute ce maximum à la valeur courante de la case s[i][j]
        s[i][j] += max(
            s[i-1][t * (j > 0): t + 2]  # Récupère une sous-liste adaptée pour le calcul
        )

# À la fin, après toutes les itérations, s[-1] est la dernière ligne, qui contient les résultats finaux
# *s[-1] déplie tous les éléments de la dernière ligne et les passe à print, donc ils seront affichés séparés par un espace
print(*s[-1])