# Importation du module 'sys' de la bibliothèque standard
# Le module 'sys' contient des fonctions et variables utilisées pour interagir avec l'interpréteur Python
import sys

# Demander à l'utilisateur d'entrer une ligne de texte via la fonction input()
# 'input()' lit une ligne de texte depuis l'entrée standard (habituellement le clavier)
# Par exemple, l'utilisateur peut entrer "3 4"
user_input = input()

# Appliquer la méthode split() à la chaîne de caractères entrée par l'utilisateur
# split() sépare la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur par défaut
# Si l'utilisateur a entré "3 4", split() renverra la liste ['3', '4']
split_input = user_input.split()

# Utiliser la fonction map() pour appliquer la fonction int à chaque élément de la liste split_input
# map(int, split_input) renverra un itérable où chaque chaîne de caractères est convertie en entier
mapped_input = map(int, split_input)

# Convertir l'itérable obtenu par map() en une liste contenant les entiers extraits de user_input
# list() transforme l'itérable en une liste, par exemple [3, 4]
input_list = list(mapped_input)

# Décomposer la liste en deux variables a et b
# Cela suppose que la liste contient exactement deux éléments
# 'a' recevra le premier élément de la liste et 'b' le second
a, b = input_list

# Calculer le produit des deux entiers a et b en utilisant l'opérateur *
# L'opérateur * effectue la multiplication arithmétique sur deux nombres
result = a * b

# Afficher le résultat de la multiplication à l'utilisateur
# La fonction print() envoie sa sortie vers la sortie standard (habituellement l'écran)
print(result)