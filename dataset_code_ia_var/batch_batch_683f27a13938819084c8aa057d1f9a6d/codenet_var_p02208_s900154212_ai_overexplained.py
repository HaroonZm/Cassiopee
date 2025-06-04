# Importation de modules standards de la bibliothèque Python
# 'itertools' est un module qui fournit différentes fonctions spécialisées pour manipuler des itérateurs.
from itertools import *
# 'bisect' contient des fonctions pour manipuler des listes triées.
from bisect import *
# 'math' contient des fonctions mathématiques telles que racine carrée, sinus, etc.
from math import *
# 'collections' propose des containers basiques alternatifs aux types natifs.
from collections import *
# 'heapq' propose une implémentation de la structure de données heap (file de priorité).
from heapq import *
# 'random' donne accès à différents générateurs de nombres pseudo-aléatoires.
from random import *
# 'sys' inclut des fonctionnalités spécifiques au système d'exécution, par exemple la gestion des entrées/sorties.
import sys

# Modification explicite de la limite de récursion pour autoriser de très profondes récursions (ici jusqu'à 10⁶ appels de fonction imbriqués).
sys.setrecursionlimit(10 ** 6)

# Définition d'une fonction anonyme (lambda) appelée int1 :
# Elle prend une entrée x (supposée convertible en entier), la convertit, et soustrait 1.
# Cela est fréquemment utilisé pour transformer un indice 1-based en indice 0-based (débutant à zéro).
int1 = lambda x: int(x) - 1

# Définition d'une fonction anonyme (lambda) appelée p2D :
# Elle prend une séquence x, la "déplie" (*x) et affiche chaque élément séparément sur une ligne différente (sep="\n").
p2D = lambda x: print(*x, sep="\n")

# Déclaration de petites fonctions utilitaires pour la lecture des entrées standardisées depuis 'sys.stdin' 
# On lit l'entrée puis on la convertit directement au bon type.
def II():
    # Retourne un entier lu sur l'entrée standard (typiquement utilisé pour lire un nombre).
    return int(sys.stdin.readline())

def MI():
    # Retourne un itérateur de plusieurs entiers lus sur la même ligne chacune séparée par un espace.
    return map(int, sys.stdin.readline().split())

def MI1():
    # Comme MI, mais soustrait 1 à chaque valeur (pour obtenir des indices zéro-based).
    return map(int1, sys.stdin.readline().split())

def MF():
    # Retourne un itérateur de flottants lus sur une ligne. Utile pour les valeurs à virgule.
    return map(float, sys.stdin.readline().split())

def LI():
    # Retourne une liste d'entiers obtenue de la ligne courante.
    return list(map(int, sys.stdin.readline().split()))

def LI1():
    # Liste d'entiers "-1" (indices 0-based) à partir d'une ligne entrée.
    return list(map(int1, sys.stdin.readline().split()))

def LF():
    # Liste de flottants à partir de la ligne entrée.
    return list(map(float, sys.stdin.readline().split()))

def LLI(rows_number):
    # Crée une liste de listes d'entiers à partir de 'rows_number' lignes. Pour chaque ligne, on lit via LI().
    return [LI() for _ in range(rows_number)]

# Variable contenant les 4 déplacements élémentaires sur une grille (haut, droite, bas, gauche),
# sous la forme de couples (dx, dy).
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    # Début du programme principal.
    # Lecture de 7 entiers sur la première ligne, chacun stocké dans x, y, z, n, m, s, t.
    # Cette ligne est souvent la ligne de paramètres du problème à traiter.
    x, y, z, n, m, s, t = MI()
    # On convertit les indices s et t en indices adaptés à la représentation interne (zéro-based)
    # s est décrémenté de 1
    # t est décrémenté de 1 puis on ajoute n (t-1+n). Ceci fait typiquement référence à deux "côtés" distincts dans une modélisation par graphe biparti.
    s, t = s - 1, t - 1 + n
    # Déclaration d'une liste qui contiendra pour chaque élément une paire (a, b) correspondant aux objets du problème.
    itoab = []
    # Déclaration de deux dictionnaires où chaque clef (a ou b) référence des listes d'indices.
    # ceux-ci représentent les liens d'adjacence entre objets partageant une même caractéristique 'a' ou 'b'.
    # defaultdict(list) initialise automatiquement une liste vide pour chaque nouvelle clef non existante.
    to1 = defaultdict(list)
    to2 = defaultdict(list)
    # Parcours des n premiers objets.
    for i in range(n):
        # Pour chaque objet, on lit deux entiers (a, b) chacun décrémenté de 1 (utilisation de MI1).
        a, b = MI1()
        # On ajoute la paire [a, b] à la liste principale.
        itoab.append([a, b])
        # On ajoute l'indice dans la liste des objets ayant la même caractéristique 'a' et 'b'.
        to1[a].append(i)
        to2[b].append(i)
    # Parcours des m objets suivants (indice allant de n à n+m-1).
    for i in range(n, n + m):
        # On lit deux entiers (b, a), chacun décrémenté de 1.
        b, a = MI1()
        # On ajuste la valeur 'a' en lui ajoutant x (ici typiquement pour la distinguer formellement des a précédents).
        a += x
        # On stocke la paire [a, b].
        itoab.append([a, b])
        # Mise à jour des dictionnaires d'adjacence.
        to1[a].append(i)
        to2[b].append(i)
    # Initialisation d'un tableau de distances, de taille n+m (nombre total de sommets), chaque distance mise initialement à -1 (non visité).
    dist = [-1] * (n + m)
    # Déclaration d'une heap (file de priorité utilisée pour Dijkstra ou BFS pondéré).
    hp = []
    # On y ajoute un couple [0, s] : distance actuelle (0, départ) et indice de départ (s).
    heappush(hp, [0, s])
    # On explore la file de priorité jusqu'à épuisement de tous les sommets accessibles.
    while hp:
        # On prend la paire de distance minimale (toujours le premier élément, car hp est trié).
        d, i = heappop(hp)
        # Si le sommet i a déjà été visité (distance différente de -1), on saute cette itération.
        if dist[i] != -1:
            continue
        # On assigne la distance d'aujourd'hui à ce sommet.
        dist[i] = d
        # On récupère la paire (a, b) correspondant à ce sommet.
        a, b = itoab[i]
        # Pour chaque sommet ayant en commun la valeur 'a', on les parcourt.
        for j in to1[a]:
            # Si on atteint le sommet cible t, on affiche la distance (d+1) et on arrête immédiatement le programme via exit().
            if j == t:
                print(d + 1)
                exit()
            # On saute si c'est le nœud actuel.
            if j == i:
                continue
            # On saute si déjà visité.
            if dist[j] != -1:
                continue
            # On ajoute ce voisin à la heap, la distance passant à d+1.
            heappush(hp, [d + 1, j])
        # Idem pour tous les sommets partageant la même valeur 'b'.
        for j in to2[b]:
            if j == t:
                print(d + 1)
                exit()
            if j == i:
                continue
            if dist[j] != -1:
                continue
            heappush(hp, [d + 1, j])
    # Si la boucle se termine sans avoir atteint le sommet cible, cela signifie que t est injoignable depuis s.
    # On affiche donc -1 pour signaler l'absence de solution.
    print(-1)

# Appel de la fonction principale, point d'entrée du programme.
main()