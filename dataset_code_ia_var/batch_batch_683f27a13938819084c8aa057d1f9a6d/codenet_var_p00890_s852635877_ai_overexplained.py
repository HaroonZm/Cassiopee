import math  # Fournit des fonctions mathématiques de base, comme sqrt, sin, cos, etc.
import string  # Donne des constantes liées aux chaînes de caractères (alphabet, chiffres, etc.)
import itertools  # Fournit des outils pour créer et utiliser des itérateurs efficaces
import fractions  # Permet le calcul avec des fractions (nombres rationnels)
import heapq  # Implémente une file de priorité (tas binaire)
import collections  # Fournit des structures de données comme deque, defaultdict, Counter, etc.
import re  # Module d'expressions régulières pour faire des recherches dans les chaînes de caractères
import array  # Fournit un type de séquence efficace pour les listes de valeurs numériques
import bisect  # Fournit des fonctions pour manipuler les listes triées (recherche, insertion)
import sys  # Permet d'accéder à des fonctionnalités propres à l'interpréteur Python (ex : stdin, stdout)
import random  # Fournit des fonctions de génération de nombres aléatoires
import time  # Permet de manipuler le temps (dates, temporisations, chronos, etc.)
import copy  # Permet de copier des objets (copy superficielle et copy profonde)
import functools  # Fournit des outils pour la programmation fonctionnelle (ex : reduce, lru_cache, etc.)

# Modifie la limite de récursion maximale autorisée (utile pour l'appel récursif profond)
sys.setrecursionlimit(10**7)  # Définit la profondeur maximale de récursion sur dix millions

inf = 10**20  # Variable pour représenter un "infiniment grand" assez pratique pour initialiser des minima
eps = 1.0 / 10**13  # Petite valeur pour comparer la précision des flottants (précision epsilon)
mod = 10**9+7  # Modulo utilisé dans de nombreux problèmes d'arithmétique modulaire (nombre premier)
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # Liste des déplacements possibles en 4 directions (haut, droite, bas, gauche)
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]  # Déplacements dans toutes les directions (8 directions)

# Fonctions utilitaires pour la lecture et le traitement d'entrées issues de sys.stdin

def LI():
    # Lit une ligne, sépare la ligne par espaces, convertit chaque morceau en entier
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Lit une ligne, sépare la ligne par espaces, convertit chaque morceau en entier et soustrait 1 (pour indexer à partir de zéro)
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    # Lit une ligne, sépare la ligne, convertit chaque morceau en flottant
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lit une ligne et renvoie la liste de mots (chaînes séparées par des espaces)
    return sys.stdin.readline().split()

def I():
    # Lit une ligne et convertit cette ligne entière en un seul entier
    return int(sys.stdin.readline())

def F():
    # Lit une ligne et convertit cette ligne entière en un seul nombre flottant
    return float(sys.stdin.readline())

def S():
    # Lit une ligne à partir de l'entrée utilisateur standard (stdin), sans retraitement
    return input()

def pf(s):
    # Affiche la chaîne passée en argument et force l'écriture dans la sortie standard immédiatement (utile sur certains juges en ligne)
    return print(s, flush=True)

def main():
    # Cette fonction principale va exécuter le processus principal du programme
    rr = []  # Crée une liste vide pour stocker les résultats à afficher à la fin

    def f(n, m, c):
        # Fonction interne pour résoudre un sous-problème donné (un cas de test)
        # n : nombre de sommets (noeuds) du graphe
        # m : nombre d'arêtes du graphe
        # c : capacité ou contrainte sur le coût (usage propre au contexte)
        e = collections.defaultdict(list)  # Crée un dictionnaire où chaque clé est initialisée automatiquement à une liste vide

        for _ in range(m):
            # Pour chaque arête, lit trois entiers : a, b, d correspondant au départ, à l'arrivée et à la distance/coût
            a, b, d = LI()
            e[a].append((b, d))  # Ajoute au dictionnaire la connexion de a vers b avec poids d

        def search(s):
            # Fonction interne qui effectue le processus de recherche (style Dijkstra modifié)
            d = collections.defaultdict(lambda: inf)  # Initialise le coût minimum d'arrivée à chaque état à infini
            s = (0, s)  # s ici est un tuple : (nombre d'utilisations spéciales, position actuelle)
            d[s] = 0  # Le coût d'arrivée à l'état de départ est 0
            q = []  # File de priorité implémentée par un tas binaire
            heapq.heappush(q, (0, s))  # Ajoute l'état de départ avec le coût à zéro
            v = collections.defaultdict(bool)  # Un dictionnaire pour retenir si un état a déjà été traité
            r = inf  # Initialise la meilleure réponse trouvée à l'infini

            while len(q):
                # Tant que la file de priorité n'est pas vide, continue
                k, u = heapq.heappop(q)  # Récupère et enlève de la file l'état ayant le coût le plus faible actuellement
                if v[u]:
                    continue  # Si déjà traité, on passe
                v[u] = True  # Marque cet état comme traité
                cc, uu = u  # Décompacte les informations d'état : cc est un compteur et uu la position

                if uu == n and r > cc:
                    # Si on a atteint le noeud terminal (n) et que le compteur cc est meilleur (plus petit)
                    r = cc  # Met à jour la meilleure réponse

                if cc >= r:
                    # Si notre compteur cc n'est pas meilleur que la meilleure réponse trouvée, on arrête là pour cet état
                    continue

                for uv, ud in e[uu]:
                    # Parcours tous les voisins (uv) possibles depuis uu, avec un coût ud

                    if k + ud <= c:
                        # Si additionner le coût courant et le coût de l'arête ne dépasse pas la capacité c
                        vv = (cc, uv)  # Crée un nouvel état en conservant le même compteur, mais en allant en uv
                        vd = k + ud  # Nouveau coût de l'état
                        if not v[vv] and d[vv] > vd:
                            # Si le nouvel état n'a pas été visité, et si le chemin trouvé est meilleur (plus petit coût)
                            d[vv] = vd  # Met à jour le meilleur coût
                            heapq.heappush(q, (vd, vv))  # Ajoute dans la file de priorité

                    if cc < r:
                        # Si le compteur actuel est potentiellement améliorable, on essaye d'utiliser la spécialité (propre au contexte)
                        vv = (cc+1, uv)  # Crée un nouvel état en incrémentant le compteur
                        vd = k  # Le coût ici ne change pas (reste k), l'interprétation dépend du problème
                        if not v[vv] and d[vv] > vd:
                            d[vv] = vd  # Met à jour le coût optimal pour le nouvel état
                            heapq.heappush(q, (vd, vv))  # Ajoute le nouvel état dans la file

            return r  # Retourne la meilleure réponse trouvée

        r = search(1)  # Lance la recherche en partant du sommet 1 (par convention des problèmes)
        return r  # Retourne la réponse pour ce sous-problème

    while 1:
        # Boucle infinie qui lit et traite chaque cas de test successivement jusqu'à la condition d'arrêt
        n, m, c = LI()  # Lit la définition du problème : nombre de sommets, nombre d'arêtes, capacité
        if n == 0:
            # Condition d'arrêt : si la taille du graphe est nulle, on sort
            break
        rr.append(f(n, m, c))  # Calcul et stocke la réponse pour chaque cas de test

    return '\n'.join(map(str, rr))  # Après avoir tout calculé, on assemble les réponses de chaque problème sous forme de chaîne

print(main())  # Lance l'exécution du programme principal et affiche la sortie finale