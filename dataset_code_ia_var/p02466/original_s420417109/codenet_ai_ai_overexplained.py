# Demande l'entrée de l'utilisateur. Cette ligne attend simplement une entrée de l'utilisateur,
# mais la valeur saisie n'est pas assignée ou utilisée, probablement parce qu'on veut sauter une ligne
# qui pourrait contenir le nombre d'éléments d'un ensemble (usuel dans certains problèmes).
input()

# Prend une ligne de saisie de l'utilisateur, la divise en sous-chaînes là où il y a des espaces,
# convertit chaque sous-chaîne en entier, puis ajoute chaque entier à un ensemble.
# Cela produit un ensemble 'A' contenant tous les entiers uniques de la ligne saisie.
A = set(int(x) for x in input().split())

# De nouveau, demande une entrée de l'utilisateur (pour ignorer une éventuelle ligne avec une taille d'ensemble).
input()

# Prend une autre ligne de l'utilisateur, la divise en sous-chaînes par espace,
# convertit chaque sous-chaîne en entier, puis construit un ensemble 'B' d'entiers uniques.
B = set(int(x) for x in input().split())

# Calcule les éléments qui sont dans l'un ou l'autre ensemble, mais pas dans les deux.
# (A | B) est l'union des ensembles A et B : cela donne un ensemble de tous les éléments présents dans A ou dans B.
# (A & B) est l'intersection : les éléments présents à la fois dans A et B.
# (A | B) - (A & B) retire de l'union les éléments communs (présents dans l'intersection), 
# ce qui aboutit à l'ensemble des éléments qui n'appartiennent qu'à un seul ensemble (la différence symétrique).
# Ensuite, on trie ces éléments pour les afficher dans l'ordre croissant,
# car l'affichage d'un ensemble n'est pas ordonné par défaut.

for i in sorted((A | B) - (A & B)):
    # Affiche chaque entier de la différence symétrique, un par ligne.
    print(i)