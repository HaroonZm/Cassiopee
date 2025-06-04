# Demande à l'utilisateur de saisir une valeur via le clavier
# La fonction input() affiche un champ de saisie et récupère le texte entré par l'utilisateur sous forme de chaîne de caractères (str)
# int() convertit la chaîne de caractères obtenue en un nombre entier (int)
a = int(input())

# Calcule le tiers (1/3) de la valeur entière saisie et stocke ce résultat dans la variable b
# L'opérateur '/' effectue une division flottante (retourne un float même si les deux opérandes sont des entiers)
b = a / 3

# Calcule la puissance de b élevé à 3 (c'est-à-dire b multiplié par lui-même deux fois : b * b * b, soit b^3)
# L'opérateur '**' est utilisé pour l'exponentiation en Python
resultat = b ** 3

# Affiche le résultat du calcul précédent
# La fonction print() envoie la valeur de resultat dans le flux de sortie standard (console)
print(resultat)