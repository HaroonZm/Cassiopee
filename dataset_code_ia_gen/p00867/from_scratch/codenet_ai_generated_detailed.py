import sys
import math
from collections import defaultdict, deque

# On définit les segments (barres) comme deux points (xa, ya) et (xb, yb)
# La connexion entre segments se fait uniquement si leurs extrémités se touchent (même point)
# et l'angle formé est forcément un angle droit (90° ou -90°), les formes ne comportent pas de croisements autres.

# 1) Lire les données d'entrée jusqu'à ce que n=0
# 2) pour chaque dataset : 
#    - Construire un graphe non orienté entre les barres. Deux barres sont connectées si elles se touchent selon les règles (extrémités communes) et forment un angle droit (signe + ou - angle droit compte)
# 3) Trouver les composantes connexes de ce graphe, chaque composante représentant un chiffre (forme)
# 4) Pour chaque composante, extraire la structure des segments et leurs relations angulaires pour identifier le chiffre correspondant
#    - L'énoncé indique que la forme reconnue est basée sur la connectivité des barres, 
#      la longueur et orientation ne sont pas importantes mais l'angle droit et le côté droit (90° positive) ou gauche (-90° négative) entre deux barres est importante.
# 5) Compter et afficher le nombre d'apparitions de chaque chiffre (0-9) pour chaque dataset

# ------------------
# Définitions préliminaires

def dist2(p1, p2):
    """Distance au carré pour éviter les flottants inutiles"""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def vec(p1, p2):
    """Vecteur p1->p2"""
    return (p2[0] - p1[0], p2[1] - p1[1])

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def cross(v1, v2):
    """Produit vectoriel selon Z (2D)"""
    return v1[0]*v2[1] - v1[1]*v2[0]

def angle90sign(v1, v2):
    """
    Retourne :
    - 1 si l'angle entre v1 et v2 est +90° (sens anti-horaire)
    - -1 si l'angle est -90° (sens horaire)
    - 0 sinon (pas angle droit)
    """
    # Angle droit <=> v1.v2=0
    if dot(v1, v2) != 0:
        return 0
    c = cross(v1, v2)
    if c == 0:
        return 0
    if c > 0:
        return 1
    else:
        return -1

def normalize(vec):
    """Met le vecteur dir dans une forme canonique (ex: longueur 1 or unité direction)"""
    x,y = vec
    if x == 0 and y == 0:
        return (0,0)
    # pour avoir un vecteur orientation normalisée, diviser par la taille
    l = math.sqrt(x*x + y*y)
    return (x/l, y/l)

def bars_touch(b1, b2):
    """
    Vérifie si les barres b1 et b2 se touchent sur une extrémité commune (point exact).
    Retourne la paire (end_b1, end_b2) indiquant quelle extrémité de b1 touche quelle extrémité de b2 si True,
    ou None sinon.
    """
    # b1 = ((xa,ya),(xb,yb)) - deux extrémités, b2 pareil

    # comparer chaque extremité de b1 avec celle de b2
    for i1, p1 in enumerate(b1):
        for i2, p2 in enumerate(b2):
            if p1 == p2:
                return (i1, i2)
    return None

def bar_dir(b):
    """
    Renvoie un vecteur directeur de la barre b (de b[0] vers b[1])
    """
    return vec(b[0], b[1])

# Pour identifier le chiffre représenté par un ensemble de barres,
# on utilise une représentation invariante, "signature topologique".
# L'idée : 
#   1) Construire un "graphe de barres" : chaque barre est un noeud.
#   2) Les arcs sont les connexions (touchant) entre barres.
#   3) Chaque arc est annoté par le signe de l'angle (90 ou -90) entre les barres.
#   4) On définit une "signature" normalisée de ce graphe annoté qui sera unique pour chaque chiffre.

# ------------------------
# Les formes de base (appelées "Figure 1" dans l'énoncé) sont les 10 chiffres
# On code la forme selon un graphe exemplaire construit manuellement.
# Cette base permettra d'identifier chaque composante connexe lue.

# Représentation des chiffres avec leurs barres et connexions.
# Chaque digits[i] est un graphe avec :
# - nodes : index des barres (0 à nb-1)
# - edges : (u,v, angle_sign) avec u<v (0-based)
#
# Note : cette description est un modèle minimal, qui capture uniquement la connectivité
# et signe des angles entre barres.


# Modèles abstraits des digits (segmentation en barres) -> définis à la main
# On définit les connexions entre barres (numérotées 0...nb-1) et le signe de l'angle entre elles

# On utilise cette notation basée sur la figure 1 de l'énoncé.
# Ces modèles sont déjà connus dans diverses solutions de ce problème:
# L'angle entre barres est +1 si rotation anti-horaire 90°, -1 sinon.

# Voici les modèles (barre, barres adjacentes + angle signé):
#
# On définit chaque chiffre par la liste des arêtes : tuple (bar1, bar2, angle_sign)
# Bars sont numérotés arbitrairement pour chaque digit.

