# Importation de plusieurs modules standards de Python pour fournir diverses fonctionnalités.
# Certains de ces modules peuvent ne pas être utilisés dans ce script, mais ils sont fréquemment utilisés pour la manipulation mathématique, de chaînes de caractères, de structures de données, etc.
import math      # Fournit des fonctions mathématiques telles que sqrt, sin, etc.
import string    # Contient des constantes et fonctions pour manipuler des chaînes de caractères.
import itertools # Fournit des outils pour créer des itérateurs efficaces (permutations, combinaisons, etc).
import fractions # Permet de travailler avec des fractions rationnelles.
import heapq     # Fournit une implémentation de tas binaire (file de priorité).
import collections # Fournit des types de données avancés comme deque, Counter, defaultdict.
import re        # Module d'expressions régulières pour la recherche de motifs dans les chaînes.
import array     # Permet de manipuler des tableaux efficaces en mémoire (moins utilisé que list pour usage courant).
import bisect    # Permet la recherche et l'insertion efficace dans des listes triées.
import sys       # Module système, utilisé ici pour lire l'entrée standard et changer certains comportements du système.
import random    # Pour générer des nombres aléatoires et mélanger des séquences.
import time      # Pour suivre le temps, pour mesurer des performances ou pour des temporisations.
import copy      # Fournit des fonctions pour copier des objets (copies superficielles et profondes).
import functools # Fournit des outils pour la programmation fonctionnelle (partial, reduce, lru_cache, etc).

# Augmente la limite maximale de profondeur de récursion.
# Cela permet d'appeler des fonctions récursivement jusqu'à 10 millions de fois.
sys.setrecursionlimit(10**7)

# Définition d'une constante représentant une valeur infinie (pas réellement infini mais très grand).
inf = 10**20

# Définition d'un epsilon pour les comparaisons de nombres à virgule flottante très proches de zéro.
eps = 1.0 / 10**10

# Un nombre premier usuel, utilisé dans de nombreux problèmes d'arithmétique modulaire (problème de reste modulo).
mod = 10**9+7

# Définition des mouvements possibles pour aller dans les 4 directions cardinales sur une grille 2D.
# Chaque tuple représente un déplacement relatif (dx, dy).
# (0,-1) : gauche, (1,0) : bas, (0,1) : droite, (-1,0) : haut
dd = [(0,-1),(1,0),(0,1),(-1,0)]

# Définition des 8 directions (voisinage de Moore) sur une grille 2D.
# Ceci inclut les diagonales en plus des 4 directions cardinales.
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

# Fonction utilitaire pour lire une ligne de l'entrée standard
# La méthode readline lit une ligne jusqu'à '\n'
# split découpe la chaîne en morceaux, et int(x) convertit chaque morceau en entier
# La compréhension de liste permet de retourner la liste de valeurs entières.
def LI(): 
    return [int(x) for x in sys.stdin.readline().split()]

# Idem mais on soustrait 1 à chaque entier (souvent utile pour passer d'un indice base 1 à base 0)
def LI_(): 
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Lit une ligne de l'entrée standard et retourne une liste de flottants
def LF(): 
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne de l'entrée standard et la découpe en mots retournés sous forme de liste de chaînes
def LS(): 
    return sys.stdin.readline().split()

# Lit une ligne, la convertit en entier
def I(): 
    return int(sys.stdin.readline())

# Lit une ligne, la convertit en flottant
def F(): 
    return float(sys.stdin.readline())

# Lit une ligne via la fonction input standard (peut être utilisée dans certains contextes par rapport à sys.stdin.readline)
def S(): 
    return input()

# Affiche une chaîne s tout en forçant le flush du buffer de sortie standard, utile dans des contextes interactifs
def pf(s): 
    return print(s, flush=True)

# Définition de la fonction principale qui réalisera le traitement principal
def main():
    # Lit un entier depuis l'entrée standard : représente potentiellement une taille (longueur d'une chaîne, taille d'un tableau, etc.)
    n = I()
    # Lit une chaîne de l'entrée standard
    s = S()
    # Construit une list 'a' encadrée par deux valeurs 2 aux extrémités. 
    # Cela est généralement employé pour éviter des erreurs d'index lors de parcours.
    # On ajoute un élément au début (2), puis...
    # On ajoute, pour chaque caractère dans s :
    #     - None si ce caractère est '>' (symbole supérieur), 
    #     sinon 1 pour tout autre caractère
    # Enfin, on ajoute un 2 à la fin de la liste.
    a = [2] + [None if s[i] == '>' else 1 for i in range(n)] + [2]

    # Définition d'une fonction interne 'f' prenant en argument un index 'i'
    def f(i):
        # Si l'index i est hors bornes (avant le début ou après la fin), retourne 0 et None
        if i < 0 or i > n+1:
            return (0, None)
        # Initialise une variable de compteur à zéro
        c = 0
        # nl et nr sont des indices qui servent à parcourir la liste 'a' vers la gauche (nl) et vers la droite (nr)
        nl = i-1
        nr = i+1
        # ni est l'indice courant que l'on parcourt pour trouver la valeur 2 (début ou fin)
        ni = i
        # Tant que l'élément courant n'est pas égal à 2 (bordure de la liste)
        while a[ni] != 2:
            # Si la valeur de a[ni] est None (correspond à un '>' dans la chaîne originale)
            if a[ni] is None:
                # On se déplace vers la droite en mettant ni = nr et en incrémentant nr
                ni = nr
                nr += 1
            else:
                # Sinon (donc a[ni] == 1), on se déplace vers la gauche en mettant ni = nl et en décrémentant nl
                ni = nl
                nl -= 1
            # Incrémente le compteur pour chaque déplacement
            c += 1
        # Retourne un tuple contenant le compteur 'c' (nombre d'étapes avant d'atteindre une bordure)
        # et un booléen indiquant si la bordure touchée était la toute première (ni == 0), ce qui renseigne le sens du parcours
        return (c, ni == 0)

    # Initialise la borne supérieure d'une recherche binaire à n+1
    ma = n+1
    # Initialise la borne inférieure à 0
    mi = 0
    # mm sera la valeur médiane entre ma et mi (borne d'itération courante)
    mm = (ma+mi) // 2
    # r va contenir la valeur maximum trouvée lors de la recherche
    r = 0
    # Boucle de recherche binaire : continue tant que la borne supérieure dépasse la borne inférieure
    while ma > mi:
        # Calcule une borne médiane mm
        mm = (ma+mi) // 2
        # Appelle la fonction f sur cette borne mm
        c, ff = f(mm)
        # Mets à jour r si c (nombre d'étapes) est supérieur à ce qu'on a trouvé jusque-là
        if r < c:
            r = c
        # Si la bordure atteinte était la première (on remonte vers la gauche/li 0)
        if ff:
            # On recherche dans la partie droite (on pousse la borne inférieure)
            mi = mm + 1
        else:
            # Sinon dans la partie gauche (on réduit la borne supérieure)
            ma = mm
    # Après la recherche binaire, on vérifie les valeurs proches autour de mm pour ne pas manquer un maximum local
    for i in range(mm-1,mm+2):
        # Calcule le nombre d'étapes pour chaque i proche de mm
        c,ff = f(i)
        # Mets à jour r si ce résultat est meilleur
        if r < c:
            c = r

    # Retourne le résultat maximum trouvé
    return r

# Appel de la fonction principale et affiche le résultat sur la sortie standard
print(main())