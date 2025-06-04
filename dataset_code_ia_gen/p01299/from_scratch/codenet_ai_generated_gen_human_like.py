import sys
import math

def circles_intersect(c1, c2):
    # retourne True si les cercles c1 et c2 se touchent ou se croisent
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    dist = math.hypot(x1 - x2, y1 - y2)
    return dist <= r1 + r2

def point_in_circle(px, py, circle):
    x, y, r = circle
    return math.hypot(px - x, py - y) <= r

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        xs, ys, xt, yt = map(int, input().split())
        circles = [tuple(map(int, input().split())) for _ in range(n)]
        
        # Construire un graphe où les noeuds sont les cercles,
        # et les arcs existent entre cercles intersectants,
        # plus deux noeuds supplémentaires: start et end (indice n et n+1)
        # start est connecté aux cercles couvrant la position de la sourie
        # end est connecté aux cercles couvrant la position du poisson
        
        graph = [[] for _ in range(n+2)]
        START = n
        END = n+1
        
        # Connexions start -> cercles qui contiennent le point (rat's lair)
        for i, c in enumerate(circles):
            if point_in_circle(xs, ys, c):
                graph[START].append(i)
                graph[i].append(START)
            if point_in_circle(xt, yt, c):
                graph[END].append(i)
                graph[i].append(END)
        
        # Connexions entre cercles
        for i in range(n):
            for j in range(i+1, n):
                if circles_intersect(circles[i], circles[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Si start et end sont directement connectés
        if END in graph[START]:
            print(0)
            continue
        
        # On cherche la distance minimale (en nombre de murs à franchir) entre start et end
        dist = [-1] * (n+2)
        dist[START] = 0
        from collections import deque
        q = deque([START])
        while q:
            u = q.popleft()
            if u == END:
                break
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        # Le résultat correspond au nombre d'arcs traversés entre start et end,
        # or start et end ont un décalage de +1 avec les indices des cercles,
        # chaque arc correspond à franchir un mur. Le résultat est dist[END] - 1
        # car on ne compte pas l'arrivée sur la position finale comme franchissement de mur.
        # Si dist[END] == -1, alors aucune route n'est possible, donc 0 murs à franchir (plein accès)
        if dist[END] == -1:
            print(0)
        else:
            # Le chemin comprend (dist[END]) noeuds incluant start et end,
            # donc nombre d'arêtes franchies = dist[END] - 1
            print(dist[END] - 1)

if __name__ == "__main__":
    main()