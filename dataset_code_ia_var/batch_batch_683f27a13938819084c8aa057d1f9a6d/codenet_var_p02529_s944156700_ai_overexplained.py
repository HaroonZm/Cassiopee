# Demande à l'utilisateur de saisir une entrée au clavier.
# Ici, la méthode raw_input() lit une ligne de texte depuis l'utilisateur (sous forme de chaîne de caractères).
n = raw_input()

# Après avoir reçu une ligne de texte, cet appel à raw_input() récupère une chaîne,
# qui représente des nombres séparés par des espaces.
# La méthode split() découpe cette chaîne à chaque espace et crée une liste de sous-chaînes,
# chacune représentant un nombre sous forme de texte.
# La compréhension de liste parcourt chaque sous-chaîne (x),
# et int(x) convertit chaque sous-chaîne en un entier (nombre entier),
# stockant tous les entiers dans la liste l1.
l1 = [int(x) for x in raw_input().split()]

# On redemande une saisie à l'utilisateur avec raw_input().
# Cette entrée est stockée dans la même variable n, écrasant l'ancien contenu.
n = raw_input()

# On appelle encore raw_input() pour lire une autre ligne d'entrée utilisateur.
# Cette ligne doit également contenir des entiers séparés par des espaces.
# La compréhension de liste fonctionne de la même façon que pour l1,
# pour créer une nouvelle liste d'entiers à partir de la saisie de l'utilisateur.
# Cette liste n'est pas stockée directement dans une variable : elle est générée à la volée.
# On convertit l1 en set (ensemble), ce qui supprime les doublons et permet d'utiliser les opérations ensemblistes.
# On convertit également la deuxième liste d'entiers en set.
# Les ensembles Python permettent d'utiliser l'opérateur & qui calcule l'intersection :
# cela donne un nouveau set contenant seulement les éléments présents dans les deux ensembles.
# len() mesure le nombre d'éléments dans ce set résultat, c'est-à-dire le nombre d'éléments communs entre les deux listes initiales.
# Enfin, print affiche ce nombre à l'écran.
print len(set(l1) & set([int(y) for y in raw_input().split()]))