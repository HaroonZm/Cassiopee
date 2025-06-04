# Demander à l'utilisateur d'entrer un nombre et assigner la valeur à la variable n
# La fonction input() demande à l'utilisateur de saisir une entrée au clavier (en Python 2, input lit une expression Python)
# Cependant, pour obtenir un entier correctement, il est nécessaire de faire une conversion de type (cast)
n = input()  # En Python 2, input() évalue l'entrée comme du code, readline sinon ; on fait comme dans l'exemple

# Créer une liste 'a' à partir d'une compréhension de liste. Pour chaque 'i' dans l'intervalle 0 à n-1,
# raw_input() lit une ligne de texte de l'utilisateur,
# split() divise la chaîne en morceaux selon les espaces,
# map(int, ...) convertit chaque morceau texte en entier.
# Cependant, map() retourne un objet map (en Python 3) ou une liste(en Python 2), selon la version.
a = [map(int, raw_input().split()) for i in range(n)]  # Pour n lignes, stocke chaque paire (ou plus) d'entiers entrés par l'utilisateur

# Parcourir la plage d'indices de 0 jusqu'à n-1 dans la liste 'a', à l'aide d'une boucle for avec la variable 'i' comme compteur
for i in range(n):
    # Pour la i-ème sous-liste (ici supposément une liste de deux entiers),
    # effectuer une rotation de 90 degrés dans l'espace des coordonnées (x, y) → (-y, x)
    # Cela signifie que la première composante (abscisse) est remplacée par l'opposé de la deuxième,
    # et la deuxième composante (ordonnée) par la première valeur
    (a[i][0], a[i][1]) = (-a[i][1], a[i][0])

# Trier la liste 'a' à l'aide de la méthode sort(), qui trie la liste sur place.
# Par défaut, cela trie selon l'ordre lexicographique des sous-listes/tuples, c'est-à-dire d'abord selon le premier élément, 
# puis le deuxième en cas d'égalité, etc.
a.sort()

# Afficher le deuxième élément (index 1) de la première sous-liste (c'est-à-dire a[0][1]),
# puis l'opposé du premier élément (index 0) de cette même sous-liste, avec un espace entre les deux,
# en utilisant la syntaxe print qui sépare les arguments par un espace.
print a[0][1], -a[0][0]  # Cela affiche la nouvelle ordonnée, puis la nouvelle abscisse (rétablie du signe opposé)