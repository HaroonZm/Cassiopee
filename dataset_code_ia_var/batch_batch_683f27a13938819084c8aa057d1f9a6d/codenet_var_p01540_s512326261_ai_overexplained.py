import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Augmente la limite maximale de récursion pour permettre des appels récursifs profonds.
sys.setrecursionlimit(10**7)  # Définit la limite de récursion sur 10 millions (10**7)

# Valeur représentant l'infini, utilisée pour initialiser ou comparer des valeurs très grandes.
inf = 10**20  # Chiffre arbitraire très grand pour simuler l'infini

# Précision epsilon, souvent utilisée pour comparer des nombres flottants.
eps = 1.0 / 10**10  # Très petite valeur pour la tolérance flottante

# Modulo utilisé souvent dans des problèmes de dénombrement pour éviter les dépassements d'entier.
mod = 10**9 + 7  # Nombre premier standard pour des opérations de modulo

# Liste des directions pour des déplacements en 2D (haut, droite, bas, gauche).
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Liste des 8 directions (y compris diagonales) pour des déplacements en 2D.
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Déclaration de fonctions utilitaires pour lire et interpréter les données d'entrée :

def LI():
    # Lecture d'une ligne de stdin, découpage en sous-chaînes selon l'espace,
    # Conversion de chaque chaîne en entier et création d'une liste avec ces entiers.
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Même que LI(), mais chaque entier est décrémenté de 1 pour indexer à partir de zéro.
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    # Lecture des flottants sur la ligne et transformation en liste de float.
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lecture d'une ligne et découpage en liste de chaînes selon les espaces.
    return sys.stdin.readline().split()

def I():
    # Lit une ligne depuis stdin et convertit directement en entier.
    return int(sys.stdin.readline())

def F():
    # Idem mais conversion en flottant.
    return float(sys.stdin.readline())

def S():
    # Utilise la fonction input() pour une lecture simple d'une chaîne depuis stdin (avec suppression du saut de ligne).
    return input()

def pf(s):
    # Affiche la chaîne/objet (s) puis force le flush du flux de sortie (est utile en concours pour output immédiat).
    return print(s, flush=True)

# Définition d'une classe pour la somme partielle (2D) - appelée communément "cumulative sum" ou "somme de préfixes".

class Ruiwa():
    def __init__(self, a):
        # Stocke la hauteur du tableau 'a' dans self.H, c'est le nombre de lignes.
        self.H = h = len(a)
        # Stocke la largeur du tableau 'a' dans self.W, nombre de colonnes (on suppose toutes les lignes de même longueur).
        self.W = w = len(a[0])
        # Stocke une référence au tableau de base dans self.R.
        self.R = r = a
        # Première passe : Effectuer une somme partielle horizontale.
        # Pour chaque ligne i (0-indexé) :
        for i in range(h):
            # Pour chaque colonne j en partant de 1 jusqu'à la fin (car r[i][j-1] doit exister) :
            for j in range(1, w):
                # Ajoute la valeur de la colonne précédente à la valeur courante pour faire la somme cumulative à gauche.
                r[i][j] += r[i][j - 1]
        # Deuxième passe : Effectuer une somme partielle verticale (après horizontale).
        # Pour chaque ligne i en partant de 1 (i.e., exclure la première ligne), pour chaque colonne :
        for i in range(1, h):
            for j in range(w):
                # Ajoute la valeur de la ligne supérieure à la valeur courante pour obtenir la somme cumulative en haut.
                r[i][j] += r[i - 1][j]

    def search(self, x1, y1, x2, y2):
        # Recherche de la somme de la sous-matrice allant du coin supérieur gauche (x1, y1)
        # au coin inférieur droit (x2, y2), bords inclus.
        # Si la zone est invalide (coin supérieur est après le coin inférieur), retourne 0.
        if x1 > x2 or y1 > y2:
            return 0
        # r est juste un raccourci vers la matrice cumulée
        r = self.R
        # Commence avec la somme cumulée en bas à droite du rectangle d'intérêt.
        rr = r[y2][x2]
        # Gère chacun des 4 coins pour soustraire les zones non désirées lors de la décomposition du rectangle par inclusion-exclusion :
        if x1 > 0 and y1 > 0:
            # On retire la sous-zone à gauche et en haut, mais elle est soustraite deux fois, donc il faut la réadditonner (Inclusion-Exclusion).
            return rr - r[y1 - 1][x2] - r[y2][x1 - 1] + r[y1 - 1][x1 - 1]
        if x1 > 0:
            # Si l'on doit uniquement retirer les colonnes à gauche.
            rr -= r[y2][x1 - 1]
        if y1 > 0:
            # Si l'on doit uniquement retirer les lignes au dessus.
            rr -= r[y1 - 1][x2]
        # Retourne le résultat calculé.
        return rr

