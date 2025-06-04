# Importation de nombreux modules standards Python, même si tous ne seront probablement pas utilisés dans ce script.
import math     # Bibliothèque pour fonctions mathématiques telles que sqrt, pow, trigonométrie, etc.
import string   # Fournit des outils et constantes pour manipuler du texte, comme les lettres de l'alphabet.
import itertools # Permet de créer des itérateurs sophistiqués (permutations, combinaisons, produits cartésiens, etc.)
import fractions # Offre des objets Fraction pour un calcul rationnel exact.
import heapq    # Fournit des outils pour manipuler des files de priorité (heaps).
import collections # Contient des types de container spécialisés (deque, Counter, etc.)
import re       # Sert à gérer les expressions régulières.
import array    # Fournit un tableau efficace d'éléments de type fixe.
import bisect   # Pour insérer/chercher efficacement dans une liste triée.
import sys      # Fournit des fonctions pour manipuler l'I/O bas niveau (stdin, stdout) et le système Python.
import random   # Génération de nombres aléatoires.
import time     # Gère les fonctions liées au temps.
import copy     # Pour effectuer des copies superficielles/profondes d'objets.
import functools # Fournit des outils pour manipuler des fonctions (comme reduce, partial, etc.)

# Modifie la limite de récursion maximale du programme.
# Par défaut, elle est assez basse; ici elle est changée à 10^7 (dix millions).
sys.setrecursionlimit(10**7)

# Définition d'une constante pour représenter l'infini, une valeur très grande.
inf = 10**20

# Une petite valeur epsilon qui peut servir pour comparer des nombres flottants
eps = 1.0 / 10**13

# Définition d'un modulo, souvent utilisé lors de calculs de grandes valeurs pour éviter le dépassement de capacité.
mod = 10**9+7

# dd contient les 4 directions principales adjacentes (haut, droite, bas, gauche) dans une grille (coordonnées relatives).
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # (haut, droite, bas, gauche)

# ddn contient les 8 directions adjacentes (y compris les diagonales).
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Définition de petites fonctions utilitaires pour gérer la lecture et l'analyse de l'entrée standard.

# Fonction LI() : lit une ligne depuis stdin, la découpe sur les espaces, convertit chaque élément en entier et retourne la liste résultante.
def LI(): 
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction LI_() : comme LI(), mais décrémente chaque entier de 1 (utile pour les indexations 0-based).
def LI_(): 
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction LF() : lit une ligne, convertit chaque élément en flottant et retourne la liste.
def LF(): 
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction LS() : lit une ligne, la découpe en mots (séparés par des espaces), retourne la liste de chaînes de caractères.
def LS(): 
    return sys.stdin.readline().split()

# Fonction I() : lit une ligne, convertit la chaîne en entier.
def I(): 
    return int(sys.stdin.readline())

# Fonction F() : lit une ligne, convertit la chaîne en nombre flottant.
def F(): 
    return float(sys.stdin.readline())

# Fonction S() : lit une ligne en utilisant simplement input().
def S(): 
    return input()

# Fonction pf(s) : imprime s et force immédiatement l'affichage du buffer (flush=True).
def pf(s): 
    return print(s, flush=True)

# Définition d'une classe pour représenter une arête d'un graphe à flot (réseau de transport).

class Edge():
    # Constructeur de la classe Edge. Les paramètres sont :
    # t : sommet d'arrivée ("to")
    # f : sommet d'origine ("from")
    # r : indice de l'arête inverse dans la liste d'adjacence du sommet "to"
    # ca : capacité de cette arête (combien de flux elle peut transporter)
    # co : coût d'utiliser cette arête (peut-être négatif)
    def __init__(self, t, f, r, ca, co):
        self.to = t       # Vers quel sommet l'arête va
        self.fron = f     # De quel sommet elle provient (on garde "fron" pour la compatibilité)
        self.rev = r      # Indice de l'arête inverse (utilisé pour gérer le flot résiduel)
        self.cap = ca     # Capacité maximale de transport de flux
        self.cost = co    # Coût associé à ce flux

