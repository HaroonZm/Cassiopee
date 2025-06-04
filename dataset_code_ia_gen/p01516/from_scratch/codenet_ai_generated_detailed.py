import sys
import math
import heapq

# Constantes
PI = math.pi
EPS = 1e-14

# Fonction pour calculer les 5 points de l'extérieur du pentagramme (les "pointe")
def generate_star_points(xc, yc, angle_deg, r):
    # Chaque pentagramme est un polygone à 5 pointes
    # angle_deg est l'angle entre la verticale (axe y) et la première pointe
    # on génère les 10 points (5 extérieures + 5 intérieures)
    # Le pentagramme est construit à partir de 10 sommets alternants extérieurs et intérieurs
    points = []
    # L'angle de rotation de base en radians
    base_angle = math.radians(angle_deg)
    # Les angles pour les 10 sommets (extérieurs + intérieurs)
    # La différence d'angle entre deux sommets est 36° = 72°/2
    # On place les premiers points extérieurs aux multiples de 72°, décalés par base_angle
    # Pour les points intérieurs on décale de 36°
    r_outer = r
    # Le rayon intérieur r_inner est calculé comme r * sin(18°)/sin(54°)
    sin18 = math.sin(math.radians(18))
    sin54 = math.sin(math.radians(54))
    r_inner = r_outer * sin18 / sin54

    # Génération des 10 points (0,2,4,6,8 extérieurs ; 1,3,5,7,9 intérieurs)
    for i in range(10):
        if i % 2 == 0:
            radius = r_outer
        else:
            radius = r_inner
        theta = base_angle + i * PI / 5  # 36° en radian = PI/5
        px = xc + radius * math.sin(theta)
        py = yc + radius * math.cos(theta)
        points.append((px, py))
    return points

# Fonction pour savoir si un point est à l'intérieur d'un polygone simple
# Utilisation de la méthode ray casting (externe)
def point_in_polygon(x, y, polygon):
    cnt = 0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        # Vérifie si le segment croise la ligne horizontale y=y
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if y < y1 or y >= y2:
            continue
        # Calcule l'intersection en x du segment avec la ligne y
        xint = (y - y1) * (x2 - x1) / (y2 - y1 + EPS) + x1
        if xint > x:
            cnt += 1
    return cnt % 2 == 1

# Fonction de calcul de la distance entre deux points (x1,y1) et (x2,y2)
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Fonction pour calculer la distance minimale entre deux segments
def segment_to_segment_dist(p1, p2, p3, p4):
    # Retourne la distance minimale entre le segment p1p2 et p3p4
    # Utilise des fonctions auxiliaires pour la distance point-segment
    def point_segment_dist(px, py, ax, ay, bx, by):
        # Vecteur AB
        ABx = bx - ax
        ABy = by - ay
        # Vecteur AP
        APx = px - ax
        APy = py - ay
        # Calcul du t pour la projection
        t = (APx*ABx + APy*ABy) / (ABx*ABx + ABy*ABy + EPS)
        t = max(0, min(1, t))
        # Coordonnées projetées
        projx = ax + t * ABx
        projy = ay + t * ABy
        return math.sqrt((px - projx)**2 + (py - projy)**2)
    # Tester chacun des 4 points sur l'autre segment
    d1 = point_segment_dist(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1])
    d2 = point_segment_dist(p2[0], p2[1], p3[0], p3[1], p4[0], p4[1])
    d3 = point_segment_dist(p3[0], p3[1], p1[0], p1[1], p2[0], p2[1])
    d4 = point_segment_dist(p4[0], p4[1], p1[0], p1[1], p2[0], p2[1])
    return min(d1, d2, d3, d4)

