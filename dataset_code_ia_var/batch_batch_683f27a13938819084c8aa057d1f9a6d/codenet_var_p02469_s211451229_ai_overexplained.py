# Demande à l'utilisateur de saisir une valeur (supposée être un entier).
# Cette valeur représente le nombre d'éléments dans la séquence.
# La fonction input() prend une entrée de l'utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne de caractères en entier.
n = int(input())

# Demande à l'utilisateur de saisir une ligne comportant plusieurs entiers séparés par des espaces.
# La fonction input() lit la ligne entière en tant que chaîne.
# La méthode split() découpe cette chaîne en une liste de sous-chaînes où chaque sous-chaîne correspond à un nombre (toujours en chaîne).
# L'expression [int(i) for i in input().split()] est une compréhension de liste.
# Pour chaque élément i de la liste résultant de split(), on convertit i en entier avec int(i).
# La liste finale 'a' contient ainsi tous les entiers saisis par l'utilisateur.
a = [int(i) for i in input().split()]

# On importe le module math.
# 'import math' donne accès à diverses fonctions mathématiques, dont 'gcd' (plus grand commun diviseur).
import math

# On initialise la variable 'lcm' (plus petit commun multiple) avec le premier élément de la liste 'a'.
# Cela suppose que la liste 'a' n'est pas vide.
lcm = a[0]

# On parcourt chaque élément de la liste 'a', sauf le premier (car il est déjà entreposé dans 'lcm' au départ).
# L'expression 'a[1:]' crée une nouvelle liste qui contient tous les éléments de 'a' à partir de l'indice 1 jusqu'à la fin.
for i in a[1:]:
    # À chaque itération, on calcule le ppcm (plus petit commun multiple) actuel de 'lcm' et du nouvel élément 'i'.
    # math.gcd(lcm, i) renvoie le plus grand commun diviseur entre 'lcm' et 'i'.
    # L'opération i * lcm produit le produit de ces deux nombres.
    # L'opérateur // effectue la division entière, c'est-à-dire que seul le quotient entier est conservé (pas la partie décimale).
    # En divisant le produit par leur pgcd, on obtient le ppcm (par la propriété : ppcm(a, b) = abs(a*b) // pgcd(a, b)).
    lcm = i * lcm // math.gcd(lcm, i)

# Affiche la valeur finale de 'lcm' qui est le ppcm de tous les nombres de la liste 'a'.
# print affiche le résultat (le ppcm) à l'utilisateur.
print(lcm)