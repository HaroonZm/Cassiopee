# Demande à l'utilisateur d'entrer une saisie clavier. La fonction `input()` affiche une invite et attend que l'utilisateur tape des valeurs, puis appuie sur 'Entrée'.
# La chaîne de caractères entrée est ensuite traitée par la méthode `split()`, qui sépare la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut.
# Par exemple, si l'utilisateur saisit "5 6", `input().split()` retournera la liste ['5', '6'].
# La fonction `map()` applique ensuite la fonction `int` à chaque élément de la liste pour convertir chaque sous-chaîne en entier.
# Cela donne un itérable de deux entiers, par exemple : 5 et 6.
# Enfin, par affectation multiple, les deux entiers sont respectivement stockés dans les variables `a` et `b`.
a, b = map(int, input().split())

# Condition 'if' : on vérifie si la variable `a` est strictement inférieure à la variable `b`.
# L'opérateur `<` compare les deux valeurs. Si la condition est vraie, le bloc d'instructions qui suit est exécuté.
if a < b:
    # La fonction `print()` affiche le texte fourni entre parenthèses à l'écran.
    # Ici, on affiche "a < b" pour indiquer que la variable `a` est inférieure à la variable `b`.
    print("a < b")
# 'elif' signifie 'else if' (sinon si) : cette condition n'est vérifiée que si la précédente était fausse.
# On vérifie ici si `a` est strictement supérieur à `b` à l'aide de l'opérateur '>'.
elif a > b:
    # Si `a` est supérieur à `b`, on affiche "a > b" pour l'indiquer.
    print("a > b")
# 'else' (sinon) : ce bloc s'exécute uniquement si toutes les conditions précédentes ont échoué,
# c'est-à-dire ici si `a` n'est ni inférieur ni supérieur à `b` (donc si `a` est égal à `b`).
else:
    # On affiche "a == b" pour signifier que la variable `a` est égale à la variable `b`.
    # Le double signe égal `==` est l'opérateur de comparaison d'égalité ; ici, il fait simplement partie du texte affiché.
    print("a == b")