# Fonction pour calculer la distance minimale entre deux étoiles pentagrammes
# Cette distance est zéro si elles se touchent (partagent un segment ou un point)
# sinon, c'est la plus petite distance entre leurs segments de contour
def star_to_star_distance(points1, points2):
    # points1, points2 sont des listes de 10 points formant le pentagramme
    # On regarde si ils se touchent.
    # Les edges du pentagramme sont données par l'ordre de points : on doit connecter les points dans l'ordre 0->2->4->6->8->0
    edges1 = []
    edges2 = []
    # Arêtes extérieures du pentagramme (ligne du pentagramme, pas le contour du polygone simple)
    # On suit le pentagramme : 0->2->4->6->8->0
    for i in range(5):
        e_start = points1[(2*i)%10]
        e_end = points1[(2*(i+1))%10]
        edges1.append((e_start, e_end))
    for i in range(5):
        e_start = points2[(2*i)%10]
        e_end = points2[(2*(i+1))%10]
        edges2.append((e_start, e_end))

    # Vérifie s'il y a intersection ou contact entre les segments (distance = 0)
    # Mais aussi, les étoiles peuvent être embiellées (l'une dans l'autre)
    # On vérifie aussi si un point de l'une est sur une arête de l'autre (distance 0)
    
    # Fonction auxiliaire pour intersection entre deux segments
    def seg_intersect(p1, p2, p3, p4):
        def ccw(A, B, C):
            return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
        return ccw(p1,p3,p4) != ccw(p2,p3,p4) and ccw(p1,p2,p3) != ccw(p1,p2,p4)

    # Test d'intersection
    for (a1,a2) in edges1:
        for (b1,b2) in edges2:
            if seg_intersect(a1, a2, b1, b2):
                return 0.0

    # Si aucune intersection, testons si un sommet d'une étoile est sur une arête de l'autre
    def point_on_segment(px, py, ax, ay, bx, by):
        # Vérifie si le point (px,py) est sur le segment (ax,ay)-(bx,by)
        cross = (bx-ax)*(py-ay) - (by-ay)*(px-ax)
        if abs(cross) > EPS:
            return False
        dot = (px-ax)*(bx-ax) + (py-ay)*(by-ay)
        if dot < -EPS:
            return False
        sq_len = (bx-ax)*(bx-ax)+(by-ay)*(by-ay)
        if dot - sq_len > EPS:
            return False
        return True

    for p in points1:
        for (a,b) in edges2:
            if point_on_segment(p[0], p[1], a[0], a[1], b[0], b[1]):
                return 0.0
    for p in points2:
        for (a,b) in edges1:
            if point_on_segment(p[0], p[1], a[0], a[1], b[0], b[1]):
                return 0.0

    # Sinon, ils ne se touchent pas : on calcule la distance minimale entre deux segments (edges)
    min_d = float('inf')
    for (a1,a2) in edges1:
        for (b1,b2) in edges2:
            d = segment_to_segment_dist(a1,a2,b1,b2)
            if d < min_d:
                min_d = d
    return min_d

# Fonction pour déterminer si deux étoiles se touchent (distance 0)
def stars_touch(points1, points2):
    # Si distance minimale = 0, alors elles se touchent
    return star_to_star_distance(points1, points2) < EPS

# Programme principal
def main():
    input = sys.stdin.readline
    while True:
        # Lecture des paramètres N(number of stars), M(start star), L(end star)
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        NML = list(map(int, line.strip().split()))
        if len(NML) != 3:
            continue
        N, M, L = NML
        if N == 0 and M == 0 and L == 0:
            break

        stars = []
        for _ in range(N):
            while True:
                line = sys.stdin.readline()
                if line.strip() != '':
                    break
            x, y, a, r = map(int, line.strip().split())
            stars.append((x, y, a, r))

        # Pour chaque étoile, générer ses 10 points du pentagramme, formant un polygone
        star_points = []
        for (x, y, a, r) in stars:
            pts = generate_star_points(x, y, a, r)
            star_points.append(pts)

        # Construction du graph
        # Les sommets sont les étoiles 0..N-1
        # Un arc a un cout 0 si les deux étoiles se touchent (sans nécessité de déplacement interstellaire)
        # Sinon, le cout est la distance minimale entre ces deux étoiles
        # On cherche le plus court chemin de M-1 à L-1 (indices 0-based)

        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                d = star_to_star_distance(star_points[i], star_points[j])
                # Si distance est nulle (elles se touchent), cout=0
                cost = d if d > EPS else 0.0
                graph[i].append((j, cost))
                graph[j].append((i, cost))

        # Recherche du plus court chemin avec Dijkstra
        start = M - 1
        end = L - 1
        dist_arr = [float('inf')] * N
        dist_arr[start] = 0.0
        pq = [(0.0, start)]  # (distance, node)

        while pq:
            curd, u = heapq.heappop(pq)
            if dist_arr[u] < curd - EPS:
                continue
            if u == end:
                # On peut arrêter tôt
                break
            for (v, cost) in graph[u]:
                nd = curd + cost
                if nd + EPS < dist_arr[v]:
                    dist_arr[v] = nd
                    heapq.heappush(pq, (nd, v))

        # Affichage avec la précision demandée (erreur <= 0.000001)
        print("%.12f" % dist_arr[end])


if __name__ == '__main__':
    main()