# Demande à l'utilisateur de saisir une ligne de texte via la fonction input().
# Cette saisie utilisateur est attendue sous la forme de deux nombres entiers séparés par un espace, par exemple : "3 4"
# Ensuite, la méthode split() est utilisée sur la chaîne obtenue pour diviser la chaîne à chaque fois qu'il y a un espace.
# Cela retourne une liste de sous-chaînes, dans cet exemple ['3', '4'].
# La fonction map() est ensuite utilisée pour appliquer la fonction int à chaque élément de la liste.
# map(int, ...) va transformer chaque chaîne de caractère en entier.
# Enfin, on utilise l'affectation multiple pour stocker ces deux entiers respectivement dans les variables A et B.
A, B = map(int, input().split())

# On effectue la multiplication des deux nombres entiers : A et B.
# L'opérateur '*' en Python sert à multiplier deux valeurs numériques.
# On utilise la fonction print() pour afficher le résultat de cette multiplication à l'écran.
print(A * B)