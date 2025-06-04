# Définition d'une fonction nommée LCM qui prend deux arguments, x et y.
def LCM(x, y):
    # set1 est un ensemble qui contient tous les multiples de x.
    # range(x, x*y+1, x) crée une séquence débutant à x,
    # finissant à x*y inclus, et en incrémentant de x à chaque fois.
    # Exemple : si x=2, y=3, on a range(2, 7, 2) soit [2, 4, 6].
    set1 = set(range(x, x*y+1, x))
    
    # set2 est un ensemble qui contient tous les multiples de y,
    # selon le même principe que ci-dessus mais avec un pas de y.
    set2 = set(range(y, x*y+1, y))
    
    # set3 est l'intersection des ensembles set1 et set2.
    # L'opérateur "&" donne les éléments communs à set1 et set2, c'est-à-dire les entiers
    # compris entre x et x*y qui sont multiples à la fois de x et de y.
    set3 = set1 & set2
    
    # Nous retournons la plus petite valeur de set3, ce qui correspond
    # au plus petit entier qui est divisible par x ET y à la fois (PPCM).
    return min(set3)

# On lit une ligne de l'entrée standard (input) contenant des valeurs séparées par un espace.
# Par exemple : "3 4"
# La méthode split() sépare la chaîne en liste ["3", "4"].
# La fonction map(int, ...) applique la conversion en entier à chaque élément de la liste,
# ce qui donne les entiers a et b.
a, b = map(int, input().split())

# On appelle la fonction LCM avec les arguments a et b, ce qui donne leur PPCM,
# puis on affiche le résultat obtenu avec la fonction print.
print(LCM(a, b))