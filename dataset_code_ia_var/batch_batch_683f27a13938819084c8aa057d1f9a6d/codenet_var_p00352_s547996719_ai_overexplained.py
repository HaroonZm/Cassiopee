# Nous commençons par demander à l'utilisateur de saisir deux nombres entiers, séparés par un espace
# La fonction `input()` affiche l'invite de saisie (par défaut vide) et attend que l'utilisateur tape une ligne de texte, puis appuie sur Entrée
# Le texte saisi par l'utilisateur est une chaîne de caractères (string) représentant les deux nombres ainsi que l'espace séparateur
# Par exemple, si l'utilisateur entre "4 6", alors input() retourne la chaîne "4 6"
# La méthode `split()` sépare cette chaîne de caractères en une liste de sous-chaînes, découpées là où il y a des espaces (par défaut)
# Par exemple, "4 6".split() retourne la liste ["4", "6"]
# Ensuite, on applique la fonction `map()` qui permet de transformer chaque élément de la liste
# Ici, on utilise `int` comme fonction de transformation pour obtenir deux entiers à partir des chaînes de caractères
# map(int, ["4", "6"]) produit un itérable contenant les entiers 4 et 6
# On utilise un unpacking (décomposition) avec a, b = ... pour assigner le premier entier à la variable a, et le second à la variable b
a, b = map(int, input().split())

# Maintenant, nous voulons calculer la moyenne arithmétique de ces deux nombres
# L'opérateur + additionne les deux nombres, donc (a + b) calcule leur somme
# On met la somme entre parenthèses pour s'assurer de l'ordre des opérations, même si la priorité de + est déjà inférieure à /
# On divise ensuite la somme par 2, ce qui calcule la moyenne
# L'opérateur / effectue une division flottante en Python, ce qui signifie que le résultat peut être un nombre à virgule flottante (float), même si a et b sont tous les deux des entiers
# Par exemple, si a = 5 et b = 6, alors (a + b) / 2 = 11 / 2 = 5.5
# Pour obtenir un entier, on entoure tout cela avec la fonction `int()`
# La fonction int() convertit la valeur passée en argument en entier, c'est-à-dire qu'elle tronque la partie décimale
# Par exemple, int(5.5) retourne 5, parce qu'il ne fait pas d'arrondi, il enlève tout ce qu'il y a après la virgule
# Enfin, on utilise la fonction `print()` pour afficher le résultat à l'écran afin que l'utilisateur puisse le voir
print(int((a + b) / 2))