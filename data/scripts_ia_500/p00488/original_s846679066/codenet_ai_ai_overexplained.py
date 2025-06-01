import sys  # Importation du module sys, utilisé pour manipuler des fonctionnalités spécifiques du système, ici non utilisé mais souvent nécessaire pour gérer les entrées/sorties dans des contextes plus complexes.
import math  # Importation du module math, qui offre des fonctions mathématiques avancées, ici importé mais non utilisé dans ce script.

# La fonction input() permet de récupérer une entrée utilisateur sous forme de chaîne de caractères (string).
# La fonction int() convertit cette chaîne de caractères en un nombre entier (integer).

p1 = int(input())  # Lecture de la première entrée utilisateur, convertie en entier, et affectation à la variable p1.
p2 = int(input())  # Lecture de la deuxième entrée utilisateur, convertie en entier, et affectation à la variable p2.
p3 = int(input())  # Lecture de la troisième entrée utilisateur, convertie en entier, et affectation à la variable p3.

j1 = int(input())  # Lecture de la quatrième entrée utilisateur, convertie en entier, et affectation à la variable j1.
j2 = int(input())  # Lecture de la cinquième entrée utilisateur, convertie en entier, et affectation à la variable j2.

# Utilisation de la fonction min() pour trouver la plus petite valeur parmi plusieurs variables.
p_min = min(p1, p2, p3)  # Trouver la valeur minimale parmi p1, p2 et p3, et stocker ce résultat dans la variable p_min.

J_min = min(j1, j2)  # Trouver la valeur minimale entre j1 et j2, et stocker ce résultat dans la variable J_min.

# Additionner les deux valeurs minimales pour obtenir une somme partielle.
# Puis soustraire 50 de cette somme partielle selon les instructions du programme.
min_sum = p_min + J_min - 50  # Calcul de la somme finale en soustrayant 50.

# Affichage du résultat final sur la sortie standard (généralement l'écran).
print(min_sum)  # La fonction print() affiche la valeur de min_sum.