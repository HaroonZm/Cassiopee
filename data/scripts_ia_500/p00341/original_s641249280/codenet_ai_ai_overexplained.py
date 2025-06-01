# On commence par lire une ligne de texte entrée par l'utilisateur via la fonction input().
# Cette fonction input() capture tout ce que l'utilisateur tape au clavier jusqu'à appuyer sur Entrée,
# et renvoie cette saisie sous forme d'une chaîne de caractères (un string).
# Ensuite, on utilise la méthode split() sur cette chaîne, sans argument, ce qui fait que la chaîne est découpée
# selon les espaces présents. Cela produit une liste de sous-chaînes de caractères indépendantes.
# Chaque élément de cette liste est supposé représenter un nombre entier sous forme de string.
# La fonction map() permet d'appliquer une fonction à chaque élément d'un itérable.
# Ici, on applique int pour convertir chaque chaîne en un entier.
# Le résultat de map(int, ...) est un itérable qui contient maintenant les entiers correspondants.
# Enfin, la fonction sorted() trie cet itérable et retourne une liste triée.
# On assigne cette liste triée à la variable e.
e = sorted(map(int, input().split()))

# On souhaite maintenant vérifier une condition précise basée sur les valeurs contenues dans la liste triée e.
# Pour cela, on travaille sur trois tranches (sous-listes) de la liste e:
# - Les quatre premiers éléments e[:4] (indices 0 à 3 inclus),
# - Les quatre éléments suivants e[4:8] (indices 4 à 7 inclus),
# - Et les éléments suivants e[8:] (à partir de l'indice 8 jusqu'à la fin).
# La fonction set() transforme une liste en un ensemble, c'est-à-dire une collection
# d'éléments uniques, sans doublons.
# En mesurant la longueur len(set(...)) d’une tranche, on obtient le nombre d’éléments distincts dans cette tranche.
# La condition vérifie que chacune de ces trois tranches a exactement un élément unique,
# ce qui signifie que tous les éléments dans chaque sous-liste sont identiques.
# Le test d'égalité chaîné len(set(e[:4])) == len(set(e[4:8])) == len(set(e[8:])) == 1
# vérifie que ces trois longueurs sont égales à 1 simultanément.
# Si cette condition est vraie, on affiche "yes".
# Sinon, on affiche "no".
# Cette instruction est écrite avec une expression conditionnelle ternaire en Python.
print("yes" if len(set(e[:4])) == len(set(e[4:8])) == len(set(e[8:])) == 1 else "no")