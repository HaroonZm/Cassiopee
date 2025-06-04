# Création d'un dictionnaire vide. Un dictionnaire (dict) est une structure de données associant des clés à des valeurs.
d = {}

# Demande à l'utilisateur d'entrer une valeur. input() lit une ligne depuis l'entrée standard.
# int() convertit la chaîne obtenue en entier.
# [0] * nombre, crée une liste dont les éléments sont tous 0 et de longueur égale à la valeur saisie.
# for _ in ... sert à répéter la boucle autant de fois que le nombre saisi, le _ indique que la variable n'est pas utilisée.
for _ in [0] * int(input()):
    # input() lit une ligne de texte entrée par l'utilisateur.
    # split() coupe la chaîne en deux parties à chaque espace, et affecte respectivement la première à k et la deuxième à v.
    k, v = input().split()
    # d.get(k, 0) récupère la valeur associée à la clé k dans le dictionnaire d ; si k n'existe pas, cela renvoie 0.
    # int(v) convertit la chaîne v en entier.
    # On additionne la valeur courante avec la nouvelle entrée, puis on affecte le résultat à la clé k dans le dictionnaire d.
    d[k] = d.get(k, 0) + int(v)

# Création d'une liste de listes [[len(x), x] for x in d], c'est-à-dire une liste qui, pour chaque clé x, contient une sous-liste :
# [longueur de la clé, la clé elle-même].
# sorted() trie cette liste d'après les éléments ; par défaut, cela trie d'abord par longueur, puis, à égalité, trie par ordre alphabétique des clés.
for l, k in sorted([[len(x), x] for x in d]):
    # Affiche la clé k et la valeur correspondante d[k], séparées par un espace.
    print(k, d[k])