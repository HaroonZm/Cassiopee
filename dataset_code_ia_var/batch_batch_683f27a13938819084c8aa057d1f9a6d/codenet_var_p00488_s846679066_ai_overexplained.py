# Importation du module 'sys', qui fournit des fonctions et des variables utilisées pour manipuler des parties du runtime Python (ici, il n'est pas utilisé mais précisé par l'énoncé de code d'origine)
import sys

# Importation du module 'math', qui fournit des fonctions mathématiques standard, par exemple sqrt pour la racine carrée, floor, etc.
import math

# Demande à l'utilisateur de saisir une valeur au clavier. Cette valeur attendue est sous forme de chaîne de caractères.
# La fonction 'input()' affiche la chaîne vide (aucun prompt), puis attend que l'utilisateur tape une valeur et appuie sur Entrée.
# Ensuite, la fonction 'int()' tente de convertir la chaîne de caractères fournie par l'utilisateur en nombre entier.
# Cette valeur entière est ensuite stockée dans la variable 'p1'.
p1 = int(input())

# Même opération pour la variable 'p2', qui représente probablement le prix ou un nombre entier similaire, saisi par l'utilisateur.
p2 = int(input())

# Saisie et conversion en entier de la troisième variable, 'p3'.
p3 = int(input())

# Idem, on demande à l'utilisateur deux autres valeurs et on les convertit aussi en entiers pour 'j1' et 'j2'.
j1 = int(input())
j2 = int(input())

# Utilisation de la fonction 'min()' qui fait partie des fonctions standards de Python :
# Elle prend une séquence (plusieurs valeurs séparées par des virgules) et retourne la plus petite.
# Ici, on compare 'p1', 'p2' et 'p3', et on stocke la valeur minimale dans la variable 'p_min'.
p_min = min(p1, p2, p3)

# De la même façon, on utilise 'min()' pour trouver la plus petite valeur entre 'j1' et 'j2', 
# et l'assigner à la variable 'J_min'.
J_min = min(j1, j2)

# On calcule une nouvelle valeur entière nommée 'min_sum'.
# Elle est obtenue en additionnant la valeur minimale parmi les trois nombres saisis pour "p" (p_min) 
# et la valeur minimale parmi les deux nombres saisis pour "j" (J_min), puis en soustrayant 50 du résultat.
# Par exemple, si p_min vaut 100 et J_min vaut 50, alors min_sum sera égal à 100 + 50 - 50 = 100.
min_sum = p_min + J_min - 50

# Affiche dans la console la valeur contenue dans la variable 'min_sum'.
# La fonction 'print()' permet d'afficher des messages, des variables ou d'autres objets sur la sortie standard (souvent l'écran).
print(min_sum)