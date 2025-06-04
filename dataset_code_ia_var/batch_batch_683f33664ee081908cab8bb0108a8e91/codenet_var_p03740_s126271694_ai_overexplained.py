# Demande à l'utilisateur d'entrer deux nombres séparés par un espace.
# La fonction input() affiche une invite (vide ici) et attend que l'utilisateur entre une ligne de texte.
# L'utilisateur doit saisir deux valeurs entières séparées par un espace, par exemple : 3 4

# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut.
# Par exemple, si l'utilisateur entre "3 4", split() retourne la liste ["3", "4"].

# La fonction map() applique la fonction spécifiée, ici 'int' (pour convertir en entier), à chaque élément de la liste obtenue par split().
# Cela retourne un itérable de deux entiers.

# L'affectation multiple "x, y = ..." attribue le premier entier à x et le second à y.

x, y = map(int, input().split())

# Calculons la valeur absolue de la différence entre x et y.
# La fonction abs() retourne toujours un nombre positif (la valeur absolue d'un nombre).
# abs(x-y) est la distance entre x et y sur la droite des entiers.

# Nous vérifions si cette distance est inférieure ou égale à 1, c'est-à-dire si x et y sont identiques ou consécutifs.
# L'opérateur <= signifie "inférieur ou égal à".

if abs(x - y) <= 1:
    # Si la condition est vraie (la différence entre x et y vaut 0 ou 1), alors on exécute ce bloc.
    # La fonction print() permet d'afficher du texte à l'écran.
    # On affiche la chaîne de caractères "Brown".
    print("Brown")
else:
    # Si la condition du if n'est pas vérifiée (la différence absolue est supérieure ou égale à 2), on exécute ce bloc.
    # On affiche la chaîne de caractères "Alice".
    print("Alice")