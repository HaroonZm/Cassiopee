# Importation de nombreux modules standards de Python pour diverses tâches, avec les alias classiques
import math                 # Module pour fonctions mathématiques basiques et avancées, ex: sqrt, sin, etc.
import string               # Fournit des constantes liées aux chaînes de caractères et des outils de manipulation
import itertools            # Outils pour combiner, permuter et générer des itérateurs complexes
import fractions            # Gestion des fractions rationnelles exactes
import heapq                # Fournit une implémentation efficace de file de priorité (tas binaire)
import collections          # Structures de données avancées (deque, defaultdict, Counter, etc.)
import re                   # Expressions régulières pour analyse de texte
import array                # Tableaux de type C pour stockage efficace de données numériques
import bisect               # Recherche et insertion dans des listes triées, très efficace
import sys                  # Permet l'accès à des fonctions système, comme stdin et setrecursionlimit
import random               # Fonctions pour générer de l'aléatoire et mélanger des listes
import time                 # Outils de gestion du temps et des délais
import copy                 # Fournit des fonctions de copie superficielle et profonde d'objets
import functools            # Fonctions utilitaires pour la programmation fonctionnelle, cache, etc.

# Modifie la limite par défaut de la profondeur de récursion possible dans le programme Python (par défaut, assez faible)
sys.setrecursionlimit(10**7)  # Permet de faire des appels récursifs profonds sans atteindre facilement la limite

# Déclare quelques constantes numériques utilisées plus loin dans le code
inf = 10**20           # Valeur numérique très grande pour simuler l'infini dans certains algos (plus grande que tout coût raisonnable)
eps = 1.0 / 10**13     # Petite valeur epsilon pour comparer les flottants ou gérer des seuils de précision
mod = 10**9+7          # Nombre premier usuel pour modulo dans de nombreux algorithmes, évite des débordements (souvent pour les concours)

# Listes de couples représentant des directions -- utiles pour parcourir des grilles
dd = [(-1,0),(0,1),(1,0),(0,-1)]   # Directions cardinales : haut, droite, bas, gauche (mouvements orthogonaux)
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]  # Directions cardinales & diagonales, donc 8 voisins possibles

# Définition de fonctions utilitaires pour lire et convertir des entrées de manière concise

def LI():
    """
    Lit une ligne de l'entrée standard, la découpe selon les espaces,
    puis convertit chaque élément en un entier et retourne la liste d'entiers.
    Ex : input = '1 2 3' -> [1,2,3]
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Similaire à LI, mais décrémente chaque valeur lue de 1.
    Pratique pour transformer des indices 1-based en indices 0-based.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard, la découpe selon les espaces, convertit chaque élément en float, et retourne la liste de floats.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard, la découpe selon les espaces, retourne une liste de chaînes (mots).
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard, et convertit en entier.
    Pratique pour les inputs d'un seul entier.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard et convertit en float.
    """
    return float(sys.stdin.readline())

def S():
    """
    Utilise la fonction input() de base pour lire une ligne (inclut le retour chariot à la fin de la saisie utilisateur/invite).
    """
    return input()

