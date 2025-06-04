import math  # Fournit des fonctions mathématiques standard.
import string  # Fournit des fonctions pour manipuler des chaînes de caractères (ex : alphabet).
import itertools  # Fournit des fonctions pour générer des itérateurs pour boucles efficaces.
import fractions  # Permet de travailler avec des fractions rationnelles.
import heapq  # Fournit des fonctions pour manipuler des files de priorité (heaps).
import collections  # Fournit des types de données utilitaires comme deque, Counter, etc.
import re  # Module permettant de travailler avec les expressions régulières.
import array  # Permet de créer des tableaux d'éléments typés (plus compacts que les listes).
import bisect  # Fournit des fonctions pour la recherche et l'insertion dans des listes triées.
import sys  # Permet d'interagir avec l'environnement d'exécution Python (entrée/sortie, arguments...).
import random  # Permet de générer des nombres aléatoires.
import time  # Permet de travailler avec le temps (dates, pauses, etc.).
import copy  # Fournit des fonctions pour copier des objets (shallow et deep copy).
import functools  # Fournit des utilitaires de programmation fonctionnelle, comme les décorateurs.

# Modifie la limite de récursion maximale de Python. Par défaut c'est 1000.
# Cela permet d'appeler une fonction jusqu'à 10 millions de fois avant d'atteindre la limite.
sys.setrecursionlimit(10**7)

# Définit une valeur qui sera utilisée pour représenter un « infini »,
# ici 10^20, une très grande valeur.
inf = 10**20

# Définit « epsilon », un petit nombre pour comparer des nombres à virgule flottante.
eps = 1.0 / 10**13

# Définit le modulo à utiliser pour des opérations arithmétiques, commun dans les problèmes d'algorithmie.
mod = 10**9+7

# Crée une liste de tuples représentant les 4 directions cardinales (haut, droite, bas, gauche),
# -1 signifie aller vers le haut ou vers la gauche, +1 vers le bas ou la droite, 0 signifie aucune modification.
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Crée une liste de tuples représentant les 8 directions (haut, haut-droite, droite, bas-droite, bas, bas-gauche, gauche, haut-gauche)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# ----- Définition de fonctions utilitaires pour lire les entrées -----

# Lit une ligne depuis l'entrée standard, coupe selon les espaces et convertit chaque groupe en entier.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Similaire à LI(), mais décrémente chaque entier obtenu de 1 (utile pour les indices commençant à 0).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Lit une ligne et transforme chaque groupe en nombre à virgule flottante.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne et renvoie les éléments séparés par espace sous forme de liste de chaînes.
def LS():
    return sys.stdin.readline().split()

# Lit une ligne, la convertit en entier (utile pour une entrée numérique unique sur une ligne).
def I():
    return int(sys.stdin.readline())

# Lit une ligne, la convertit en flottant.
def F():
    return float(sys.stdin.readline())

# Lit une entrée utilisateur (jusqu'à retour-chariot) en tant que chaîne (équivalent à input()).
def S():
    return input()

# Affiche une chaîne et force le vidage du tampon d'affichage (utile pour les juges interactifs).
def pf(s):
    return print(s, flush=True)

# ----- Début de la fonction principale -----
def main():
    # Initialise une liste vide qui va accueillir les résultats pour chaque jeu de données.
    rr = []

    # Définit la fonction de résolution principale, prenant comme argument n
    def f(n):
        # Lit une ligne de l'entrée et la découpe en mots (normalement 2 mots : a et b)
        a, b = LS()

        # Si a et b sont égaux, on retourne 0, car aucune opération n'est nécessaire
        if a == b:
            return 0

        # Transforme la chaîne 'a' en liste d'entiers, chaque chiffre étant un élément de la liste
        a = [int(c) for c in a]
        # Idem pour 'b'
        b = [int(c) for c in b]

        # Crée une liste qui contient uniquement la liste a (dans une liste, car on travaillera avec plusieurs)
        aa = [a]

        # Crée un set ad pour garder en mémoire toutes les versions de 'a' déjà rencontrées,
        # afin d'éviter des boucles ou des répétitions inutiles lors de la transformation.
        # On transforme chaque a en tuple pour qu’il soit stockable dans un set.
        ad = set()
        ad.add(tuple(a))

        # Initialise un compteur pour compter le nombre d'opérations (étapes) effectuées
        r = 0

        # Commence une boucle infinie qui va s'arrêter lorsqu'on aura trouvé la solution
        while True:
            # À chaque tour, on incrémente le nombre d'étapes
            r += 1

            # Crée une nouvelle liste temporaire pour stocker les nouveaux candidats générés à cette étape
            na = []

            # On parcourt toutes les séquences 'a' candidates obtenues à l'étape précédente
            for a in aa:
                # Initialise un indice ti à 0 ; il va servir à pointer sur le premier chiffre de a qui diffère de b à partir de l'étape en cours
                ti = 0

                # Parcourt les indices de la position r-1 (qui augmente à chaque itération) jusqu'à la fin du nombre (excluant le dernier), pour trouver la première différence
                for i in range(r-1, n):
                    # Si le ième chiffre de a est différent de celui de b
                    if a[i] != b[i]:
                        # On enregistre cet indice
                        ti = i
                        # On quitte la boucle dès qu'on trouve la première différence
                        break

                # Calcule la différence entre le chiffre correspondant de b et celui de a à cette position.
                sa = b[ti] - a[ti]

                # Pour chaque longueur de segment possible partant de ti (on va de ti+1 jusqu'à n inclus),
                # on va appliquer la transformation à ce segment.
                for j in range(ti+1, n+1):
                    # Crée une nouvelle liste t à partir de a.
                    # Si l'indice i est compris entre ti (inclus) et j (exclus), on ajoute la différence sa à a[i] modulo 10 (pour garantir un chiffre).
                    # Sinon, a[i] reste inchangé.
                    t = [(a[i] + sa) % 10 if ti <= i < j else a[i] for i in range(n)]

                    # Transforme la liste t en tuple pour pouvoir la stocker dans un set (ensemble)
                    k = tuple(t)

                    # Si on a déjà rencontré cette configuration, on saute cette transformation
                    if k in ad:
                        continue

                    # Si la nouvelle séquence t est identique à la cible b, on retourne le nombre d'opérations r
                    if t == b:
                        return r

                    # Sinon, on marque cette séquence comme déjà vue
                    ad.add(k)
                    # Et on l'ajoute à la liste des candidats pour la prochaine étape
                    na.append(t)

            # On met à jour la liste aa avec tous les nouveaux candidats générés à cette étape
            aa = na

    # Démarre une boucle infinie pour lire chaque jeu de données, un par un, jusqu'à rencontrer un zéro (fin de saisie)
    while True:
        # On lit la valeur de n (longueur du nombre), attendue sur une ligne seule
        n = I()
        # Si n vaut zéro, c'est la condition d'arrêt : on sort de la boucle
        if n == 0:
            break
        # Sinon, on applique la fonction f à ce jeu de données de longueur n, et on stocke le résultat dans la liste rr
        rr.append(f(n))

    # Après avoir traité tous les jeux de données, on transforme chaque résultat en chaîne de caractères,
    # puis on les joint tous ensemble avec un saut de ligne, pour former la sortie finale (une ligne par cas)
    return '\n'.join(map(str, rr))

# Appelle la fonction principale et affiche le résultat
print(main())