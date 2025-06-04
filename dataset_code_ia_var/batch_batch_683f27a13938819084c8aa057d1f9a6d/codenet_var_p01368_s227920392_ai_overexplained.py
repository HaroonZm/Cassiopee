import math  # Importe le module mathématique fondamental, pour des opérations comme racine carrée, sinus, etc.
import string  # Importe le module string qui contient des constantes et fonctions pour manipuler les chaînes de caractères (lettres, chiffres…)
import itertools  # Permet de créer des itérateurs efficaces (produit cartésien, permutations, etc.)
import fractions  # Permet de manipuler des fractions exactes (rationnelles) plutôt que des flottants
import heapq  # Fournit une structure de données de file de priorité (tas binaire, heap)
import collections  # Fournit des types spécialisés de collections (dict avec valeurs par défaut, tuples nommés…)
import re  # Fournit les expressions régulières pour manipuler et rechercher dans des chaînes de caractères
import array  # Tableau de données efficace (plus compact qu’une liste Python)
import bisect  # Fournit des fonctions pour chercher et insérer efficacement dans des listes triées
import sys  # Permet d’interagir avec l’environnement Python (entrées/sorties, etc.)
import random  # Génération de nombres pseudo-aléatoires
import time  # Gérer le temps (temps système, pauses, etc.)
import copy  # Fournit des fonctions pour copier des objets (shallow ou deep copy)
import functools  # Fournit des fonctions pour travailler avec des fonctions (partial, reduce, lru_cache, etc.)

# Modifie la limite de récursion pour les fonctions récursives afin de permettre plus d'appels imbriqués.
sys.setrecursionlimit(10 ** 7)  # 10 millions

# Définition d’une valeur d’infini “pratique” car math.inf ne fonctionne pas dans tous les contextes d’utilisateurs
inf = 10 ** 20  # Un nombre très grand utilisé pour représenter l'infini dans les algorithmes de graphe

# Petite valeur epsilon pour comparaison entre flottants (précision, évite les soucis d’arrondi)
eps = 1.0 / 10 ** 13  # Très petite valeur, utile pour la comparaison de nombres flottants

# Déclaration du modulo utilisé dans beaucoup de problèmes de programmation modulaire (souvent utilisé pour éviter overflow)
mod = 10 ** 9 + 7  # Un nombre premier très utilisé dans de nombreux problèmes de programmation compétitive

# “dd” est une liste de directions de mouvement de base : haut, droite, bas, gauche (pour se déplacer dans une grille)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Vecteurs de déplacement cardinal

# “ddn” est la liste de directions de mouvement pour les 8 directions (cardinales et diagonales)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 8 directions dans une grille

# Définit une fonction LI qui lit une ligne de l’entrée standard et convertit chaque élément en entier
def LI():
    # sys.stdin.readline() lit une chaîne depuis l'entrée
    # .split() divise cette chaîne par espace
    # int(x) convertit chaque morceau en nombre entier
    return [int(x) for x in sys.stdin.readline().split()]

# Identique à LI mais réduit chaque entier de 1 (utile pour convertir des indices 1-based en indices 0-based)
def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

# Lis une ligne et convertit chaque élément en nombre flottant
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lis une ligne et la coupe en mots (chaîne de caractères)
def LS():
    return sys.stdin.readline().split()

# Lis un entier seul depuis l’entrée standard
def I():
    return int(sys.stdin.readline())

# Lis un flottant seul depuis l’entrée standard
def F():
    return float(sys.stdin.readline())

# Lis une ligne depuis l’entrée standard (équivaut à input())
def S():
    return input()

# Fonction pour imprimer une valeur puis forcer la vidange du buffer de sortie (utile pour les problèmes interactifs)
def pf(s):
    return print(s, flush=True)

# Classe qui implémente l’algorithme de Warshall-Floyd, c’est-à-dire l’algorithme de Floyd-Warshall pour trouver les plus courts chemins entre tous les couples de sommets dans un graphe pondéré
class WarshallFloyd():
    # Constructeur de la classe, il prend le graphe sous forme de dictionnaire d'adjacence (e) et le nombre de sommets (n)
    def __init__(self, e, n):
        self.E = e  # Graphe (dictionnaire) ou chaque clé est un sommet, et la valeur est une liste des arêtes issues de ce sommet
        self.N = n  # Nombre total de sommets dans le graphe

    # Méthode principale de recherche des plus courts chemins entre tous les sommets
    def search(self):
        n = self.N  # Nombre de sommets
        nl = list(range(n))  # Liste de tous les indices de sommet (de 0 à n-1)
        # Crée une matrice distances 'd' de taille n x n initialisée à l'infini
        d = [[inf] * n for _ in nl]
        # Distance de chaque sommet à lui-même est 0
        for i in range(n):
            d[i][i] = 0
        # Remplit la matrice d’après les arêtes du graphe
        for k, v in self.E.items():  # Pour chaque sommet k, parcours la liste de ses voisins et leur distance
            dk = d[k]
            for b, c in v:  # b = voisin, c = coût/distance
                # Traite les doublons : si plusieurs arêtes, garde le coût minimal
                if dk[b] > c:
                    dk[b] = c
        # Triplement imbriqué (Floyd-Warshall classique) pour trouver tous les plus courts chemins
        for i in nl:  # Pour chaque point de départ
            di = d[i]  # Ligne i de la matrice
            for j in nl:  # Pour chaque point d’arrivée
                if i == j:
                    continue  # Distance à soi-même déjà gérée
                dj = d[j]  # Ligne j de la matrice
                for k in nl:  # Pour chaque possible sommet intermédiaire
                    # S'il n'est pas de départ ni d'arrivée et améliore le chemin, actualise la distance
                    if i != k and j != k and dj[k] > dj[i] + di[k]:
                        dj[k] = dj[i] + di[k]
        # Retourne la matrice complète des plus courts chemins
        return d

