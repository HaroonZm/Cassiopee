# Demande à l'utilisateur de saisir trois entiers sur une seule ligne séparés par des espaces.
# La fonction input() lit la ligne de texte entrée par l'utilisateur comme une chaîne de caractères.
# La méthode split() sépare cette chaîne à chaque espace et renvoie une liste de chaînes correspondant aux nombres saisis.
# La fonction map() applique la conversion int() à chaque élément de cette liste de chaînes, transformant chaque chaîne en un entier.
# La fonction list() convertit le résultat de la fonction map en une liste de trois entiers.
# Enfin, on assigne simultanément les trois entiers aux variables A, B et C grâce à l'affectation multiple.
A, B, C = list(map(int, input().split()))

# Calcule la somme simple des trois variables A, B, et C en utilisant l'opérateur +.
# Le résultat est stocké dans la variable sum_l (l l'indique peut-être "length" ou une autre signification selon le contexte).
sum_l = A + B + C

# Utilise la fonction intégrée max() pour déterminer la plus grande valeur parmi les trois variables A, B et C.
# Le résultat, c’est-à-dire la plus grande des trois valeurs, est stocké dans la variable max_l.
max_l = max(A, B, C)

# Calcule la différence basée sur le triple de la plus grande valeur max_l moins la somme totale des trois valeurs sum_l.
# Cette différence est stockée dans la variable dif. Formule : dif = 3*max_l - sum_l
dif = 3 * max_l - sum_l

# On va maintenant déterminer combien d'opérations sont nécessaires selon si cette différence est paire ou impaire.
# Pour savoir si un nombre est pair, on utilise l'opérateur modulo %. Si le reste de la division de dif par 2 est égal à 0, alors le nombre est pair.
if dif % 2 == 0:
    # Si la différence est paire, on divise simplement dif par 2 avec l'opérateur de division entière // qui renvoie le quotient sans la partie décimale.
    # Cela permet d'obtenir le nombre minimal d'opérations requises selon la logique de l'algorithme.
    print(dif // 2)
else:
    # Si la différence est impaire (dif % 2 renvoie 1 donc l'instruction else est exécutée),
    # on effectue une division entière de dif par 2 (dif // 2), ce qui arrondit vers le bas,
    # puis on ajoute 2 au résultat. Cette opération tient probablement compte d'un ajustement nécessaire lié à la parité de dif.
    print((dif // 2) + 2)