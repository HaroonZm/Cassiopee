#!/usr/bin/env python3

# Importation du module collections. 'defaultdict' permet de créer un dictionnaire avec une valeur par défaut lorsqu'une nouvelle clé est utilisée.
from collections import defaultdict

# Importation de deque depuis collections. 'deque' est une structure de file ou pile doublement terminée, mais elle n'est pas utilisée dans ce code.
from collections import deque

# Importation de heappush et heappop depuis heapq. Ceux-ci sont utilisés pour la manipulation de files de priorité (heaps), mais ne sont pas utilisés ici.
from heapq import heappush, heappop

# Le module sys est importé pour accéder à des fonctions spécifiques du système, notamment la gestion des flux d'entrée et sortie.
import sys

# Le module math fournit des fonctions mathématiques standards. Non utilisé explicitement ici.
import math

# Le module bisect permet d'utiliser des fonctions standards pour éliminer la complexité lors de l'insertion ou de la recherche dans des listes triées. Pas utilisé ici dans le code principal.
import bisect

# Le module random permet de générer des nombres aléatoires. N'est pas utilisé dans ce code.
import random

# Déclaration d'une fonction utilitaire LI, toujours utilisée pour lire une ligne d'entrée, la découper en entiers et retourner une liste d'entiers.
def LI():
    # sys.stdin.readline() lit une ligne entière en entrée, par exemple "1 2 3\n". La méthode split() découpe la chaîne en fonction des espaces. La fonction map applique la fonction int à chaque élément résultant et list convertit le map en liste.
    return list(map(int, sys.stdin.readline().split()))

# Déclaration d'une fonction utilitaire I, qui lit un entier à partir de l'entrée standard.
def I():
    # sys.stdin.readline() lit la ligne comme chaîne, int() convertit la chaîne en entier.
    return int(sys.stdin.readline())

# Déclaration d'une fonction utilitaire LS. Elle lit une ligne, la coupe par espaces, puis convertit chaque morceau en une liste de caractères (donc retourne une liste de listes de caractères).
def LS():
    return list(map(list, sys.stdin.readline().split()))

# Déclaration d'une fonction utilitaire S, qui lit une ligne d'entrée et retourne une liste de caractères, sauf le dernier, car [-1] enlève généralement le caractère \n de fin de ligne.
def S():
    return list(sys.stdin.readline())[:-1]

# Déclaration d'une fonction utilitaire IR, qui lit n lignes, chaque ligne contenant un entier, et renvoie la liste de ces entiers.
def IR(n):
    # Création d'une liste de taille n remplie avec None, qui sera remplacée avec la valeur à chaque itération.
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = I()
    return l

# Déclaration d'une fonction utilitaire LIR, comme IR mais chaque ligne contient une liste d'entiers.
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

# Déclaration d'une fonction utilitaire SR, qui lit n lignes, chaque ligne étant un mot, et renvoie une liste de ces listes de caractères.
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

# Déclaration d'une fonction utilitaire LSR, similaire à LIR et SR, mais chaque ligne lue est décomposée en une liste de listes de caractères.
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Augmentation de la limite de récursion pour permettre une récursion profonde, utile dans le cas de structures de données récursives (par exemple, arbres profonds).
sys.setrecursionlimit(1000000)

# Déclaration d'une constante mod servant généralement de modulo pour les problèmes d'arithmétique modulaire.
mod = 1000000007

# ===============================
# Fonction A
# ===============================
def A():
    # On lit une ligne d'entrées composées d'entiers.
    e = LI()
    # Création d'un dictionnaire à valeurs par défaut 0, permettant de compter les occurrences de chaque valeur.
    d = defaultdict(int)
    # Pour chaque élément de la liste lue en entrée, on incrémente son compteur dans le dictionnaire.
    for i in e:
        d[i] += 1
    # Pour chaque valeur (i.e., nombre de fois qu'un élément est apparu), on vérifie si celle-ci diffère de 2.
    for i in d.values():
        if i != 2:
            # Si un élément n'apparaît pas exactement deux fois, on affiche "no".
            print("no")
            break  # On sort de la boucle car on a trouvé une irrégularité.
    else:
        # La clause else associée au for s'exécute seulement si la boucle for se termine sans exécuter de break. Ici cela signifie que chaque valeur apparaît exactement deux fois.
        print("yes")
    return

# ===============================
# Fonction B
# ===============================
def B():
    # Lecture d'un entier n, qui représente généralement la taille de la liste suivante.
    n = I()
    # Lecture d'une liste de n entiers.
    a = LI()
    # On trie la liste 'a' en place dans l'ordre croissant.
    a.sort()
    # On initialise la variable 'ans' à une très petite valeur (moins l'infini), pour y stocker la réponse maximale trouvée.
    ans = -float("inf")
    # Parcourt tous les indices possibles pour c dans la liste, de 0 à n-1 inclus.
    for c in range(n):
        # Parcourt tous les indices possibles pour d dans la liste, de 0 à c-1 inclus.
        for d in range(c):
            # On calcule la différence entre la valeur à l'index c et l'index d, pour obtenir 'm'.
            m = a[c] - a[d]
            # Recherche de l'indice 'e' pour le plus grand index différent de c et d.
            for i in range(n)[::-1]:  # [::-1] parcourt n-1 à 0, soit les indices du plus grand au plus petit.
                if i != c and i != d:
                    e = i  # On prend la première valeur rencontrée correspondant aux critères.
                    break  # On arrête la boucle, car on cherche seulement le plus grand index valide.
            # Recherche de l'indice 'b' pour le deuxième plus grand index différent de c et d.
            for i in range(e)[::-1]:  # De e-1 à 0, (e lui-même non inclus)
                if i != c and i != d:
                    b = i  # On sélectionne le prochain plus grand index différent de c et d.
                    break  # On sort de cette boucle après avoir trouvé b.
            # On met à jour la réponse maximale trouvée. On considère le cas, sur la base de e et b, du quotient (a[e]+a[b])/m.
            ans = max(ans, (a[e] + a[b]) / m)
    # Affichage de la réponse finale.
    print(ans)
    return

# ===============================
# Fonction C (Vide)
# ===============================
def C():
    return

# ===============================
# Fonction D (Vide)
# ===============================
def D():
    return

# ===============================
# Fonction E (Vide)
# ===============================
def E():
    return

# ===============================
# Fonction F (Vide)
# ===============================
def F():
    return

# ===============================
# Fonction G (Vide)
# ===============================
def G():
    return

# ===============================
# Fonction H (Vide)
# ===============================
def H():
    return

# ===============================
# Fonction I_ (Vide)
# ===============================
def I_():
    return

# ===============================
# Fonction J (Vide)
# ===============================
def J():
    return

# ===============================
# Point d'entrée principal du script
# ===============================
if __name__ == "__main__":
    # Si ce script est exécuté comme programme principal (et non importé en module), on lance la fonction B(). 
    B()