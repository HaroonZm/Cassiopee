import sys
import heapq

def solve():
    # Lecture multiple datasets jusqu'à ce que (0,0) soit rencontré
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        # Construction du graphe : liste d'adjacence où chaque noeud a une liste de (voisin, coût)
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append((b,c))
            graph[b].append((a,c))

        # On va utiliser un Dijkstra modifié avec un état supplémentaire indiquant si la réduction
        # a été utilisée ou pas.
        # dist[node][used] = coût minimum pour atteindre node
        # used = 0 si la réduction non utilisée,
        #        1 si la réduction utilisée
        INF = 10**9
        dist = [[INF]*2 for _ in range(n+1)]
        dist[1][0] = 0

        # File de priorité contenant (coût_courant, noeud_courant, used)
        pq = []
        heapq.heappush(pq, (0, 1, 0))

        while pq:
            cost, u, used = heapq.heappop(pq)
            if dist[u][used] < cost:
                continue
            if u == n:
                # On a atteint la destination, affichage immédiat possible mais on continue pour s'assurer du minimum
                # On peut sortir dès qu'on pop car la file est triée et ce sera le min
                print(cost)
                break

            # Exploration des voisins sans utiliser la réduction (normal)
            for v, c in graph[u]:
                ncost = cost + c
                if dist[v][used] > ncost:
                    dist[v][used] = ncost
                    heapq.heappush(pq, (ncost, v, used))

            # Si la réduction n'a pas encore été utilisée, essayer de l'appliquer à deux segments consécutifs
            if used == 0:
                # On parcourt les voisins de u
                for v1, c1 in graph[u]:
                    # De v1, on parcourt à nouveau ses voisins (segment consécutif)
                    for v2, c2 in graph[v1]:
                        # Conditions: 
                        # - On est sûr que u->v1->v2 forme deux segments consécutifs
                        # - Le passage est gratuit donc coût 0 pour ces deux segments
                        # - Même si v1 ou v2 = n (destination), ce n'est pas défini qu'on s'arrête là, on met à jour dist
                        #   mais le problème dit qu'atteindre n en milieu de ces 2 segments ne suffit pas..
                        #   Or ici on considère qu'on peut "passer" par n hors de l'arrivée finale, 
                        #   c'est cohérent avec le fait que le parcours dans dijkstra continue après n.
                        #   On ne s'arrête qu'au moment ou on pop n depuis la file.
                        ncost = cost + 0
                        if dist[v2][1] > ncost:
                            dist[v2][1] = ncost
                            heapq.heappush(pq, (ncost, v2, 1))

solve()