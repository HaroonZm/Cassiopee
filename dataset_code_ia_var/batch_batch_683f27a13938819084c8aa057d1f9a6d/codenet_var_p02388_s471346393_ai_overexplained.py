# Demande à l'utilisateur d'entrer une valeur via la console.
# La fonction input() arrête l'exécution du programme et attend que l'utilisateur tape quelque chose.
# Le texte tapé est ensuite renvoyé sous forme de chaîne de caractères (str) et stocké dans la variable x.
x = input()

# Comme la valeur récupérée par input() est une chaîne de caractères (et non un nombre),
# il faut la convertir en un entier pour pouvoir effectuer une opération mathématique comme l'exponentiation.
# La fonction int() convertit la chaîne de caractères en un nombre entier.
# Si l'entrée n'est pas un nombre valide, cela provoquera une erreur.
x = int(x)

# Calcule le cube de x. L’opérateur ** en Python sert à réaliser une exponentiation.
# x**3 signifie "x à la puissance 3", c’est-à-dire multiplier x par lui-même trois fois (x * x * x).
# On place cette opération à l’intérieur de la fonction print()
# pour afficher directement le résultat à l’écran.
print(x ** 3)