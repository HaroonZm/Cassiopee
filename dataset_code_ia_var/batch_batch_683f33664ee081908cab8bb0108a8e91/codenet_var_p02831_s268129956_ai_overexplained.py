import math  # Importation du module 'math' qui fournit des fonctions mathématiques, ici on l’utilisera pour le calcul du PGCD

# Lecture de deux entiers depuis l'entrée standard (c’est-à-dire depuis le clavier)
# La fonction input() lit une ligne de texte au format chaîne de caractères (string)
# Ensuite, split() sépare cette chaîne selon les espaces et renvoie une liste de chaînes
# map(int, ...) transforme chaque chaîne de cette liste en nombre entier (int)
# Enfin, on attribue les deux entiers obtenus aux variables A et B
A, B = map(int, input().split())

# Calcul du résultat selon la formule du PPCM (plus petit commun multiple)
# On multiplie d'abord A et B ensemble. L'opérateur * effectue la multiplication arithmétique
# On utilise 'math.gcd(A, B)' pour calculer le plus grand commun diviseur (PGCD) des deux nombres A et B
# La fonction math.gcd retourne un entier correspondant au PGCD
# On divise ensuite le produit (A * B) par le PGCD obtenu pour déterminer le PPCM
# L'opérateur // est la division entière, c’est-à-dire qu’on ne garde que la partie entière du résultat sans les décimales
result = (A * B) // math.gcd(A, B)

# Affichage du résultat final à l'utilisateur
# La fonction print() affiche la valeur fournie entre parenthèses sur une nouvelle ligne de la sortie standard (généralement l'écran)
print(result)