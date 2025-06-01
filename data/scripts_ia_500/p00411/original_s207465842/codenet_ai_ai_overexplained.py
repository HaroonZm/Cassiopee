# Demande à l'utilisateur d'entrer une ligne de texte via la fonction input()
# input() retourne une chaîne de caractères (string) représentant ce que l'utilisateur a tapé au clavier
# Ici, on prévoit que l'utilisateur va entrer trois nombres entiers séparés par des espaces, par exemple: "4 5 6"
# Ensuite, on divise cette chaîne en plusieurs sous-chaînes en utilisant l'espace comme séparateur grâce à split(" ")
# Cela produit une liste de chaînes comme ["4", "5", "6"]
# Pour chaque élément de cette liste, on applique int(x) qui convertit la chaîne "x" en entier numérique
# La compréhension de liste [int(x) for x in input().split(" ")] génère donc une liste de trois entiers, par exemple [4, 5, 6]
# Enfin, on attribue ces trois entiers respectivement aux variables a, t, r, par affectation multiple
a, t, r = [int(x) for x in input().split(" ")]

# Calcul de l'expression (r / a) * t
# r / a fait une division flottante entre les valeurs entières r et a, produisant un nombre à virgule flottante
# Puis on multiplie ce résultat par t, un entier, ce qui donne une valeur finale flottante
# print() affiche ce résultat à l'écran sous forme de chaîne de caractères, convertit automatiquement le nombre en texte
print((r / a) * t)