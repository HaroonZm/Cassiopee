# Importation du module math, qui offre des fonctions mathématiques standards
import math

# Importation spécifique de certaines fonctions depuis le module math :
# gcd : pour calculer le plus grand commun diviseur
# pi : la constante mathématique π (environ 3.14159)
# sqrt : permet de calculer la racine carrée d'un nombre
from math import gcd, pi, sqrt

# Déclaration d'une constante INF, qui est utilisée pour représenter l'infini (float("inf"))
INF = float("inf")

# Importation du module sys, qui fournit un accès à des fonctions liées au système d'exploitation
import sys

# Modification du paramètre de limite de récursion
# Ceci augmente la profondeur maximale autorisée pour la récursion à 1 000 000
sys.setrecursionlimit(10**6)

# Importation du module itertools, qui fournit des fonctions utiles pour manipuler des itérateurs (par exemple les permutations, combinaisons, etc.)
import itertools

# Importation depuis collections :
# Counter : une classe qui sert à compter les éléments d'un itérable
# deque : une structure de données qui fonctionne comme une "double-ended queue" (file d'attente à double extrémité)
from collections import Counter, deque

# Définition d'une fonction i_input, qui renvoie un entier lu depuis l'entrée standard (clavier)
def i_input():
    return int(input())  # lit une ligne au clavier, puis la convertit en entier et la retourne

# Définition d'une fonction i_map, qui renvoie un objet map contenant des entiers issus des valeurs lues au clavier séparées par des espaces
def i_map():
    return map(int, input().split())  # lit une ligne, la découpe en mots (split), convertit chaque mot en entier grâce à la fonction map

# Définition d'une fonction i_list, qui crée une liste d'entiers depuis une ligne entrée par l'utilisateur
def i_list():
    return list(i_map())  # transforme l'objet map produit par i_map en liste

# Définition d'une fonction i_row, qui lit N lignes et retourne une liste d'entiers correspondant à chaque ligne
def i_row(N):
    return [i_input() for _ in range(N)]  # construit une liste en appelant i_input N fois

# Définition d'une fonction i_row_list, qui lit N lignes, chaque ligne contenant plusieurs entiers, retourne une liste contenant N sous-listes d'entiers
def i_row_list(N):
    return [i_list() for _ in range(N)]  # construit une liste contenant N listes d'entiers, chaque sous-liste issue d'une ligne d'entrée

# Définition d'une fonction s_input, qui lit une ligne de texte de l'utilisateur (entrée standard) et la retourne telle quelle (en tant que chaîne de caractères)
def s_input():
    return input()  # lit une ligne texte, retourne la chaîne de caractères entrée par l'utilisateur

# Définition d'une fonction s_map, qui lit une ligne et sépare ses mots en une liste
def s_map():
    return input().split()  # lit une ligne de texte et la découpe en mots (chaînes) selon les espaces

# Définition d'une fonction s_list, qui lit une ligne, la sépare en mots, et retourne la liste de ces mots
def s_list():
    return list(s_map())  # transforme en liste l'objet retourné par s_map

# Définition d'une fonction s_row, qui lit N lignes et retourne une liste de fonctions s_input (erroné ici : cela capture la fonction, pas le résultat; la version correcte invoquerait s_input())
def s_row(N):
    return [s_input for _ in range(N)]  # (Remarque : cela retourne la fonction s_input, pas les lignes lues effectivement)

# Définition d'une fonction s_row_str, qui lit N lignes et, pour chaque ligne, la découpe en mots et ajoute la liste à un tableau
def s_row_str(N):
    return [s_list() for _ in range(N)]  # pour chaque ligne, lit et découpe en mots (mots séparés par des espaces)

# Définition d'une fonction s_row_list, qui lit N lignes et pour chacune, retourne la liste des caractères (chaque ligne devient une liste de caractères)
def s_row_list(N):
    return [list(s_input()) for _ in range(N)]  # pour chaque ligne lue, crée une liste de caractères à partir de la chaîne

# Définition de la fonction principale du programme
def main():
    # Lit quatre entiers depuis l'entrée standard, sur une seule ligne, et les affecte aux variables a, b, c, d
    a, b, c, d = i_map()  # suppose que l'utilisateur entre quatre nombres entiers séparés par des espaces

    # Calcule quatre produits possibles : a*c, a*d, b*c, b*d, les stocke dans une liste ans
    ans = [a*c, a*d, b*c, b*d]  # pour chaque combinaison possible entre a/b et c/d, calcule le produit respectif

    # Affiche à l'écran la valeur maximale trouvée parmi tous les produits possibles
    print(max(ans))  # trouve et affiche le maximum de la liste ans

# Point d'entrée du programme. Si ce fichier est exécuté en tant que programme principal, alors la fonction main sera appelée.
if __name__ == "__main__":  # comparaison pour vérifier si ce fichier est le fichier principal exécuté
    main()  # appel de la fonction main pour démarrer l'exécution du programme