# Classe Flow pour calcul du flot maximum par une méthode simple basée sur DFS (Depth-First Search)
class Flow():
    # Constructeur, prend la représentation du graphe (e) et le nombre de sommets (N)
    def __init__(self, e, N):
        self.E = e  # Graphe, chaque clé est un sommet, chaque valeur est un set/liste des voisins accessibles
        self.N = N  # Nombre total de sommets
        self.nl = list(range(N))  # Liste des indices de sommet (non utilisée ici mais définie)

    # Méthode de calcul du flot maximum entre s (source) et t (puits/sink)
    def max_flow(self, s, t):
        r = 0  # Variable pour stocker le flot total trouvé
        e = self.E  # Référence locale au graphe (pour plus de lisibilité/performance)
        v = None  # Vecteur de visites (sera un tableau booléen pour marquer les sommets visités lors du DFS)

        # Fonction récursive DFS qui cherche un chemin de la source à la cible sans repasser sur les sommets
        def f(c):
            v[c] = 1  # Marque le sommet courant comme visité
            if c == t:  # Si on atteint le puits, on a trouvé un chemin
                return 1  # Retourne 1 pour signifier un chemin trouvé
            for i in list(e[c]):  # Parcours tous les voisins accessibles depuis c (copie pour permettre modification)
                if v[i] is None and f(i):  # Si le voisin n’est pas visité et qu’il existe un chemin depuis i vers le puits
                    e[c].remove(i)  # Retire le chemin (marque comme saturé/occupé)
                    e[i].add(c)  # Ajoute le chemin inverse (permet la réutilisation dans les cycles)
                    return 1  # Retourne 1 pour signifier le succès
            return  # Aucun chemin trouvé

        # Répète jusqu’à ce qu’aucun nouveau chemin n’existe de s à t
        while True:
            v = [None] * self.N  # Initialise un tableau de visite pour chaque recherche de chemin
            if f(s) is None:  # Si aucun chemin n’a été trouvé, on arrête
                break
            r += 1  # Sinon, on incrémente le flot total (un chemin supplémentaire trouvé)

        return r  # Retourne le flot maximum trouvé

# Fonction principale contrôlant la logique du programme
def main():
    rr = []  # Initialize une liste 'rr' pour stocker les résultats de chaque cas traité

    # Fonction f réalise le calcul principal pour un ensemble donné de paramètres n, m, l
    def f(n, m, l):
        # Lit les m arêtes et crée la liste ma (chaque arête est décrite par 3 entiers : u, v, d)
        ma = [LI() for _ in range(m)]
        # Lit les l demandes ou points particuliers à traiter
        la = [LI() for _ in range(l)]
        # Crée le graphe sous forme de dictionnaire d'adjacence pour les sommets
        e = collections.defaultdict(list)
        # Remplit la structure de graphe avec chaque arête lue précédemment (bidirectionnelle)
        for u, v, d in ma:
            e[u].append((v, d))
            e[v].append((u, d))
        # Initialise une instance de l’algorithme Floyd-Warshall pour obtenir toutes les plus courtes distances
        wf = WarshallFloyd(e, n)
        wd = wf.search()
        # Prépare un nouveau graphe pour le flot maximal
        e2 = collections.defaultdict(set)
        # Pour chaque paire de points dans la liste la, on établit des arêtes dans le graphe du flot maximal si la contrainte de temps est respectée
        for i in range(l):
            p1, t1 = la[i]
            for j in range(l):
                if i == j:
                    continue  # Ignore les boucles sur soi-même
                p2, t2 = la[j]
                # Vérifie que le chemin respecte la contrainte temporelle
                if wd[p1][p2] <= t2 - t1:
                    e2[i].add(j + l)  # Ajoute une arête de i vers j décalé de l
            e2[l * 2].add(i)  # Connecte la super-source à tous les sommets d’entrée
            e2[i + l].add(l * 2 + 1)  # Connecte tous les sommets de sortie à la super-puits
        # Crée une instance de flot maximal avec le graphe e2 et la taille adaptée
        fl = Flow(e2, l * 2 + 2)
        t = fl.max_flow(l * 2, l * 2 + 1)  # Cherche le flot de la super-source à la super-puits
        # Retourne le résultat, i.e. le nombre de demandes non satisfaites (l – nombre de flux satisfaits)
        return l - t

    # Boucle pour traiter plusieurs cas jusqu’à ce qu’on rencontre n = 0 (entrée “sentinelle” pour terminer)
    while 1:
        n, m, l = LI()  # Lit trois entiers depuis la ligne de l'entrée standard
        if n == 0:
            break  # Si n vaut 0, on termine le traitement (fin des cas de test)
        rr.append(f(n, m, l))  # Applique la fonction f sur cette entrée et stocke le résultat
    # Retourne sous forme de chaîne (séparée par nouvelle ligne) l’ensemble des résultats calculés
    return '\n'.join(map(str, rr))

# Lance la fonction principale et affiche le résultat final sur la sortie standard
print(main())  # Affiche l’ensemble des réponses calculées, une par ligne, pour tous les cas lus