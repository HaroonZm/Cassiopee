# On utilise la fonction open(0) pour ouvrir l'entrée standard (stdin)
# On lit tout le contenu de l'entrée standard comme une seule chaîne de caractères avec .read()
# La méthode .split() découpe la chaîne lue en une liste de sous-chaînes (chaînes), en séparant selon les espaces ou les retours à la ligne.
# La fonction map() applique la fonction int à chaque élément de la liste obtenue, transformant donc chaque sous-chaîne numérique en entier.
# On affecte le résultat du unpacking:
# - n reçoit le premier entier (typiquement, il s'agit d'un compteur ou d'une taille, dépendant du contexte)
# - a reçoit le deuxième entier (représente une borne inférieure, exclusive)
# - b reçoit le troisième entier (représente une borne supérieure, inclusive)
# - *s capture tous les entiers restants dans une liste (cela permet de manipuler une séquence de valeurs de façon souple)

n, a, b, *s = map(int, open(0).read().split())

# On utilise la fonction sum() pour additionner le résultat de l'expression pour chaque élément de s.
# L'expression à l'intérieur de sum() est un générateur de booléens:
# - for t in s : on parcourt chaque entier t de la liste s.
# - (t < a or b <= t) : on vérifie si t est strictement inférieur à a (c'est-à-dire que t n'atteint pas a)
#    ou si t est supérieur ou égal à b.
#   - L'opérateur "or" signifie que si au moins une des deux conditions est vraie, l'expression globale est vraie.
# - En Python, True vaut 1 et False vaut 0 lorsqu'on les additionne.
# On obtient donc, pour chaque t de s, 1 si t hors de l'intervalle [a, b), et 0 sinon.
# sum(...) renvoie alors le nombre total d'éléments de s qui sont hors de cet intervalle.
# Enfin, print() affiche ce nombre à la sortie.

print(sum((t < a or b <= t) for t in s))