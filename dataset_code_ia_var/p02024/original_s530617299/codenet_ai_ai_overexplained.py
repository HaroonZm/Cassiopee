# On demande à l'utilisateur d'entrer quatre nombres entiers séparés par des espaces
# Ces quatre valeurs vont correspondre à :
# h : la hauteur d'une certaine entité (par exemple un tableau ou une grille)
# w : la largeur de cette entité
# x : une coordonnée x (généralement une colonne)
# y : une coordonnée y (généralement une ligne)
# La fonction input() lit une ligne au clavier, au format texte (string)
# La fonction split() découpe cette chaîne selon les espaces et renvoie une liste de chaînes
# La fonction map(int, ...) va convertir chaque élément de cette liste textuelle en un entier
# Enfin, l'affectation multiple permet d'attribuer chaque valeur entière aux variables respectives
h, w, x, y = map(int, input().split())

# L'expression h * w calcule l'aire ou le nombre total de cases, par multiplication de la hauteur et de la largeur
# h * w % 2 calcule le reste de la division entière de cette aire par 2, ce qui renseigne sur la parité :
# - Si le résultat est 0 : produit pair
# - Si le résultat est 1 : produit impair
# La même idée s'applique pour (x + y) % 2, qui indique la parité de la somme des indices x et y
#
# L'opérateur "and" en Python évalue à True si les deux conditions sont vraies simultanément
# La liste ["Yes", "No"] contient deux éléments : "Yes", accessible à l'indice 0, et "No" à l'indice 1
#
# L'expression [h * w % 2 == 1 and (x + y) % 2 == 1] sera True si les deux conditions sont vraies
# En Python, l'expression booléenne True équivaut à 1 et False à 0 si utilisée comme indice dans une liste
# Donc, si la condition renvoie True (c-à-d. à la fois une aire impaire et une somme d'indices impaire), "No" sera affiché
# Sinon, "Yes" sera affiché
print(["Yes", "No"][h * w % 2 == 1 and (x + y) % 2 == 1])