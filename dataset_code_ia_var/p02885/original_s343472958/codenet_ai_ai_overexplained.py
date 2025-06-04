# Demander à l'utilisateur d'entrer deux entiers séparés par un espace sur une seule ligne.
# Utiliser input() pour lire la ligne de texte saisie par l'utilisateur.
# input() renvoie une chaîne de caractères.
# Passer cette chaîne à la fonction split(), qui découpe la chaîne en une liste de sous-chaînes (ici deux) en se basant sur les espaces.
# map(int, ...) applique la fonction int à chaque élément de cette liste, convertissant ainsi les deux sous-chaînes en entiers.
# Les deux entiers sont alors affectés respectivement aux variables a et b grâce à l'affectation multiple.
a, b = map(int, input().split())

# Calculer la valeur de (a - (2 * b)).
# (2 * b) signifie que l'on multiplie b par 2 avant de le soustraire à a.
# On vérifie si le résultat de ce calcul est inférieur à 0.
if (a - (2 * b) < 0):
    # Ce bloc de code ne sera exécuté que si l'expression ci-dessus est vraie, c'est-à-dire si a - 2b est négatif.
    # Dans ce cas, afficher 0 en utilisant la fonction print().
    print(0)
else:
    # Ce bloc de code else sera exécuté si la condition du if (a - 2b < 0) est fausse.
    # Cela signifie que a - 2b est supérieur ou égal à 0.
    # Afficher la valeur calculée de (a - 2b) avec print().
    print(a - (2 * b))