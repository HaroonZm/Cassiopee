import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10**7)

# Fonction pour calculer la distance euclidienne entre deux points
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Fonction pour déterminer l'orientation de l'ordre des points (p, q, r)
# Renvoie:
# 0 si p, q, r sont colinéaires,
# positive si orientation dans le sens horaire,
# negative si orientation dans le sens antihoraire
def orientation(p, q, r):
    return (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])

# Fonction qui vérifie si deux segments (p1,p2) et (p3,p4) s'intersectent
# retourne le point d'intersection si ils s'intersectent, sinon None
def segment_intersection(p1, p2, p3, p4):
    # On calcule l'orientation des quadruples
    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    # Cas général d'intersection
    if o1*o2 < 0 and o3*o4 < 0:
        # Calcul du point d'intersection des droites
        # Représentation paramétrique des droites
        # p1 + t*(p2-p1) intersecte p3 + u*(p4-p3)
        A1 = p2[1] - p1[1]
        B1 = p1[0] - p2[0]
        C1 = A1*p1[0] + B1*p1[1]

        A2 = p4[1] - p3[1]
        B2 = p3[0] - p4[0]
        C2 = A2*p3[0] + B2*p3[1]

        det = A1*B2 - A2*B1
        if abs(det) < 1e-14:
            # Parallèles (pas de cas possible ici avec test orientation)
            return None
        x = (B2*C1 - B1*C2)/det
        y = (A1*C2 - A2*C1)/det
        return (x, y)
    # Cas colinéaires et chevauchements
    # Vérifions si les points d'extrémité d'un segment sont sur l'autre si orientations sont nulles
    def on_segment(p, q, r):
        # q est dans le rectangle formé par p, r
        return min(p[0], r[0]) - 1e-14 <= q[0] <= max(p[0], r[0]) + 1e-14 and min(p[1], r[1]) - 1e-14 <= q[1] <= max(p[1], r[1]) + 1e-14

    if abs(o1) < 1e-14 and on_segment(p1, p3, p2):
        return p3
    if abs(o2) < 1e-14 and on_segment(p1, p4, p2):
        return p4
    if abs(o3) < 1e-14 and on_segment(p3, p1, p4):
        return p1
    if abs(o4) < 1e-14 and on_segment(p3, p2, p4):
        return p2

    return None

# Fonction pour découper un segment en plusieurs sous-segments à partir des points donnés sur ce segment
# points_on_segment doit contenir les 2 extrémités du segment et tous les points (dont intersection et valves) dessus
# Tous les points doivent être exactement sur ce segment
def split_segment(points):
    # Tri des points selon la distance par rapport au premier point du segment
    base = points[0]
    points.sort(key=lambda p: dist(base, p))
    return points

# Cette classe recense les points uniques du graphe et donne leur index
class PointIndexer:
    def __init__(self):
        self.idx_map = dict()
        self.points = []

    # Ajoute un point s'il n'existe pas encore et retourne son index
    def add_point(self, p):
        key = (round(p[0],8), round(p[1],8)) # arrondi pour éviter problèmes numériques
        if key not in self.idx_map:
            self.idx_map[key] = len(self.points)
            self.points.append(p)
        return self.idx_map[key]

    # Récupère les coordonnées d'un point à partir de son index
    def get_point(self, i):
        return self.points[i]

# Lecture des données
input_iter = iter(sys.stdin.read().strip().split())
N = int(next(input_iter))
M = int(next(input_iter))
segments = []
for _ in range(N):
    xs = int(next(input_iter))
    ys = int(next(input_iter))
    xd = int(next(input_iter))
    yd = int(next(input_iter))
    segments.append(((xs, ys), (xd, yd)))

valves = []
for _ in range(M):
    xv = int(next(input_iter))
    yv = int(next(input_iter))
    valves.append((xv, yv))

xb = int(next(input_iter))
yb = int(next(input_iter))
source = (xb, yb)

xc = int(next(input_iter))
yc = int(next(input_iter))
repair = (xc, yc)

# Étape 1 : Trouver les points d'intersection entre chaque paire de segments
# On récupère aussi toutes les valves, la source et le repair point comme points d’intérêt.
point_indexer = PointIndexer()

# Pour chaque segment, on stocke les points dessus qui serviront à découper le segment
segment_points = [[] for _ in range(N)]

# On commence en ajoutant les extrémités des segments pour découpage
for i, (p1, p2) in enumerate(segments):
    segment_points[i].append(p1)
    segment_points[i].append(p2)

# On calcule les intersections entre segments (i < j) pour éviter double calcul
for i in range(N):
    p1, p2 = segments[i]
    for j in range(i+1, N):
        p3, p4 = segments[j]
        ip = segment_intersection(p1, p2, p3, p4)
        if ip is not None:
            # On ajoute le point d'intersection sur les deux segments
            # Important : vérifier que c'est sur les deux segments physiquement
            # Le test intersection a déjà pris en compte ça
            segment_points[i].append(ip)
            segment_points[j].append(ip)

