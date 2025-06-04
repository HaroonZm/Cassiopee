import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Lecture des données
W, H, N = map(int, input().split())
lamp_positions = [tuple(map(int, input().split())) for _ in range(N)]

# Les coordonnées sont 1-based dans l'énoncé.
# On traitera les coordonnées en 1-based aussi.

# Fonction pour calculer la distance de Manhattan entre deux points
def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Objectif:
# On veut assigner à chaque lampadaire un rayon r_i (coût),
# tel que le chemin de (1,1) à (W,H) soit dans les cases éclairées
# par au moins un lampadaire (distance manhattan <= r_i)
# et minimiser sum(r_i)

# Observations importantes:
# - Chaque lampe éclaire initialement sa position (r_i = 0)
# - Coût doit être un int positif (>0) si on cherche à étendre la lumière,
#   mais r_i=0 est autorisé (pas d'extension)
# - Le chemin doit être conforme aux cases éclairées (au moins 1 lampe couvre cette case)

# Approche possible:
# On doit trouver des r_i pour que le chemin existe,
# minimisant sum r_i.

# Problème complexe. On peut inverser la problématique:
# Pour une valeur fixée R (somme des r_i),
# peut-on choisir r_i (avec sum r_i <= R) tel qu'on puisse aller de (1,1) à (W,H)
# dans la zone éclairée ?

# Puis faire une recherche du minimum R possible (binaire sur R).

# Implémentation:

# Pour un ensemble de r_i fixés, une case est éclairée si
# elle est à distance manhattan <= r_i d'au moins une lampe.

# Comme le coût est la somme des r_i, et que chaque r_i >= distance entre lampe et cases parcourues,
# et on veut un chemin éclairé, on peut chercher pour un cout total donné,
# si on peut répartir ce cout entre lampes pour couvrir un chemin.

# Modélisation alternative:

# On peut définir un graphe sur les lampes + points start/end:
# On cherche un chemin de (1,1) à (W,H)
# Chaque case sur le chemin est éclairée par au moins une lampe.
# extension du rayon = distance maximum entre lampe et cases éclairées.

# On remarque que la distance minimale du point (1,1) au lampadaire i est fixée.
# De même pour (W,H) au lampadaire j.

# En fait, une idée est d'approximer la solution par un graphe dont les noeuds sont les lampadaires + les points de départ et d'arrivée,
# où le poids d'une arête (i,j) est la distance manhattan entre lampadaires i et j divisé par 2 (car deux rayons peuvent se recouvrir) ou maximum.

# Mais il faut aussi tenir compte de la condition que chaque case sur le chemin est éclairée.

# Alternative simplifiée (car contraintes modestes):

# On peut construire un graphe entre lampadaires + début + fin:
# - Le début (1,1) et la fin (W,H) sont des sommets aussi
# - On connecte deux sommets (lampadaires ou départ/fin) s'ils peuvent s'éclairer mutuellement avec un certain coût

# Puis on fait un Dijkstra sur ce graphe pour trouver la somme minimale des r_i nécessaires.

# Détails:

# Les sommets sont les lampadaires plus deux sommets fictifs:
# - start: (1,1)
# - goal: (W,H)

# Pour chaque arc (u,v), le coût associé est la moitié (arrondi vers le haut) de la distance entre u et v,
# car si l'on mets r_u et r_v >= distance(u,v)/2, alors leurs zones d'éclairage se recouvrent,
# et un chemin passant entre eux est possible.

# Puis on cherche le chemin start->goal minimisant la somme des coûts r_i (radii)

# Cela correspond à chercher un ensemble de lampadaires plus start/goal reliés entre eux
# Minimisant la somme des r_i nécessaires pour couvrir un chemin.

# On effectue Dijkstra sur ce graphe pour trouver le coût minimal.

# Enfin on renvoie le total.

# IMPLEMENTATION DÉTAILLÉE:

