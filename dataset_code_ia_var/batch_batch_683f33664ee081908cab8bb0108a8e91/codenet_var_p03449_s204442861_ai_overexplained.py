# Demande à l'utilisateur de saisir un nombre entier.
# La fonction input() lit une ligne de texte que l'utilisateur entre au clavier.
# La fonction int() convertit ce texte en un nombre entier.
n = int(input())

# Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces.
# input() capture la ligne en tant que chaîne.
# split() divise la chaîne en une liste de sous-chaînes, séparées par des espaces.
# map(int, ...) convertit chaque sous-chaîne en entier.
# list(...) crée finalement une liste d'entiers à partir de la séquence obtenue.
a1 = list(map(int, input().split()))

# Même chose pour a2 : saisit une deuxième ligne de nombres et la convertit en liste d'entiers.
a2 = list(map(int, input().split()))

# Calcule la somme des éléments à partir du deuxième élément de a1 (en excluant le premier élément, donc de l'indice 1 à la fin).
# a1[1:] signifie 'tous les éléments de a1 à partir de l'indice 1 (inclus) jusqu'à la fin'.
# Calcule aussi la somme des éléments de a2 sauf le dernier élément (de l'indice 0 jusqu'à n-2).
# a2[:-1] signifie 'tous les éléments de a2 sauf le dernier'.
# min(x, y) retourne la plus petite des deux valeurs x et y.
mi = min(sum(a1[1:]), sum(a2[:-1]))

# Boucle for pour i allant de 2 (inclus) à n (exclu).
# range(2, n) produit les entiers 2, 3, ..., n-1 en séquence.
for i in range(2, n):
    # Calcule la somme des éléments de a1 à partir de l'indice i jusqu'à la fin.
    # a1[i:] correspond à 'tous les éléments de a1 à partir de l'indice i (inclus)'.
    # Calcule aussi la somme des éléments de a2 du début jusqu'à l'indice i-2 inclus.
    # a2[:i-1] signifie 'tous les éléments de a2 du début jusqu'à l'indice i-2 inclus'.
    tmp = sum(a1[i:]) + sum(a2[:i-1])
    # Compare la valeur tmp avec mi, et retient la plus petite des deux dans mi.
    mi = min(tmp, mi)

# Calcule la somme totale des éléments de a1 et de a2.
# Puis, soustrait à ce total la plus petite valeur de mi trouvée précédemment.
# Affiche le résultat final à l'aide de print().
print(sum(a1) + sum(a2) - mi)