# Demande à l'utilisateur de saisir une ligne de texte contenant trois valeurs séparées par des espaces. 
# La fonction input() affiche l'invite de commande (vide ici) et attend que l'utilisateur saisisse des données, puis appuie sur "Entrée".
# La chaîne saisie par l'utilisateur est transmise à la fonction split() qui, sans argument, divise la chaîne selon les espaces et retourne une liste de sous-chaînes.
# Par exemple, si l'utilisateur entre "3 4 5", split() retournera ['3', '4', '5'].
# La fonction map() applique la fonction int à chaque élément de cette liste, convertissant les sous-chaînes en entiers.
# map(int, ...) retourne donc un itérable contenant des entiers, ici correspondant à a, b, c.
# Les trois entiers sont assignés respectivement aux variables a, b, et c grâce à l'affectation multiple.

a, b, c = map(int, input().split())

# On effectue ensuite le calcul demandé :
# a * b calcule le produit de a et b. Cela donne un entier.
# // est l'opérateur de division entière. Il divise le résultat du produit (a * b) par 2
# et retourne le quotient sans la partie décimale. Ainsi, 7 // 2 donnerait 3.
# print() est une fonction intégrée qui affiche la valeur passée en argument sur la sortie standard (habituellement l'écran).
# Ici, on affiche donc le résultat de (a * b) // 2.

print(a * b // 2)