def pf(s):
    """
    Fonction raccourcie pour afficher une chaîne à l'écran et forcer le flush (important pour certains systèmes online).
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale du script, gère la logique centrale du traitement du problème.
    """
    rr = []  # Liste qui va stocker les résultats d'éventuels multiples cas de test

    def f():
        """
        Fonction interne, gérant le traitement d'un cas de test.
        Contient toute la logique pour le problème à résoudre.
        """
        # Lecture des dimensions de la grille et du nombre de positions importantes (m)
        r, c, m = LI()  # r : nombre de lignes, c : colonnes, m : nombre de positions spéciales à traiter

        # Lecture de la grille 'a', chaque cellule encodée :
        # - Les bords sont remplis avec '1' (pour éviter les débordements lors des parcours),
        # - Les cellules '.' (points) sont None, les autres chars sont remplacés par '1'
        a = (
            [[1] * (c+2)] +
            [
                [1] + [None if cell == '.' else 1 for cell in S()] + [1]
                for _ in range(r)
            ] +
            [[1] * (c+2)]
        )

        # Construction de plusieurs matrices dont :
        # cost = coût de traversée d'une case,
        # on = coût (ou état) pour un type "on",
        # off = coût/état pour "off"
        # Ces matrices ont taille (r+2) x (c+2) avec des bords à 1
        cost = (
            [[1] * (c+2)] +
            [[1] + LI() + [1] for _ in range(r)] +
            [[1] * (c+2)]
        )
        on = (
            [[1] * (c+2)] +
            [[1] + LI() + [1] for _ in range(r)] +
            [[1] * (c+2)]
        )
        off = (
            [[1] * (c+2)] +
            [[1] + LI() + [1] for _ in range(r)] +
            [[1] * (c+2)]
        )

        # Lecture des m positions clés à considérer ("ms"), les indices sont incrémentés de 1 pour correspondre à la grille avec bordure
        ms = [tuple(map(lambda x: x+1, LI())) for _ in range(m)]

        # Construction d'un graphe (e) via une table de hachage (dictionnaire) des voisins accessibles pour chaque cellule libre (a[i][j] == None)
        e = collections.defaultdict(list)
        for i in range(1, r+1):  # On parcourt la zone utile de la grille (hors bords)
            for j in range(1, c+1):
                if a[i][j]:  # Si la cellule n'est pas un espace libre (donc mur ou bordure), on saute
                    continue
                for di, dj in dd:  # Pour chaque direction orthogonale
                    if a[i+di][j+dj]:  # Si la cellule voisine n'est pas libre, on saute
                        continue
                    e[(i, j)].append(((i+di, j+dj), 1))  # Sinon, on ajoute le voisin accessible avec un coût de 1

        def search(s):
            """
            Recherche du plus court chemin depuis s dans le graphe e.
            Utilise Dijkstra vu que tous les coûts sont 1 ici (BFS suffirait), mais Dijkstra est plus générique.
            Renvoie un dictionnaire d : pour chaque coordonnée, la distance minimale depuis la source s.
            """
            d = collections.defaultdict(lambda: inf)  # Toutes les distances initialisées à +infini
            d[s] = 0  # Distance à soi-même = 0
            q = []  # File de priorité (tas), chaque élément : (coût, position)
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)  # Mémorise les positions déjà traitées dans l'algo

            while len(q):  # Tant qu'il reste des positions à traiter
                k, u = heapq.heappop(q)
                if v[u]:  # Si déjà visité, on ignore
                    continue
                v[u] = True  # Marque comme visité

                for uv, ud in e[u]:  # Pour chaque voisin de u
                    if v[uv]:  # Si voisin déjà vu, on saute
                        continue
                    vd = k + ud  # Nouveau coût potentiel pour atteindre uv
                    if d[uv] > vd:  # Si ce nouveau chemin est meilleur
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))  # On alimente le tas/priorité

            return d  # Renvoie le dico distances

        # Pour chaque position à atteindre ("ms"), on pré-calcule la table de distances/minimum distances depuis elle
        ad = {}
        for k in ms:
            if k in ad:  # Si la position déjà traitée, on saute
                continue
            ad[k] = search(k)

        ti = 0  # Compteur pour le temps/ordre de traversée
        td = collections.defaultdict(list)  # Pour chaque position traversée, mémorise les moments où elle est visitée
        c = ms[0]  # On commence par la première position à atteindre
        td[c].append(0)  # On note qu'on la visite au temps 0

        for t in ms[1:]:  # Pour chaque prochaine position à atteindre
            while c != t:  # Tant qu'on n'est pas arrivé à la position voulue
                cc = ad[t][c]  # Distance minimale de t à la position courante c
                # On cherche à reculer d'un cran vers t, en utilisant toujours des plus courts chemins
                for di, dj in dd:  # Pour chaque direction orthogonale
                    ni = c[0] + di
                    nj = c[1] + dj
                    n = (ni, nj)  # Nouvel emplacement après le déplacement
                    if ad[t][n] == cc - 1:  # Si voisin plus proche de t qu'actuellement
                        ti += 1  # Incrémente temps/mouvement
                        td[n].append(ti)  # Note que cette position est atteinte à ce temps
                        c = n  # Avance vers la cible
                        break  # Sort du for : un seul mouvement à chaque étape

        r = 0  # Somme finale du coût total
        # On traite chaque position traversée par ordre (tri sur positions)
        for k, v in sorted(td.items()):
            i = k[0]
            j = k[1]
            cs = cost[i][j]          # Coût de base de la case
            onf = on[i][j] + off[i][j]  # Somme de paramètres "on" et "off" pour la case
            tr = onf                    # Coût total temporaire démarré à onf
            for vi in range(len(v)-1):  # Pour chaque passage successif sur la case
                sa = v[vi+1] - v[vi]  # Ecart de temps entre deux visites
                tr += min(cs * sa, onf)  # Coût du passage : soit coût cumulé, soit onf si c'est plus optimal
            r += tr  # Ajoute le coût total pour cette position au coût global

        return r  # Renvoie le coût total pour ce cas de test

    while True:  # Boucle potentiellement prévue pour supporter plusieurs cas de test (ici break après un cas seulement)
        rr.append(f())  # Appelle la fonction f, et ajoute le résultat à la liste rr
        break  # Sort de la boucle (donc en l'état, ne supporte en fait qu'un seul cas)

    # Formate et retourne les résultats, chaque résultat en ligne séparée (prêt à être affiché)
    return '\n'.join(map(str, rr))

# Point d'entrée standard en Python, lance la fonction main et affiche le résultat retourné
print(main())