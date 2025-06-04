# Demander à l'utilisateur de saisir un nombre entier et le stocker dans la variable N
# input() permet à l'utilisateur de saisir une chaîne de caractères depuis la console
# int() convertit la chaîne de caractères saisie en un entier
N = int(input())

# Demander à l'utilisateur de saisir une séquence d'entiers séparés par des espaces
# input() prend une ligne d'entrée utilisateur sous forme de chaîne de caractères
# split() sépare la chaîne en une liste de sous-chaînes là où il y a des espaces
# map(int, ...) applique la fonction int() à chaque sous-chaîne dans la liste pour la convertir en entier
# set(...) convertit la séquence d'entiers en un ensemble (ensemble = collection sans doublons, non ordonnée)
A = set(map(int, input().split()))

# Demander à l'utilisateur un autre entier, qui sera stocké dans la variable M
# Ceci est une autre saisie utilisateur et sert souvent à indiquer le nombre d'éléments d'un ensemble
M = int(input())

# Demander à l'utilisateur de saisir une séquence d'entiers séparés par des espaces pour constituer un autre ensemble
B = set(map(int, input().split()))

# Calculer la différence symétrique (XOR d'ensembles) entre A et B, c'est-à-dire les éléments qui sont dans A ou B mais pas dans les deux
# L'opérateur ^ appliqué aux ensembles en Python donne un nouvel ensemble contenant ces éléments uniques à chaque ensemble
C = A ^ B

# Vérifier si l'ensemble C n'est pas vide (cas où il y a au moins un élément unique dans A ou B)
if C:
    # sorted(C) trie l'ensemble C par ordre croissant et le retourne sous forme de liste
    # print(*...) utilise l'opérateur d'éclatement (*) pour passer chaque élément de la liste comme un argument distinct de print()
    # sep='\n' indique à print d'afficher chaque argument sur une nouvelle ligne
    print(*sorted(C), sep='\n')
# Note : si C est vide, l'instruction 'print' n'est pas exécutée et rien ne s'affiche