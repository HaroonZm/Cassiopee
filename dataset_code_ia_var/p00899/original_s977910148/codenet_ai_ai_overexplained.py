# Importation de tous les modules nécessaires pour certaines fonctions mathématiques, manipulations de chaînes, structures de données, etc.
import math  # Fournit des fonctions mathématiques comme les racines carrées, les puissances, etc.
import string  # Fournit des opérations utiles sur les chaînes de caractères, comme ascii_letters.
import itertools  # Fournit des outils pour créer et manipuler des itérateurs.
import fractions  # Permet de manipuler les fractions (nombres rationnels).
import heapq  # Fournit une implémentation efficace de la file de priorité (heap).
import collections  # Fournit des structures de données haut niveau (deque, defaultdict, etc.).
import re  # Fournit des opérations de traitement des expressions régulières.
import array  # Fournit un espace mémoire efficient pour stocker des tableaux de valeurs numériques.
import bisect  # Permet la recherche et l'insertion dans des listes triées.
import sys  # Fournit un accès direct à certaines variables utilisées ou maintenues par l’interpréteur Python.
import random  # Fournit des fonctions générant des nombres aléatoires.
import time  # Fournit des fonctions pour travailler avec le temps.
import copy  # Permet de faire des copies superficielles et profondes d'objets.
import functools  # Fournit des outils pour la programmation fonctionnelle.

# Définit la limite maximale de récursion pour éviter l'erreur de récursion dans les appels récursifs profonds.
sys.setrecursionlimit(10**7)
# Initialise une constante représentant une valeur "infinie" pour certains algorithmes nécessitant une telle valeur.
inf = 10**20
# Définit un epsilon, petite valeur pour la comparaison de flottants (pour vérifier l'égalité approximative).
eps = 1.0 / 10**10
# Définit un module premier très utilisé dans les problèmes de programmation compétitive, par exemple pour éviter les débordements d'entiers.
mod = 10**9+7
# Liste représentant les 4 directions cardinales (haut, droite, bas, gauche) pour les déplacements sur une grille.
dd = [(-1,0),(0,1),(1,0),(0,-1)]
# Liste représentant les 8 directions (y compris les diagonales) pour les déplacements sur une grille.
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonctions utilitaires pour la lecture des entrées
def LI():
    # Lit une ligne de l'entrée standard, la sépare par des espaces et convertit chaque élément en entier.
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Comme LI(), mais soustrait 1 à chaque entier (utile pour passer de 1-indexé à 0-indexé).
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    # Lit une ligne, splitte et convertit en flottants.
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lit une ligne, splitte en sous-chaînes séparées par des espaces.
    return sys.stdin.readline().split()

def I():
    # Lit une ligne et la convertit en entier.
    return int(sys.stdin.readline())

def F():
    # Lit une ligne et la convertit en float.
    return float(sys.stdin.readline())

def S():
    # Utilise la fonction input() pour obtenir une chaîne de caractères depuis l'utilisateur.
    return input()

def pf(s):
    # Imprime une chaîne et force le flush du tampon de sortie pour affichage immédiat.
    return print(s, flush=True)

# Fonction utilitaire aidant à déterminer si deux segments de droite s'intersectent (partie d'un test d'intersection).
def _kosa(a1, a2, b1, b2):
    # Décompresse les coordonnées (x, y, _) pour chaque point (le troisième élément est ignoré ici).
    x1, y1, _ = a1
    x2, y2, _ = a2
    x3, y3, _ = b1
    x4, y4, _ = b2

    # Calcule une forme de produit vectoriel pour déterminer de quel côté du segment se situent les autres points.
    tc = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    td = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    # Si les produits ont des signes opposés, les points sont de chaque côté de l'autre segment.
    return tc * td < 0

# Fonction qui détermine si les deux segments de droite (a1-a2) et (b1-b2) s'intersectent.
def kosa(a1, a2, b1, b2):
    # Les deux segments doivent "se croiser" mutuellement.
    return _kosa(a1, a2, b1, b2) and _kosa(b1, b2, a1, a2)

# Calcule la distance euclidienne entre deux points (x1, y1) et (x2, y2).
def distance(x1, y1, x2, y2):
    # Calcule la racine carrée de la somme des carrés des différences des coordonnées (théorème de Pythagore).
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calcule la distance minimale entre un point et un segment défini par deux points dans le plan 2D.
def distance3(p1, p2, p3):
    # Décompresse les coordonnées pour chaque point (on ignore le troisième élément).
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = p3

    # Calcul des vecteurs ax (segment p1-p2) et bx (segment p1-p3) dans le plan.
    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    # Calcule le rapport du produit scalaire sur la longueur au carré du segment.
    # Ceci donne la position du projeté orthogonal de p3 sur le segment p1-p2.
    r = (ax * bx + ay * by) / (ax * ax + ay * ay)

    # Si le projeté est en dehors du segment du côté de p1, retourne la distance de p3 à p1.
    if r <= 0:
        return distance(x1, y1, x3, y3)
    # Si le projeté est en dehors du segment du côté de p2, retourne la distance de p3 à p2.
    if r >= 1:
        return distance(x2, y2, x3, y3)
    # Sinon, la distance minimale de p3 au segment est la distance du projeté à p3.
    return distance(x1 + r * ax, y1 + r * ay, x3, y3)