# - On définit les sommets: 0=start, 1..N lampadaires, N+1=goal
# - Pour start et goal on calculera le coût r:
#   - r_start = distance minimal au plus proche lampadaire (pour que start soit éclairé)
#   - idem pour goal
#   mais dans notre modèle, start et goal sont traités aussi comme nodes, on connecte on edges computed as above.
# - On construit toutes les arêtes avec le poids = ceil( distance(u,v) / 2 )

# On fait Dijkstra de start vers goal pour trouver le chemin avec somme minimal des r.

# Comme le rayon r_i doit être un entier positif si étendu, mais 0 est possible,
# les poids d'arêtes correspondent au maximum des r_i nécessaires pour couvrir la distance entre lampes.

# Cependant la solution d'origine de l'énoncé a un exemple avec 0 pour le cas d'une lampe unique sur (1,1).
# Donc on doit gérer efficacement les radii nuls.

# Pour la distance entre start et une lampe:
# - Si distance=0 (start sur lampe), coût 0 possible.
# - Sinon, on doit r_i >= distance pour couvrir start.

# Donc on ajoute les arcs de start => lampes avec poids distance(start, lampe)
# même chose lampes => goal.

# Pour les arcs entre lampes, le coût (r_i or r_j) doit couvrir moitié distance entre lampes.

# Pour plus de clarté, on fait un graphe complet avec:
# - sommet 0: start (1,1)
# - sommets 1..N: lampadaires
# - sommet N+1: goal (W,H)

# Arêtes:
# - start->lampadaire i: coût = distance(start, lampadaire_i)
# - lampadaire i -> lampadaire j: coût = (distance(i,j)+1)//2
# - lampadaire i -> goal: coût = distance(lampadaire_i, goal)

# Dans Dijkstra, le cout cumulatif est la somme des r_i 
# On cherchera la somme minimale pour atteindre goal.

# Remarque: Le chemin sur les lampadaires correspond à la distribution des r_i.

# Puisque nous n'avons pas de "chemin" réel qui passe par des cases non lampadaires,
# nous devons modéliser correctement.

# Mais l'énoncé demande la somme totale des r_i minimisée,
# on peut formuler cette solution comme un plus court chemin sur ce graphe.

# IMPLEMENTATION:

# Construire graphe avec N+2 nœuds et arêtes comme décrit.
# Faire Dijkstra du noeud "start" (0) au noeud "goal" (N+1)
# Le poids du chemin trouvé est la réponse.

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

nodes = [(1,1)] + lamp_positions + [(W,H)]  # 0=start, 1..N lmp, N+1=goal

N_nodes = N + 2
graph = [[] for _ in range(N_nodes)]

# Ajouter arêtes start->lampadaire i avec coût = distance(start, lampadaire i)
for i in range(1, N+1):
    d = dist(nodes[0], nodes[i])
    graph[0].append((i, d))
    graph[i].append((0, d))  # symétrique

# Arêtes entre lampadaires
for i in range(1, N+1):
    for j in range(i+1, N+1):
        d = dist(nodes[i], nodes[j])
        cost = (d + 1)//2  # coût minimal pour éclairage recouvrant entre deux lampadaires
        graph[i].append((j, cost))
        graph[j].append((i, cost))

# Arêtes lampadaire->goal
for i in range(1, N+1):
    d = dist(nodes[i], nodes[N+1])
    graph[i].append((N+1, d))
    graph[N+1].append((i, d))

# Arête start -> goal directe:
d = dist(nodes[0], nodes[N+1])
graph[0].append((N+1, d))
graph[N+1].append((0, d))

# Dijkstra
INF = 10**15
distances = [INF]*N_nodes
distances[0] = 0
hq = [(0,0)]  # (cost, node)

while hq:
    cost, u = heappop(hq)
    if distances[u] < cost:
        continue
    if u == N+1:
        # Atteint goal
        break
    for v, w in graph[u]:
        ncost = cost + w
        if ncost < distances[v]:
            distances[v] = ncost
            heappush(hq, (ncost, v))

print(distances[N+1])