# Classe pour résoudre le problème du flot de coût minimum (problème de transport à coût minimal)
class MinCostFlow():
    # size : nombre de sommets dans le graphe
    # graph : liste d'adjacence représentant le graphe ; chaque sommet contient la liste de ses arêtes sortantes

    size = 0   # Initialise le nombre de sommets à zéro (sera redéfini dans __init__)
    graph = [] # Initialise la liste d'adjacence vide

    # Constructeur, prend la taille (nombre de sommets) du graphe
    def __init__(self, s):
        self.size = s
        # Pour chaque sommet, on prépare une liste (vide) d'arêtes sortantes
        self.graph = [[] for _ in range(s)]

    # Ajoute une arête au graphe, de f à t, avec capacité ca et coût co.
    # Crée aussi l'arête résiduelle correspondante de t à f (coût négatif et capacité zéro).
    def add_edge(self, f, t, ca, co):
        # Ajoute une arête "directe" de f à t
        self.graph[f].append(Edge(t, f, len(self.graph[t]), ca, co))
        # Ajoute l'arête "résiduelle" (inverse) de t à f
        self.graph[t].append(Edge(f, t, len(self.graph[f])-1, 0, -co))

    # Recherche le chemin de coût minimal, avec possibilité d'augmentation de flux, du sommet s au sommet t.
    def min_path(self, s, t):
        # Initialise la distance minimale pour atteindre chaque sommet à l'infini.
        dist = [inf] * self.size

        # route[v] contiendra l'arête utilisée pour atteindre le sommet v sur le chemin optimal
        route = [None] * self.size

        # On utilise une file pour le parcours BFS (Breadth-First Search), ici, une deque (double-ended queue)
        que = collections.deque()

        # inq[v] est True si le sommet v est actuellement dans la file (pour éviter d'ajouter plusieurs fois le même sommet)
        inq = [False] * self.size

        # Distance initiale pour la source s est 0
        dist[s] = 0

        # On commence le BFS à partir du sommet source s
        que.append(s)
        inq[s] = True

        # Parcours en largeur modifié pour trouver le plus court chemin en coût (pas en nombre d'arêtes)
        while que:
            u = que.popleft()
            inq[u] = False
            # On parcourt toutes les arêtes sortantes du sommet u
            for e in self.graph[u]:
                # On ne considère que les arêtes avec capacité positive (flux possible)
                if e.cap == 0:
                    continue
                v = e.to
                # Mise à jour de la distance si on trouve un chemin de coût moindre
                if dist[v] > dist[u] + e.cost:
                    dist[v] = dist[u] + e.cost
                    route[v] = e # On enregistre l'arête menant à v
                    # Si v n'est pas déjà dans la file, on l'y ajoute
                    if not inq[v]:
                        que.append(v)
                        inq[v] = True

        # Si on n'a pas pu atteindre le sommet destination t, c'est que le flot n'est plus augmentable, on retourne inf
        if dist[t] == inf:
            return inf

        # On cherche la capacité résiduelle minimale (le "goulot d'étranglement") sur le chemin trouvé
        flow = inf
        v = t
        while v != s:
            e = route[v]
            if flow > e.cap:
                flow = e.cap
            v = e.fron # On remonte le chemin vers la source

        # On applique le flux sur le chemin trouvé (on "pousse" flow unités)
        c = 0    # Variable pour calculer le coût total appliqué pendant ce chemin
        v = t
        while v != s:
            e = route[v]
            # On réduit la capacité résiduelle sur chaque arête du chemin
            e.cap -= flow
            # On augmente la capacité sur l'arête inverse (pour le flot résiduel)
            self.graph[e.to][e.rev].cap += flow
            # On ajoute le coût correspondant
            c += e.cost * flow
            v = e.fron

        # Retourne la distance/coût globale du chemin trouvé (c'est la distance finale pour t)
        return dist[t]

    # Fonction pour exécuter sur le graphe la recherche du flot de coût minimal entre s et t afin d'envoyer "flow" unités.
    def calc_min_cost_flow(self, s, t, flow):
        total_cost = 0 # Coût total initialisé à zéro
        # On itère autant de fois que d'unités de flow à faire circuler
        for i in range(flow):
            c = self.min_path(s, t) # Recherche du plus court chemin coût pour une unité de flow
            if c == inf:
                # Si on ne peut plus pousser de flux, on retourne tout de suite
                return c
            total_cost += c # On accumule le coût de chaque unité de flux envoyée
        # Retourne le coût total pour envoyer tout le flux demandé
        return total_cost

# Cette fonction sera exécutée sous forme de script principal
def main():
    # On prépare une liste pour stocker les résultats de chaque instance traitée
    rr = []

    # On définit une sous-fonction f(n) qui va traiter chaque instance, prenant comme paramètre n (nombre de segments/événements)
    def f(n):
        # On lit n listes de 3 entiers (supposément pour définir des intervalles)
        # On trie cette liste par (fin, début, -poids). Cela facilite l'ordre de traitement.
        a = sorted([LI() for _ in range(n)], key=lambda x: [x[1], x[0], -x[2]])
        # On prépare un objet de flot de coût minimal avec 368 sommets (0 à 367 inclus)
        mcf = MinCostFlow(368)
        s = 366 # Sommet source, choisi arbitrairement hors de la plage des "jours"
        t = 367 # Sommet puit, à la suite du dernier

        # On connecte chaque jour du calendrier (ils sont 366 ; du 0 au 365)
        for i in range(1, 366):
            # Entre chaque jour consécutif, on ajoute une arête de capacité 2 et de coût 0
            mcf.add_edge(i-1, i, 2, 0)

        # Pour chaque intervalle (i, j, w) donné par l'entrée :
        for i, j, w in a:
            # On ajoute une arête de i-1 vers j, capacité 1, coût -w (pour maximiser la somme des poids via la minimisation des coûts négatifs)
            mcf.add_edge(i-1, j, 1, -w)

        # On relie la source s au jour 0, capacité 2, coût nul
        mcf.add_edge(s, 0, 2, 0)
        # On relie le dernier jour 365 au puit t
        mcf.add_edge(365, t, 2, 0)

        # On cherche le minimum cost flow de s à t, avec demande de 2 unités de flux
        res = mcf.calc_min_cost_flow(s, t, 2)
        # On retourne l'opposé du résultat (car on avait mis des coûts négatifs pour maximiser la somme initiale)
        return -res

    # Boucle principale : on traite autant d'instances que demandé à l'entrée jusqu'à rencontrer n = 0
    while 1:
        n = I() # On lit un entier
        if n == 0:
            break # Fin de toutes les instances si n vaut zéro
        rr.append(f(n)) # On traite l'instance et on stocke le résultat

    # On convertit tous les résultats en chaînes, les assemble avec des retours à la ligne et on les retourne pour impression.
    return '\n'.join(map(str, rr))

# Ce bloc exécute la fonction main lorsque ce fichier est exécuté directement (par ex : via python mon_prog.py)
print(main())