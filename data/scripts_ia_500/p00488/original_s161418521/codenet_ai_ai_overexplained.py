# Demande à l'utilisateur d'entrer une valeur, convertit cette entrée en un nombre entier, répète cette opération 3 fois
# puis trouve le minimum (la plus petite valeur) parmi ces 3 nombres
# Ici, la fonction input() lit une chaîne de caractères saisie par l'utilisateur
# int() convertit cette chaîne de caractères en un entier numérique
# La boucle for _ in range(3) signifie que l'on répète l'opération 3 fois,
# le "_" est une variable temporaire ignorée car on n'a pas besoin de sa valeur
# l'expression (int(input()) for _ in range(3)) est un générateur qui produit 3 entiers
# min() calcule le plus petit entier produit par ce générateur
min_value_first_set = min(int(input()) for _ in range(3))

# Demande à l'utilisateur d'entrer une valeur, convertit cette entrée en un nombre entier, répète cette opération 2 fois
# puis trouve le minimum (la plus petite valeur) parmi ces 2 nombres
min_value_second_set = min(int(input()) for _ in range(2))

# Additionne les deux minimums trouvés précédemment
sum_min_values = min_value_first_set + min_value_second_set

# Soustrait 50 du résultat de l'addition précédente
final_result = sum_min_values - 50

# Affiche le résultat final à l'écran
print(final_result)