# Fonction principale du programme
def main():
    # Création d'une liste vide 'rr' pour stocker les résultats de chaque test/instance.
    rr = []

    # Définition d'une fonction interne f prenant un entier n.
    def f(n):
        # Lecture de n chaînes de caractères via la fonction S().
        a = [S() for _ in range(n)]

        # 'b' contiendra les chaînes de 'a' qui ne sont pas sous-chaînes de toute autre chaîne de a.
        b = []
        for i in range(n):
            # On suppose d'abord que la chaîne courante 'a[i]' n'est pas contenue dans une autre.
            f = True
            for j in range(n):
                # On ne compare pas une chaîne avec elle-même.
                if i == j:
                    continue
                # Si 'a[i]' est une sous-chaîne de 'a[j]', on la retire.
                if a[i] in a[j]:
                    f = False
                    break
            # Si la chaîne 'a[i]' n'était dans aucun 'a[j]', elle est ajoutée à 'b'.
            if f:
                b.append(a[i])
        # Mise à jour de a, et ajustement de n à la taille de b.
        a = b
        n = len(b)

        # Construction d'une matrice d'adjacence 'd' telle que d[i][j] correspond au chevauchement maximal
        # entre la fin de a[i] et le début de a[j].
        d = [[0] * n for _ in range(n)]
        for i in range(n):
            ai = a[i]
            for j in range(n):
                if i == j:
                    continue
                aj = a[j]
                # On compare tous les suffixes de ai avec les préfixes de aj pour trouver le plus long chevauchement.
                for k in range(1, min(len(ai), len(aj))):
                    # Si le suffixe de taille k de ai égale le préfixe de taille k de aj.
                    if ai[-k:] == aj[:k]:
                        d[i][j] = k

        # ii contient 2 à la puissance i pour chaque i de 0 à n-1. Cela servira pour le masquage de bits.
        ii = [2**i for i in range(n)]
        # Création d'un dictionnaire avec clé (état, index) et valeur le chevauchement maximal.
        q = collections.defaultdict(int)
        for i in range(n):
            # On initialise q avec chaque chaîne prise seule (chaque bit du masque allumé individuellement).
            q[(ii[i], i)] = 0

        # Boucle du programme principal utilisant une approche DP sur les sous-ensembles (type TSP + overlaps).
        for _ in range(n-1):
            # nq stockera les états du prochain tour (profondeur du DP).
            nq = collections.defaultdict(int)
            for i in range(n):
                t = ii[i]  # Bit correspondant à la i-ème chaîne.
                for k, v in q.items():
                    # Si la i-ème chaîne est déjà utilisée dans l'état/masque courant, on saute.
                    if k[0] & t:
                        continue
                    # Ajoute la chaîne i à l'état/masque courant (k[0]) et termine le chemin par i.
                    key = (k[0] | t, i)
                    # Ajoute le chevauchement du dernier élément utilisé jusqu'à présent et la chaîne i.
                    nv = v + d[k[1]][i]
                    # On garde seulement la valeur maximale trouvée pour cet état.
                    if nq[key] < nv:
                        nq[key] = nv
            # On passe à l'état suivant.
            q = nq

        # fr sera la valeur maximale parmi tous les masques finaux, i.e. le max du chevauchement possible.
        fr = max(q.values())
        # On soustrait le total du chevauchement maximal à la somme des longueurs pour obtenir la longueur minimale du supertexte "concaténé". 
        return sum(map(len, a)) - fr

    # Boucle infinie pour traiter plusieurs instances (par exemple, lignes d'entrée successives).
    while True:
        n = I()  # Récupère le nombre de chaînes pour ce cas de test.
        if n == 0:
            # Si n vaut 0, cela signifie qu'il n'y a plus de cas à traiter.
            break
        # Ajoute le résultat de f(n) à la liste rr.
        rr.append(f(n))
        # La ligne suivante (commentée) permettrait d'afficher le n et le résultat (debug).
        # print(n, rr[-1])

    # Combine tous les résultats en une seule chaîne de caractères, avec un saut de ligne entre chaque.
    return '\n'.join(map(str, rr))

# Exécute la fonction main et affiche son résultat à l'écran.
print(main())