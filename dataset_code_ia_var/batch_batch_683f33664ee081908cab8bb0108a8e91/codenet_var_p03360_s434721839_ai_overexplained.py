# Demande à l'utilisateur de saisir une ligne de texte contenant des nombres entiers séparés par des espaces.
# La fonction input() lit la saisie utilisateur sous forme de chaîne de caractères (string).
user_input = input()

# La méthode split() découpe cette chaîne en une liste de sous-chaînes (chaque sous-chaîne représentant un nombre).
# Si aucun argument n'est donné à split(), la séparation se fait sur les espaces par défaut.
user_input_split = user_input.split()

# La fonction map applique ici la fonction int à chaque élément de la liste.
# int convertit chaque sous-chaîne représentant un nombre en un entier (type int).
mapped_to_int = map(int, user_input_split)

# La fonction list prend un objet itérable (ici, le map) et le transforme en une liste d'entiers.
a = list(mapped_to_int)

# La fonction sorted prend la liste des entiers a et renvoie une nouvelle liste contenant les mêmes entiers, 
# mais triés dans l'ordre croissant (du plus petit au plus grand).
a = sorted(a)

# Demande à l'utilisateur de saisir un autre nombre, qui sera interprété comme la variable k.
# input lit une chaîne de caractères que l'on convertit ensuite en entier avec int() pour obtenir une valeur entière.
k_input = input()
k = int(k_input)

# On veut modifier le plus grand élément de la liste a. 
# Puisque sorted() retourne une liste triée du plus petit au plus grand, 
# le dernier élément de la liste (d'indice -1) est le plus grand.
# On remplace cet élément par la valeur du plus grand élément multiplié par 2 puissance k.
# L'opérateur ** sert à élever un nombre à la puissance k : 2**k signifie 2^k.
a[-1] = (2 ** k) * a[-1]

# La fonction sum() additionne tous les éléments de la liste a et retourne leur somme.
result = sum(a)

# Enfin, on affiche le résultat à l'écran grâce à la fonction print.
print(result)