# Demande à l'utilisateur d'entrer trois entiers séparés par des espaces
# Ces trois entiers servent à initialiser les variables n, a et b respectivement
# La fonction input() lit la ligne de texte entrée par l'utilisateur
# La méthode split() découpe cette ligne en une liste de chaînes de caractères selon les espaces
# La fonction map(int, ...) applique la conversion en entier à chaque morceau issu du split()
# Les valeurs sont ensuite attribuées respectivement à n, a, b par l'affectation multiple
n, a, b = map(int, input().split())

# Demande à l'utilisateur d'entrer une autre ligne d'entiers séparés par des espaces
# Ces entiers sont censés constituer la liste principale sur laquelle opérer
# Comme précédemment, map(int, ...) convertit chaque valeur saisie en entier
# La fonction list(...) transforme l'objet map obtenu en véritable liste Python assignée à la variable arr
arr = list(map(int, input().split()))

# Vérifie si le nombre d'éléments désigné par n est égal à 1
# En d'autres termes, on s'interroge si la liste contient un seul élément
if n == 1:
    # Si la condition précédente est vraie, c'est-à-dire qu'il n'y a qu'un seul élément dans la liste arr
    # La valeur absolue de la différence entre l'unique élément arr[0] et la variable b est calculée
    # La fonction abs(...) retourne toujours une valeur positive (ou nulle)
    # Enfin, la fonction print(...) affiche cette valeur unique calculée sur la sortie standard (l'écran)
    print(abs(arr[0] - b))
else:
    # Si la liste contient plus d'un élément (n > 1), alors on entre ici
    # On souhaite calculer deux différences absolues pour déterminer laquelle est la plus grande
    # Première valeur : abs(arr[-1] - b)
    #    arr[-1] représente le dernier élément de la liste arr (syntaxe des indices négatifs en Python)
    #    On soustrait b de cet élément et abs(...) prend la valeur absolue du résultat
    # Deuxième valeur : abs(arr[-1] - arr[-2])
    #    arr[-2] est l'avant-dernier élément de la liste arr
    #    On fait la différence entre le dernier et l'avant-dernier élément (puis valeur absolue)
    # La fonction max(...) compare les deux valeurs calculées et retient la plus grande
    # print(...) affiche ce maximum à l'écran
    print(max(abs(arr[-1] - b), abs(arr[-1] - arr[-2])))