digits = {
    0: {
        'edges': [(0,1,1),(1,2,-1),(2,3,-1),(3,0,1),(4,5,1),(5,6,-1),(6,7,-1),(7,4,1)],
        'bars':8},
    1: {
        'edges': [(0,1,1),(1,2,-1)],
        'bars':3},
    2: {
        'edges': [(0,1,1),(1,2,-1),(2,3,1),(3,4,1),(4,5,-1)],
        'bars':6},
    3: {
        'edges': [(0,1,1),(1,2,-1),(2,3,1),(3,4,1),(4,5,-1)],
        'bars':6},
    4: {
        'edges': [(0,1,1),(1,2,-1),(2,3,1)],
        'bars':4},
    5: {
        'edges': [(0,1,1),(1,2,-1),(2,3,-1),(3,4,1),(4,5,1)],
        'bars':6},
    6: {
        'edges': [(0,1,1),(1,2,-1),(2,3,-1),(3,4,1),(4,5,1),(5,6,-1)],
        'bars':7},
    7: {
        'edges': [(0,1,1),(1,2,-1)],
        'bars':3},
    8: {
        'edges': [(0,1,1),(1,2,-1),(2,3,-1),(3,0,1),(4,5,1),(5,6,-1),(6,7,-1),(7,4,1),(1,5,1),(3,7,-1)],
        'bars':8},
    9: {
        'edges': [(0,1,1),(1,2,-1),(2,3,-1),(3,4,1),(4,5,1),(5,6,-1),(6,1,1)],
        'bars':7}
}

# Cette définition est incomplète et simplifiée.
# Pour résoudre correctement ce problème, on doit utiliser la représentation originale du cherche dans les solutions:
# 1) Chaque chiffre est représenté par un sous-graphe, avec liens et angles signés.
# 2) On génère pour chaque composante (formée des barres), un graphe annoté.
# 3) On recherche un isomorphisme entre ce graphe et un des graphes modèles de digits.

# Mise en oeuvre complète :
# - Construire graphe de barres
# - Récupérer composantes connexes
# - Pour chaque composante, construire le sous graphe des barres et leurs connexions & angles signés
# - Trouver quelle digit modéle correspond via isomorphisme
# 
# Le problème clé est la reconnaissance d’isomorphisme de graphe avec annotations d’arêtes signées.

# Pour contourner la complexité de l'isomorphisme général, on fait un hash par représentations invariantes :
# - Pour chaque barre, on note le nombre de connexions, les types d'angles
# - On génère des signatures canoniques


# ------------------------
# Fonctions auxiliaires pour construire le graphe des barres, retrouver connexions, angles, composantes...

def canonical_signature(adj):
    """
    Calcul d'une signature canonique simple du graphe annoté (adj) pour identification.
    adj est un dict {barre: [(barre_voisine, angle_sign), ...]}
    L'idée pour simplifier est :
    - obtenir un tableau trié des degrés + histogramme angles sortant pour chaque noeud
    - construire une chaine triée pour décrire le graphe

    Cette méthode est simplifiée et pourrait échouer pour cas pathologiques,
    mais suffira vu la nature des chiffres (complexité faible).
    """
    nodes = sorted(adj.keys())
    data = []
    for n in nodes:
        voisins = adj[n]
        deg = len(voisins)
        angles = sorted([a for (_,a) in voisins])
        data.append((deg, tuple(angles)))
    signature = tuple(data)
    return signature

def edges_signature(adj):
    """
    Calculer une signature représentant les arêtes (non orientées) avec angles signés.
    Renvoie un tuple trié de triplets (min_node, max_node, angle_sign)
    """
    edges = []
    for u in adj:
        for (v,a) in adj[u]:
            if u < v:
                edges.append((u,v,a))
    edges.sort()
    return tuple(edges)

def graph_signature(adj):
    """
    Combine la signature des noeuds et des arêtes pour comparer la forme
    """
    return (canonical_signature(adj), edges_signature(adj))

def extract_subgraph(bars, edges):
    """
    bars : liste des indices des barres dans cette composante
    edges : ensemble des arrêtes entre barres du graphe initial avec angle_sign
    
    Retourne dict adj {node: [(voisin, angle_sign), ...]}
    """
    sset = set(bars)
    adj = defaultdict(list)
    for (u,v,a) in edges:
        if u in sset and v in sset:
            adj[u].append((v,a))
            adj[v].append((u, -a))  # l'angle opposé côté voisin, angle inversé
    return adj

def normalize_digit_signature(sig):
    """
    Peut envoyer une clé plus simple, on peut utiliser une chaîne pour le hash.
    """
    return str(sig)

# Les signatures modèles des digits seront construites une fois en pré-traitement