# Ajout des valves, source et repair point dans les bons segments
# On cherche sur quel segment chacun de ces points se trouve pour l'ajouter à segment_points
def point_on_segment(p, seg):
    # Regarde si p est sur le segment seg (avec marge d'erreur)
    p1, p2 = seg
    # Colinéarité
    o = orientation(p1, p2, p)
    if abs(o) > 1e-10:
        return False
    # Vérifie si p est dans enveloppe rectangulaire de seg
    if min(p1[0], p2[0]) - 1e-10 <= p[0] <= max(p1[0], p2[0]) + 1e-10 and min(p1[1], p2[1]) - 1e-10 <= p[1] <= max(p1[1], p2[1]) + 1e-10:
        return True
    return False

to_add_points = valves + [source, repair]

for p in to_add_points:
    found = False
    for i in range(N):
        if point_on_segment(p, segments[i]):
            segment_points[i].append(p)
            found = True
            break
    if not found:
        # Enoncé garantit que tous les points sont sur un segment
        # Mais on ajoute cette sécurité
        print(-1)
        sys.exit()

# Étape 2 : découpage des segments en arcs élémentaires
# Pour chaque segment, on trie les points sur ce segment et forme les sous-arcs entre points consécutifs
# On ajoute tous les points découpés dans point_indexer, et construit des arêtes (edges)
edges = defaultdict(list)  # graph: from -> list of (to, poids)
valve_set = set((round(p[0],8),round(p[1],8)) for p in valves)

# Pour retrouver si un point est une valve, source ou réparation rapidement
source_key = (round(source[0],8), round(source[1],8))
repair_key = (round(repair[0],8), round(repair[1],8))

for i in range(N):
    pts = segment_points[i]
    # On doit enlever doublons et trier par distance sur le segment
    # Le segment a deux extrémités
    p1, p2 = segments[i]
    unique_pts = []
    seen_keys = set()
    for p in pts:
        key = (round(p[0],8), round(p[1],8))
        if key not in seen_keys:
            seen_keys.add(key)
            unique_pts.append(p)
    # Tri
    base = p1
    unique_pts.sort(key=lambda p: dist(base, p))
    # On crée les arcs entre chaque paire consécutive de points
    for k in range(len(unique_pts)-1):
        a = unique_pts[k]
        b = unique_pts[k+1]
        ia = point_indexer.add_point(a)
        ib = point_indexer.add_point(b)
        length = dist(a, b)
        # On construit graph non orienté (canaux d'eau dans les deux sens)
        # On ajoute l'info pour gérer les valves
        edges[ia].append((ib, length))
        edges[ib].append((ia, length))

# Étape 3 : Construire un graphe orienté permettant de modéliser la coupure d'eau
# Hypothèse : Eau part du source, et on souhaite couper l'alimentation du repair
# Pour cela il faut fermer quelques valves (points valves)
# On veut min sum longueur edges "bloqués" pour séparer source et repair

# Pour modéliser la coupure par valves sur les arcs, on va diviser chaque noeud en deux noeuds (in/out)
# et mettre une capacité infinie sur arcs entre out->in des différents nodes, sauf valves où la capacité sera 0 ou énorme suivant l'idée du problème.

# En fait les valves sont des points où on peut "fermer" pour couper le flux.
# Mais on peut fermer QUE aux valves, pas ailleurs.
# Donc on modélise:
# - Chaque noeud devient deux noeuds (in, out)
# - Arc interne (in->out) a une capacité infinie si ce n'est pas un valve, et coût infini (très grand) sinon.
# - Dans notre cas, on fait un réseau de flots, et on veut min cut
# En réalité, d’après l’énoncé, on peut fermer des valves, donc seul endroit où on coupe le flux est sur les valves.
# Donc l’arête in->out a un coût égal à 0 (pas fermée) ou infini (fermée), on veut minimiser longueur des tuyaux fermés, 
# mais on ne peut que fermer ces valves, donc on considère valves comme arcs qui peuvent être coupés.
# Or on ne peut pas fermer arbitrairement longue portion du tuyau, mais que sur valves.
# Donc on va considérer que chaque valve fait "cut" en un seul point.
# Les "longueurs" des coupures sont la somme des segments "coupés".
# Mais ici en réalité, couper un valve empêche l'eau de passer par ce point.
# Donc en modélisant en graphe:
# - On crée un graphe avec arcs associés à leurs longueurs.
# - On cherche un cut minimal pour séparer la source et la réparation.
# - Mais les coupures ne peuvent être que sur des valves, donc on va transformer chaque valve en un noeud dont on coupe le passage.

# On doit séparer source et repair en coupant un ensemble de valves.
# On veut la longueur minimale totale des tuyaux qui seront coupés = la somme des longueurs des segments qui seront sectionnés.

