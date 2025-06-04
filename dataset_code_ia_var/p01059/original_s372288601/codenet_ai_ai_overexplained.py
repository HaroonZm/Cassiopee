# On commence par demander à l'utilisateur d'entrer deux entiers séparés par un espace via l'entrée standard.
# La fonction input() lit une ligne depuis l'entrée, puis split() sépare cette ligne en une liste de chaînes de caractères selon les espaces.
# map(int, ...) applique la fonction int à chaque élément de la liste obtenue, transformant ainsi chaque chaîne de caractères en entier.
# Enfin, on initialise les variables n et m avec les deux premiers entiers lus.
n, m = map(int, input().split())

# On crée une liste 'lst' comprenant 'n' éléments.
# On utilise une list comprehension : [100000 for _ in range(n)], cela veut dire qu'on répète 100000, n fois pour initialiser tous les éléments à 100000.
# Le caractère '_' est une convention pour dire que nous n'avons pas besoin de la variable de boucle (on ne s'en sert pas).
lst = [100000 for _ in range(n)]

# On lit la deuxième ligne de l'entrée qui contient m entiers séparés par des espaces.
# input().split() sépare l'entrée en liste de chaînes, map(int, ...) applique int à chaque pour obtenir une liste d'entiers.
# On transforme le résultat de map en liste grâce à list(), ce qui donne a_lst, une liste de m entiers.
a_lst = list(map(int, input().split()))

# Pour chaque élément 'a' de la liste d'entiers 'a_lst', on fait :
for a in a_lst:
    # On affecte la valeur 0 à l'élément d'indice (a - 1) dans la liste lst.
    # Cela veut dire que l'élément à la position 'a' (mais comme les listes Python commencent à l'indice 0, on soustrait 1) devient 0.
    # On fait ça sans vérifier si l'indice est déjà à 0, puisqu'on veut juste écraser la valeur précédente.
    lst[a - 1] = 0

# On traverse ensuite la liste lst de gauche à droite pour 'propager' les valeurs 0 sur la droite.
# On utilise une boucle for avec range(n - 1), ce qui donne les indices de 0 à n-2 inclus.
for i in range(n - 1):
    # Pour chaque position, on compare la valeur à l'indice i+1, avec lst[i] + 1.
    # Cela correspond à vérifier s'il vaut mieux garder la valeur actuelle ou utiliser la valeur de gauche +1.
    # min(lst[i] + 1, lst[i + 1]) prend la valeur la plus petite entre les deux.
    # On affecte le résultat à lst[i + 1], donc on peut possiblement réduire la valeur de lst[i + 1] si une valeur de gauche est plus petite.
    lst[i + 1] = min(lst[i] + 1, lst[i + 1])

# On fait une opération similaire mais de droite à gauche pour assurer que la propagation se fait bien dans les deux sens.
# range(n - 1, 0, -1) parcourt les indices de n-1 à 1 inclus, en décrémentant de 1 à chaque itération.
for i in range(n - 1, 0, -1):
    # Pour chaque position, on compare la valeur à l'indice i-1 avec lst[i] + 1.
    # Encore une fois, on choisit la valeur la plus petite entre la valeur actuelle ou la valeur de droite +1.
    # On met à jour la valeur de lst[i - 1] selon le minimum choisi.
    lst[i - 1] = min(lst[i - 1], lst[i] + 1)

# A la fin, on veut afficher la valeur maximale dans la liste lst après les deux passages de propagation.
# On utilise la fonction max(lst) pour obtenir la plus grande valeur présente dans la liste.
print(max(lst))