def main():
    # Lecture de deux entiers séparés par espace :
    n, m = LI()  # n : nombre de points, m : nombre de requêtes
    # Lecture des coordonnées pour n points. Chaque point a deux entiers (x, y).
    na = [LI() for _ in range(n)]  # na sera une liste de paires [x, y]
    # Initialisation de deux ensembles pour capter les abscisses et ordonnées distinctes :
    xd = set()
    yd = set()
    for x, y in na:
        # Ajoute chaque coordonnée x à l'ensemble xd (pour unicité)
        xd.add(x)
        # Idem pour y, dans yd
        yd.add(y)
    # Trie et convertit les ensembles xd, yd en listes triées.
    xl = sorted(list(xd))  # Liste triée des abscisses uniques
    yl = sorted(list(yd))  # Liste triée des ordonnées uniques
    # Création de dictionnaires de compression de coordonnées.
    xx = {}  # Clef : valeur originale, Valeur : index compressé dans xl
    yy = {}  # Idem pour y
    for i in range(len(xl)):
        xx[xl[i]] = i  # Pour chaque valeur x, on stocke son rang/index dans la liste triée
    for i in range(len(yl)):
        yy[yl[i]] = i
    # Création d'une matrice a de dimensions (|xl|+1) x (|yl|+1), remplie de zéros.
    # On ajoute +1 pour éviter les problèmes d'indice bordure lors du cumulatif.
    a = [[0] * (len(yl) + 1) for _ in range(len(xl) + 1)]
    # Incrémentation de chaque point sur sa version compressée.
    for x, y in na:
        a[xx[x]][yy[y]] += 1  # Place +1 à la position compressée correspondante
    # Instanciation d'une classe pour le cumulatif (somme 2D).
    rui = Ruiwa(a)
    # Liste pour stocker les résultats des m requêtes
    r = []
    for _ in range(m):
        # Pour chaque requête, lire les bornes du rectangle [x1, y1, x2, y2]
        x1, y1, x2, y2 = LI()
        # Conversion de ces coordonnées en index compressés
        # Pour le bord gauche (>= x1) et supérieur (>= y1), utiliser bisect_left pour trouver le premier index >=
        xx1 = bisect.bisect_left(xl, x1)
        yy1 = bisect.bisect_left(yl, y1)
        # Pour le bord droit (<= x2) et inférieur (<= y2), utiliser bisect pour dépasser x2 puis reculer de 1.
        xx2 = bisect.bisect(xl, x2) - 1
        yy2 = bisect.bisect(yl, y2) - 1
        # Recherche la somme des points dans le rectangle demandé, selon les indices compressés.
        res = rui.search(yy1, xx1, yy2, xx2)
        # Ajoute le résultat à la liste des réponses.
        r.append(res)
    # Formate les résultats dans une chaîne, un résultat par ligne.
    return '\n'.join(map(str, r))

# Exécute la fonction principale et affiche son résultat final.
print(main())