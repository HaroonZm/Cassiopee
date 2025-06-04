import math
import sys
from heapq import heappush, heappop

# Fonction pour calculer la distance euclidienne entre deux points
def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Fonction pour trouver les deux points d'intersection entre deux cercles
# Ces points correspondent aux intersections de C_i et C_{i+1}
def circle_intersections(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = dist((x1,y1),(x2,y2))
    # deux cercles s'intersectent en deux points distincts, garanties par l'énoncé
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 - a**2)
    # point P, projection de l'intersection sur la droite entre centres
    x3 = x1 + a*(x2 - x1)/d
    y3 = y1 + a*(y2 - y1)/d
    # les deux points d'intersection
    rx = -(y2 - y1) * (h/d)
    ry = -(x2 - x1) * (h/d)
    p_int1 = (x3 + rx, y3 - ry)
    p_int2 = (x3 - rx, y3 + ry)
    return p_int1, p_int2

# Fonction pour vérifier si un segment (p1,p2) est contenu dans au moins un des cercles de la chaîne
# On vérifie par échantillonnage si les points sont dans au moins un cercle
# Ici, on sample uniformément entre p1 et p2 pour une approximation suffisante
def segment_in_chain(p1, p2, circles):
    samples = 20  # nombre de points à tester sur le segment
    for i in range(samples + 1):
        t = i / samples
        x = p1[0] + t*(p2[0] - p1[0])
        y = p1[1] + t*(p2[1] - p1[1])
        # vérifier si (x,y) est dans au moins un cercle
        if not any(dist((x,y), (cx,cy)) <= r + 1e-10 for (cx,cy,r) in circles):
            return False
    return True

# Fonction principale traitant un dataset (liste de cercles)
def solve(dataset):
    n = len(dataset)
    circles = dataset

    # On va construire un graphe représentatif :
    # chaque cercle a 2 points d'intersection avec le cercle suivant (sauf le dernier)
    # On ajoute aussi les centres des premiers et derniers cercles (points de départ et d'arrivée)
    # Les sommets du graphe: 2*(n-1) points d'intersection + 2 centres
    # On connecte les sommets par arcs si le segment entre eux est contenu dans la chaîne

    # Stockage des points d'intersections entre cercles i et i+1
    inter_points = [circle_intersections(circles[i], circles[i+1]) for i in range(n-1)]

    # On numérote les sommets :
    # vertex 0 : centre du cercle 0 (départ)
    # vertex 1: centre du cercle n-1 (arrivée)
    # vertices 2k, 2k+1 (k=0..n-2): les deux points d'intersection entre cercle k et k+1
    vertices = []
    vertices.append((circles[0][0], circles[0][1]))  # centre premier cercle, id = 0
    vertices.append((circles[-1][0], circles[-1][1]))# centre dernier cercle, id = 1
    for p1,p2 in inter_points:
        vertices.append(p1)
        vertices.append(p2)

    # On construit un graphe sous forme de listes d'adjacence avec poids (distances)
    # Les sommets sont ordonnés: [centre_0, centre_n-1, inter_0_p1, inter_0_p2, inter_1_p1, inter_1_p2,... ]

    E = len(vertices)
    graph = [[] for _ in range(E)]

    # Ajouter arêtes entre centres et points d'intersections de cercle 0
    # Le centre 0 est le vertex 0, les points d'intersection entre C0 et C1 sont vertices 2 et 3
    for v_id in [2,3]:
        if segment_in_chain(vertices[0], vertices[v_id], circles):
            d = dist(vertices[0], vertices[v_id])
            graph[0].append((v_id, d))
            graph[v_id].append((0, d))

    # Ajouter arêtes entre centres et points d'intersections de cercle n-1
    # Le centre n-1 est le vertex 1, les points d'intersection entre C_{n-2} et C_{n-1} sont vertices 2(n-2) et 2(n-2)+1
    last_i1 = 2*(n-2)
    for v_id in [last_i1, last_i1+1]:
        if segment_in_chain(vertices[1], vertices[v_id], circles):
            d = dist(vertices[1], vertices[v_id])
            graph[1].append((v_id, d))
            graph[v_id].append((1, d))

    # Ajouter arêtes entre points d'intersections consécutifs pour chaque i, i+1
    # Pour chaque i de 0 à n-2, on a points 2i, 2i+1
    # points d'un cercle apparaissent par paires; construire les connections possibles :
    # - la paire de points d'un même cercle d'intersections (par exemple, points d'intersection entre i et i+1)
    # - les connexions entre les points d'intersection d'une chaîne voisine (i) et (i+1)

    # Arêtes entre les 2 points d'intersection du même cercle (par exemple 2i et 2i+1)
    # Ils sont accessibles par une arc puisque ils appartiennent au même cercle ci
    for i in range(n-1):
        a = 2*i
        b = 2*i + 1
        # vérifier que segment est dans la chaîne (en pratique, les 2 points sont sur la frontière des 2 cercles adjacents,
        # donc la segment est dans ces cercles et la chaîne)
        if segment_in_chain(vertices[a], vertices[b], circles):
            d = dist(vertices[a], vertices[b])
            graph[a].append((b, d))
            graph[b].append((a, d))

    # Arêtes entre points d'intersection adjacents dans la chaîne, i.e. entre (2i,2i+1) et (2(i+1),2(i+1)+1)
    # Ces points se situent sur les intersections entre cercles i,i+1 et i+1,i+2
    # On tente toute combinaison entre les 2 points du ième couple et les 2 points du (i+1)ème couple
    for i in range(n-2):
        for u in [2*i, 2*i+1]:
            for v in [2*(i+1), 2*(i+1)+1]:
                # Le segment u-v doit être contenu dans la chaîne
                if segment_in_chain(vertices[u], vertices[v], circles):
                    d = dist(vertices[u], vertices[v])
                    graph[u].append((v,d))
                    graph[v].append((u,d))

    # Maintenant, trouver le plus court chemin entre vertex 0 (centre cercle 0) et vertex 1 (centre cercle n-1)
    # Utilisons Dijkstra
    def dijkstra(start, end):
        distances = [math.inf]*E
        distances[start] = 0.0
        heap = [(0.0, start)]
        while heap:
            cur_d, u = heappop(heap)
            if cur_d > distances[u]:
                continue
            if u == end:
                return cur_d
            for v, w in graph[u]:
                nd = cur_d + w
                if nd < distances[v]:
                    distances[v] = nd
                    heappush(heap, (nd,v))
        return distances[end]

    ans = dijkstra(0,1)
    return ans

# Lecture des données en entrée et résolution
def main():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx >= len(input):
            break
        n = int(input[idx])
        idx += 1
        if n == 0:
            break
        dataset = []
        for _ in range(n):
            x = int(input[idx]); y = int(input[idx+1]); r = int(input[idx+2])
            idx += 3
            dataset.append((x,y,r))
        # Résoudre pour ce dataset
        ans = solve(dataset)
        print(f"{ans:.6f}")

if __name__ == "__main__":
    main()