# Une bonne approche est de transformer le graphe en graphe "noeud coupable" où l’on peut couper les valves,
# en modélisant chaque point valve comme un noeud qui a un coût pour être coupé égale à 0 (car couper valve = coupure efficace),
# et les autres noeuds ont coût coupe infini (ne peuvent pas être fermés).

# Les arêtes entre noeuds ont capacité infinie (ou très élevée). On recherche min-cut en coupant les valve nodes internes?

# Mais d’après la problématique : On minimise la longueur des tuyaux stoppés, donc coupe minimale de tuyaux passant par valves.
# Donc on doit modéliser le réseau où couper l’eau correspond à couper des arcs contenant valves.

# On peut modéliser les valves par des arcs avec poids=0 (pas de "coût" à les couper), mais le vrai "coût" est la longueur des segments (arcs) qui sont coupés donc longueur réelle des arcs coupés.

# Problème plus clair : 
# "En coupant (fermants) certains valves, on stoppe le flux d'eau qui arrive au point de réparation"
# Il faut couper le minimum de longueur de tuyaux (la somme des arcs coupés), sur la condition qu’on ne peut fermer que aux valves.

# D'où conception suivante:
# - Le graphe est composé de noeuds et arcs, arcs avec poids = longueur.
# - On veut couper des arcs subsections du réseau, mais coupure ne peut être immédiate qu'en valve.
# - Il faut donc modéliser les valves comme noeuds coupables, donc en découplant chaque valve en deux sommets (in/out)
# - Et mettre la capacité (coût) de le traverser égale à la longueur des tuyaux attachés (ou égal à 0 ?)
# La difficulté est qu'un valve est un point sur un segment. Couper là arrête l'écoulement sur les segments contigus.

# Proposition de modélisation:
# On découpe les segments en arcs sans valve (atomiques), entre points.
# Chaque valve est un point, existant sur les arcs.

# On modélise le problème précisément par des arcs entre points, avec longueur.

# On veut fermer certains valves pour tout couper entre source et réparation.

# Donc on peut représenter la fermeture d'une valve comme couper tous les arcs adjacents passant par ce point.

# On modélise :

# - On crée pour chaque point deux noeuds (in, out)
# - Entre in et out on met une capacité infinie sauf pour valve points, où la capacité sera la somme des longueurs des arcs incidentes sur ce valve, car couper ce valve revient à couper ces arcs.
# Mais si valve est sur une branche courte, couper valve = couper peu de tuyaux.
# En fait on cherche à minimiser la somme des longueurs des segments coupés.

# Vis-à-vis de la modélisation classique:

# On peut modéliser chaque segment élémentaire comme une arête, avec poids = sa longueur.

# Pour couper l'alimentation, au niveau des valves, on ferme cette valve => couper une arête entrant/sortant du point valve (in/out).

# Donc on construit un graphe orienté où :

# - Chaque point est découpé en noeud_in, noeud_out
# - Capacité d'arête interne in->out = capacité infinite si point non valve, sinon = infini aussi (car on coupe valve comme suppression arêtes adjacentes)
# - Aux valves on assigne capacité égale à somme des arcs adjacents (longueur des segments passant par valve)

# - Pour toutes les arêtes entre différents points, on crée deux arêtes (out->in) des points reliés avec capacité infinite (car on ne peut pas couper sur ces arcs)

# Le min-cut dans ce graphe sépare source et réparation sans couper les arcs hors valves.

# Il nous faut un algorithme de min-cut maximum flow.

# Implémentation d'Edmond-Karp ou Dinic

INF = 1e15

class Edge:
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity

class MaxFlow:
    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(n)]

    def add(self, fr, to, capacity):
        forward = Edge(to, len(self.graph[to]), capacity)
        backward = Edge(fr, len(self.graph[fr]), 0)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs_level(self, s, t, level):
        queue = deque()
        level[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.capacity > 1e-14 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level[t] >= 0

    def dfs_flow(self, v, t, upTo, level, iter_):
        if v == t:
            return upTo
        while iter_[v] < len(self.graph[v]):
            e = self.graph[v][iter_[v]]
            if e.capacity > 1e-14 and level[v] < level[e.to]:
                d = self.dfs_flow(e.to, t, min(upTo, e.capacity), level, iter_)
                if d > 1e-14:
                    e.capacity -= d
                    self.graph[e.to][e.rev].capacity += d
                    return d
            iter_[v] += 1
        return 0.0

    def max_flow(self, s, t):
        flow = 0
        level = [-1]*self.size
        while self.bfs_level(s, t, level):
            iter_ = [0]*self.size
            f = self.dfs_flow(s, t, INF, level, iter_)
            while f > 1e-14:
                flow += f
                f = self.dfs_flow(s, t, INF, level, iter_)
            level = [-1]*self.size
        return flow

# Construction du graphe coupable valve

# Index des noeuds dans graphe