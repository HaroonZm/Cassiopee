# Demande à l'utilisateur d'entrer une valeur, puis convertit cette valeur (habituellement une chaîne de caractères) en un entier (type int).
# La fonction input() attend que l'utilisateur tape quelque chose puis appuie sur "Entrée". int() convertit la chaîne en nombre entier.
i = int(input())

# Initialise une variable 's' à 0. Cette variable servira à stocker la somme totale résultante à calculer plus tard.
s = 0

# Calcule combien de fois 500 rentre dans 'i' sans dépasser. L'opérateur // effectue une division entière,
# c'est-à-dire qu'il donne combien de fois le diviseur tient dans le dividende, sans prendre la partie décimale.
x = i // 500

# Multiplie 'x' (le nombre de fois où 500 rentre dans 'i') par 1000, puis ajoute ce résultat à 's'.
# Cela correspond à donner 1000 pour chaque "billet" de 500 extrait.
s += x * 1000

# Met à jour la valeur de 'i' en lui affectant son reste après division par 500.
# L'opérateur % donne le reste de la division entière (appelé aussi modulo).
i = i % 500

# Calcule combien de fois 5 rentre dans le reste de 'i' (après avoir retiré tous les multiples de 500).
# Encore une fois, // effectue une division entière.
x = i // 5

# Multiplie 'x' (le nombre de fois où 5 rentre dans le reste de 'i') par 5, puis ajoute ce résultat à 's'.
# Ceci équivaut à donner 5 pour chaque "billet" de 5 extrait du reste.
s += x * 5

# Affiche le résultat final stocké dans 's' à l'utilisateur.
# La fonction print() affiche des données à l'écran.
print(s)