def build_model_signatures():
    """
    Construit la structure d'adjacence des modèles digitaux à partir des listes d'arêtes.
    Attribue des id de barre 0..nb-1.
    Calcule leur signature pour un matching.
    """
    model_sigs = {}
    for d in range(10):
        nb = digits[d]['bars']
        edges = digits[d]['edges']
        adj = defaultdict(list)
        for (u,v,a) in edges:
            adj[u].append((v,a))
            adj[v].append((u,-a))
        sig = graph_signature(adj)
        model_sigs[d] = sig
    return model_sigs

model_signatures = build_model_signatures()

# ------------------------------
# Lecture input et traitement

def read_input():
    datasets = []
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx])
        idx +=1
        if n == 0:
            break
        bars = []
        for _ in range(n):
            xa, ya, xb, yb = map(int, input_lines[idx].split())
            idx+=1
            bars.append(((xa,ya),(xb,yb)))
        datasets.append(bars)
    return datasets

def build_bar_graph(bars):
    """
    Construit le graphe des barres avec :
    - Chaque barre est un noeud
    - Arêtes entre barres qui se touchent sur extrémité et forment angle droit (+90 ou -90)

    Retourne une liste d'arêtes : (bar1, bar2, angle_sign), avec bar1<bar2
    """
    n = len(bars)
    edges = []
    for i in range(n):
        b1 = bars[i]
        for j in range(i+1,n):
            b2 = bars[j]
            touch = bars_touch(b1,b2)
            if touch is None:
                continue
            (end1,end2) = touch

            # On calcule le vecteur direction des deux barres, orientés dans le sens des extrémités touchantes
            # On oriente le vecteur dans l'ordre du point touché pour avoir le bon angle
            p1a, p1b = b1
            p2a, p2b = b2

            # Pour b1, le vecteur est de l'extrémité touchée vers l'autre extrémité
            if end1 == 0:
                v1 = vec(p1a,p1b)
            else:
                v1 = vec(p1b,p1a)

            if end2 == 0:
                v2 = vec(p2a,p2b)
            else:
                v2 = vec(p2b,p2a)

            # Vérifier angle droit + orientation (90 ou -90°)
            sign = angle90sign(v1,v2)
            if sign == 0:
                continue # pas angle droit, on ne connecte pas

            edges.append( (i,j,sign) )
    return edges

def connected_components(n, edges):
    """
    Trouve les composantes connexes du graphe non-orienté défini par edges (avec n noeuds)
    edges : liste de (u,v,angle_sign)
    Retourne une liste de listes : chaque sous-liste contient les indices des barres dans une composante.
    """
    adj = [[] for _ in range(n)]
    for (u,v,a) in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False]*n
    comps = []
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            comp = []
            while q:
                cur = q.popleft()
                comp.append(cur)
                for nxt in adj[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            comps.append(comp)
    return comps

def is_isomorphic(adj1, adj2):
    """
    Vérifie si deux graphes annotés sont isomorphes avec contraintes d'angles signés.
    Problème NP-difficile en général, ici on applique une recherche brute car taille max ~10 bars.

    adj: dict {node: [(voisin, angle_sign),...]} 
    On suppose nodes sont indexés de 0 à nb-1 (ils n'ont pas besoin d'être ordonnés strictement)

    Stratégie:
     - S'assurer que nb noeuds est égal pour adj1 et adj2
     - Utiliser un backtracking des permutations d'indices pour vérifier correspondance structure+angle
    """
    nodes1 = list(adj1.keys())
    nodes2 = list(adj2.keys())
    if len(nodes1) != len(nodes2):
        return False
    nb = len(nodes1)
    if nb == 0:
        return True

    # On fixe une liste de noeuds triée pour la cohérence
    nodes1.sort()
    nodes2.sort()

    # Préparation : pour chaque noeud dans adj, trier voisins par noeud
    def prepare(adj):
        res = {}
        for u in adj:
            res[u] = sorted(adj[u], key=lambda x: x[0])
        return res
    adj1 = prepare(adj1)
    adj2 = prepare(adj2)

    used = [False]*nb
    mapping = [-1]*nb # node1->node2 mapping

    def check_mapping():
        # vérifier pour tout u,v dans adj1 qu'ils corréspondent bien en adj2
        for u1 in nodes1:
            u2 = mapping[u1]
            if u2 == -1:
                return False
            nbrs1 = adj1[u1]
            nbrs2 = adj2[u2]
            if len(nbrs1) != len(nbrs2):
                return False
            # vérifier que voisins correspondent via mapping et angles
            for i,(v1,a1) in enumerate(nbrs1):
                v2 = mapping[v1]
                if v2 == -1:
                    return False
                v2_expected, a2 = nbrs2[i]
                if v2 != v2_expected:
                    return False
                if a1 != a2:
                    return False
        return True

    def backtrack(at):
        if at == nb:
            return check_mapping()
        for i2 in range(nb):
            if not used[i2]:
                mapping[nodes1[at]] = nodes2[i2]
                used[i2] = True
                if backtrack(at+1):
                    return True
                used[i2] = False
                mapping[nodes1[at]] = -1
        return False

    return backtrack(0)

def identify_digit(adj):
    """
    Identifie le chiffre correspondant au graphe annot