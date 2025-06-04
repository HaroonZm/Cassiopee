# Demande à l'utilisateur de saisir deux nombres séparés par un espace sur une seule ligne.
# La fonction `input()` lit la ligne de texte saisie par l'utilisateur sous la forme d'une chaîne de caractères.
# La méthode `split()` découpe cette chaîne à chaque espace et retourne une liste contenant chaque morceau sous forme de chaînes.
# La fonction `map(int, ...)` applique la fonction `int` à chacun des éléments de la liste obtenue,
# transformant ainsi chaque élément sous forme de chaîne en nombre entier.
# Les deux valeurs ainsi extraites sont ensuite affectées aux variables `x` et `y` respectivement.
x, y = map(int, input().split())

# La fonction `abs()` calcule la valeur absolue de la différence entre `x` et `y`.
# L'opérateur de comparaison `>` teste si cette valeur absolue est strictement supérieure à 1.
# Cette condition renvoie un résultat booléen : `True` si c'est le cas, `False` sinon.
# L'expression conditionnelle (ternaire) `"Alice" if ... else "Brown"` évalue cette condition.
# Si la condition est vraie (`True`), c'est la chaîne `"Alice"` qui sera utilisée en sortie.
# Sinon (condition fausse, `False`), c'est la chaîne `"Brown"` qui sera utilisée.
# La fonction `print()` affiche la chaîne résultante à l'écran.
print("Alice" if abs(x - y) > 1 else "Brown")