import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

# Augmente la limite de récursion pour permettre des appels récursifs profonds dans les graphes.
sys.setrecursionlimit(10**7)

# Définition de constantes globales utilisées pour les comparaisons et modules.
inf = 10**20  # Un nombre suffisamment grand représentant l'infini
eps = 1.0 / 10**13  # Précision flottante pour les comparaisons numériques
mod = 10**9 + 9  # Modulo utilisé dans diverses opérations mathématiques (rarement ici)

# Directions de mouvement, utilisé potentiellement pour les parcours de grilles (NON utilisé ici, mais conservé pour contexte)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 4 directions: N, E, S, O
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 8 directions

# Fonctions utilitaires pour lecture d'entrée standard avec typages spécifiques

def LI():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers décrémentés de 1 (pour indices zéro-based).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et retourne une liste de flottants.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et retourne une liste de chaînes (mots séparés par défaut).
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard et retourne un entier.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard et retourne un flottant.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard et retourne une chaîne.
    """
    return input()

def pf(s):
    """
    Affiche la chaîne s avec purge du buffer de sortie.
    """
    return print(s, flush=True)

class Flow:
    """
    Classe pour calculer et manipuler le flot maximal sur un graphe non pondéré orienté.

    Utilise une structure de graphe basée sur des ensembles d'adjacence.
    Permet l'ajout et la suppression dynamique d'arêtes avec recalcul du flot.
    """
    def __init__(self, e, N):
        """
        Initialise la structure du graphe.

        Args:
        - e: dictionnaire ou defaultdict(set) représentant les arêtes (adjacence).
        - N: nombre de nœuds du graphe.
        """
        # Structure permettant de conserver toutes les arêtes jamais ajoutées (utilisée lors des suppressions)
        self.EE = collections.defaultdict(set)
        for i in range(N):
            self.EE[i] |= e[i]
        # Graphe "actuel" (arêtes présentes)
        self.E = e
        self.N = N
        self.nl = list(range(N))  # Liste des nœuds (pour usage éventuel)
        self.R = 0  # Valeur courante du flot maximal

    def max_flow(self, s, t):
        """
        Calcule le flot maximal actuel entre les nœuds s et t, sur le graphe courant.

        Args:
        - s: sommet source
        - t: sommet puits

        Returns:
        - Flot maximal actuel.
        """
        e = self.E

        def f(c):
            """
            Parcourt récursivement depuis le nœud courant pour trouver un chemin augmentant.
            Marque les nœuds visités sur ce parcours.
            Lorsqu'un chemin t est atteint, on retire les arêtes correspondantes (simulant leur saturation).

            Args:
            - c: nœud en cours

            Returns:
            - 1 si un chemin augmenté vers t est trouvé, None sinon.
            """
            v[c] = 1
            if c == t:
                # Arrivé au puits, on a trouvé un chemin augmentant
                return 1
            for i in e[c]:
                if v[i] is None and f(i):
                    # Chemin trouvé via i, suppression ou ajout rétroactif d'arête pour maintenir la structure du flot
                    if c in e[i]:
                        # S'il existe l'arête dans les deux sens, on retire dans le sens courant
                        e[c].remove(i)
                    else:
                        # Sinon, on ajoute un retour (pour la gestion de flot résiduel)
                        e[i].add(c)
                    return 1
            return

        while True:
            # Réinitialise les visites
            v = [None] * self.N
            if f(s) is None:
                # Si aucun chemin augmentant n'est trouvé, on a le flot maximum
                break
            self.R += 1  # On a trouvé un nouveau chemin augmentant

        return self.R

    def max_flow_add(self, s, t, u, v):
        """
        Ajoute une arête bidirectionnelle (u,v) et recalcule le flot maximum.

        Args:
        - s: sommet source du flot
        - t: sommet puits du flot
        - u: extrémité 1 de l'arête
        - v: extrémité 2 de l'arête

        Returns:
        - Nouveau flot maximal après l'ajout.
        """
        self.E[u].add(v)
        self.E[v].add(u)
        self.EE[u].add(v)
        self.EE[v].add(u)
        return self.max_flow(s, t)

    def del_path_st(self, u, v, s, t):
        """
        Supprime toutes les augmentations de flot passant par le chemin (u, ..., v) dans le graphe.
        Met à jour la valeur actuelle du flot maximal.

        Args:
        - u: point de départ du chemin à supprimer
        - v: point d'arrivée
        - s: source du flot
        - t: puits du flot
        """
        e = self.E
        vv = [None] * self.N

        def f(c):
            vv[c] = 1
            if c == v:
                return 1
            for i in e[c]:
                if vv[i] is None and f(i):
                    # Parcours du chemin, supprime le lien
                    if c in e[i]:
                        e[c].remove(i)
                    else:
                        e[i].add(c)
                    return 1
            return

        if f(u):
            return

        # Si aucun chemin direct trouvé, on essaie de supprimer via la source et le puits
        uu = self.del_path_s(u, s)
        tt = self.del_path_s(t, v)
        self.R -= 1  # On réduit le flot maximal car on retire forcément un chemin augmentant

    def del_path_s(self, u, s):
        """
        Chercher et supprimer un chemin allant de u à la source s dans le graphe résiduel.

        Args:
        - u: nœud de départ
        - s: source à atteindre

        Returns:
        - True si un chemin supprimé, None sinon
        """
        e = self.E
        ee = self.EE
        v = [None] * self.N

        def f(c):
            if v[c]:
                return
            v[c] = 1
            if c == s:
                return 1
            for i in e[c]:
                if c in e[i]:
                    continue
                if f(i):
                    e[i].add(c)
                    return 1
            return

        return f(u)

    def max_flow_del(self, s, t, u, v):
        """
        Supprime une arête entre u et v ainsi que tous les effets de son passage sur d'éventuels chemins de flot augmentant.
        Recalcule le flot maximal.

        Args:
        - s: source du flot
        - t: puits du flot
        - u: extrémité 1 de l'arête à supprimer
        - v: extrémité 2 de l'arête à supprimer

        Returns:
        - Nouveau flot maximal après suppression de l'arête.
        """
        e = self.E
        ee = self.EE
        ee[u].remove(v)
        ee[v].remove(u)
        if v in e[u] and u in e[v]:
            # Arête présente dans les deux sens, on retire les deux
            e[u].remove(v)
            e[v].remove(u)
        elif v in e[u]:
            # Arête présente uniquement dans un sens, on retire et on ajuste les chemins du flot
            e[u].remove(v)
            self.del_path_st(v, u, s, t)
        else:
            # Arête présente dans l'autre sens, on retire et ajuste
            e[v].remove(u)
            self.del_path_st(u, v, s, t)
        return self.max_flow(s, t)

def main():
    """
    Point d’entrée du programme principal.
    Gère les entrées/sorties et exécute les requêtes de modification de flot sur un graphe dynamique.

    Returns:
    - Une chaîne contenant le résultat de chaque requête (une valeur par ligne).
    """
    rr = []

    def f(n, e, q):
        """
        Traite un lot de requêtes sur un graphe donné de n sommets et e arêtes.

        Args:
        - n: nombre de sommets
        - e: nombre d'arêtes initiales
        - q: nombre de requêtes à traiter

        Returns:
        - Liste des résultats (valeurs du flot maximal après chaque modification).
        """
        # Lecture des arêtes initiales du graphe
        ft = [LI() for _ in range(e)]
        # Lecture des requêtes sous la forme (type, a, b)
        mab = [LI() for _ in range(q)]
        # Création du graphe initial : dictionnaire d'ensembles
        edges = collections.defaultdict(set)
        for fi, ti in ft:
            edges[fi].add(ti)
            edges[ti].add(fi)
        # Instantiate l'objet Flow pour gérer les opérations sur le graphe dynamique
        fl = Flow(edges, n + 1)
        r = []
        for m, a, b in mab:
            # m == 1 : ajout d'arête ; m == 2 : suppression d'arête
            if m == 1:
                r.append(fl.max_flow_add(1, n, a, b))
            else:
                r.append(fl.max_flow_del(1, n, a, b))
        return r

    while True:
        # Lecture du triplet principal : nombre de sommets, arêtes, requêtes
        n, m, l = LI()
        if n == 0:
            break
        rr.extend(f(n, m, l))
        break  # Le code original ne traite qu'un cas, donc sortie immédiate après le premier

    return '\n'.join(map(str, rr))

print(main())