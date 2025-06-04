# Demander à l'utilisateur de saisir une première ligne de texte et stocker cette valeur dans la variable s1.
# La fonction input() lit une chaîne entrée par l'utilisateur à partir de la console.
s1 = input()

# Demander à l'utilisateur de saisir une seconde ligne de texte et stocker cette valeur dans la variable s2.
s2 = input()

# Utiliser une compréhension de liste pour convertir chaque sous-chaîne obtenue par la méthode split()
# sur la chaîne s1 (ce qui découpe la chaîne en morceaux séparés par des espaces)
# en un entier en utilisant int().
# Ensuite, on “dépaquette” la liste résultante en trois variables x, y et z.
x, y, z = [int(i) for i in s1.split()]

# De façon similaire, on découpe la chaîne s2 en sous-chaînes à chaque espace,
# puis on convertit chaque sous-chaîne en entier avec int(), stockant le tout dans une liste l.
l = [int(i) for i in s2.split()]

# Vérifier si la valeur de x est exactement égale à 1.
if x == 1:
    # Si la condition précédente est vraie, alors on exécute ce qui suit.
    # Prendre la valeur d’indice x-1 dans la liste l. 
    # Puis, soustraire cette valeur de z, puis calculer la valeur absolue de la différence avec abs().
    # Ceci correspond à comparer l’élément d’indice 0 (car x-1 lorsque x=1 donne 0) de la liste l à z.
    # Ensuite, afficher le résultat à l’écran avec print().
    print(abs(z - l[x-1]))
else:
    # Si x n’est pas égal à 1 (c’est-à-dire si x>1), alors ce bloc s’exécute.
    # D’abord, calculer abs(z - l[x-1]) qui est la valeur absolue de la différence entre z et l’élément d’indice x-1 dans la liste l.
    # Ensuite, calculer abs(l[x-1] - l[x-2]) qui est la valeur absolue de la différence entre deux éléments consécutifs dans la liste l.
    # Ensuite, vérifier si la première quantité (abs(z - l[x-1])) est strictement plus grande que la seconde (abs(l[x-1] - l[x-2])).
    if abs(z - l[x-1]) > abs(l[x-1] - l[x-2]):
        # Si la condition précédente est vraie, alors on affiche la première quantité calculée.
        print(abs(z - l[x-1]))
    else:
        # Sinon (c'est-à-dire si la première quantité est inférieure ou égale à la seconde),
        # on affiche la seconde quantité.
        print(abs(l[x-1] - l[x-2]))