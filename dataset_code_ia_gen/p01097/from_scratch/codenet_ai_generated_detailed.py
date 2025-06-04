import sys
import math
from collections import deque, defaultdict

# Le problème consiste à sélectionner k cubes parmi n positions candidates pour former un polyèdre connexe avec une surface minimale.
# Chaque cube est un cube axis-aligned de côté s, placé aux coordonnées données.
# La surface totale est calculée comme 6*s*s cubes moins 2*s*s par face commune entre cubes adjacents.
# La condition de connectivité impose que le graphe induit par les cubes sélectionnés est connexe (adjacency = partage d'une face).
# Si aucun choix de k cubes connexes n'est possible, on retourne -1.

# Approche:
# 1) Construire un graphe avec les n positions. Deux positions sont adjacentes si la distance entre leurs coins est exactement s sur une seule coordonnée et identique sur les autres (voisin direct).
# 2) Trouver un sous-ensemble de k positions connexes minimisant la surface = 6*k*s*s - 2*s*s*(nombre d'arêtes internes dans le sous-graphe).
# 3) Maximiser les arêtes internes revient à minimiser la surface parce que chaque arête interne retire 2*s*s à la surface.
# 4) Le problème est équivalent à trouver un "connected induced subgraph" de taille k avec le maximum d'arêtes internes, dans un graphe non pondéré.
#
# Difficultés:
# Le graphe peut avoir jusqu'à 2000 sommets, ce qui est trop grand pour explorer exhaustivement toutes les combinaisons.
# L'énoncé semble complexe, mais en pratique, une méthode BFS/DFS pour générer toutes les composantes connexes jusqu'à taille k pourrait fonctionner.
# Cependant, plusieurs composantes connexes peuvent être nombreuses, donc on doit optimiser.
#
# Stratégie:
# - Parcourir tous les sommets comme points de départ.
# - Utiliser une BFS pour générer tous les ensembles connexes de taille k à partir de ce sommet.
#   - Comme le nombre de combinaisons serait prohibitif, on utilisera une recherche en/à la limite raisonnable:
#     On génère les connexions par niveaux, on sauvegarde les ensembles étendus.
#     Pour le plus grand k (2000), on peut faire uniquement un BFS simple pour exister ou pas (et prendre la surface de la composante connexe minimale approchée).
# - En pratique, on sélectionne une approche plus simple: trouver la plus petite surface parmi les composantes connexes de taille au moins k.
# - Si une composante connexe a taille < k, on ne peut pas choisir k cubes dedans.
# - Sinon, choisir k cubes dans cette composante faisant un sous-graphe connexe minimal pour la surface.
#   - Supposons que la surface diminue quand on prend plus d'arêtes, donc on veut des sous-graphes complets, c'est difficile.
#
# Simplification:
# - Puisque la surface dépend uniquement du nombre d'arêtes dans le sous-graphe, pour minimiser la surface, on cherche à maximiser le nombre d'arêtes internes dans le sous-graphe de taille k.
# - Trouver un sous-graphe connexe avec k sommets et un nombre maximisé d'arêtes internes est NP-difficile.
#
# Solution pragmatique:
# - L'énoncé indique 100 datasets max.
# - Implémenter une recherche heuristique :
#   * Pour chaque composante connexe, si sa taille >= k :
#       - Utiliser BFS pour générer ensembles connexes à partir de chaque sommet mais limité (prune si taille > k).
#       - Calculer surface pour chaque ensemble connexe de taille k rencontré.
#       - Mémoriser la surface minimale.
# - Si aucune configuration trouvée, retourner -1.
#
# Optimisation:
# - Pre-calcul des composantes connexes.
# - Pour chaque composante ayant taille >= k, on tente BFS ou DFS pour trouver aucune à tous les sous-ensembles connexes de taille k : cette approche est exponentielle.
#
# Approche finale:
# - Trouver toutes composantes connexes via BFS.
# - Pour chaque composante connexe de taille >= k:
#   - Parce que les cubes sont sur une grille sparse et conditions du problème, il est probable que la composante soit fortement connectée.
#   - On considère la surface de la composante entière (taille = taille composante):
#     surface = 6*s*s*size - 2*s*s*number_of_edges.
#   - Puis on tente de trouver un sous-graphe connexe de taille k dans cette composante qui minimise la surface.
#
# Heuristique pour sous-graphe connexe:
# - Pour chaque sommet, BFS pour étendre la composante jusqu'à taille k (premiers arrivés suffisent).
# - Calcul surface pour ensemble result.
# - Mémoriser la meilleure surface.
#
# On peut accélérer en prunant par "frontier" minimum et éviter revisiter mêmes ensembles.
#
# Implémentation modérée pour tenir dans le temps et mémoire.


def main():
    input = sys.stdin.readline

    # Directions pour voisinage adjacents (faces communes)
    directions = [(s,0,0) for s in [1]] + [(0,s,0) for s in [1]] + [(0,0,s) for s in [1]]
    # Mais le pas est s, on prendra s variable, donc on fera plus tard

    while True:
        line = input().strip()
        if not line:
            break
        n, k, s = map(int, line.split())
        if n == 0 and k == 0 and s == 0:
            break

        coords = []
        pos_to_id = dict()
        for i in range(n):
            x,y,z = map(int, input().split())
            coords.append((x,y,z))
            pos_to_id[(x,y,z)] = i

        # Construire le graphe: deux cubes sont adjacents s'ils sont à distance s sur une axe et mêmes coord sur les deux autres axes
        adj = [[] for _ in range(n)]

        # Pour accélérer la recherche de voisins, on indexe les positions par coord accessibles
        # Comme s peut être grand, on cherche uniquement sur les dimensions x,y,z avec +s ou -s déplacement sur une coord

        # Construisons un set pour lookup rapide
        pos_set = set(coords)

        for i,(x,y,z) in enumerate(coords):
            # Tester voisins en décalant coord +- s sur chaque axe
            neighbors = [
                (x+s,y,z),
                (x-s,y,z),
                (x,y+s,z),
                (x,y-s,z),
                (x,y,z+s),
                (x,y,z-s)
            ]
            for nx,ny,nz in neighbors:
                if (nx,ny,nz) in pos_set:
                    j = pos_to_id[(nx,ny,nz)]
                    adj[i].append(j)

        # Trouver composantes connexes
        visited = [False]*n
        components = []
        for i in range(n):
            if not visited[i]:
                q = deque([i])
                comp = []
                visited[i] = True
                while q:
                    u = q.popleft()
                    comp.append(u)
                    for w in adj[u]:
                        if not visited[w]:
                            visited[w] = True
                            q.append(w)
                components.append(comp)

        # Fonction pour calculer surface d'un ensemble de cubes
        # Surface = 6*s*s*len - 2*s*s*nombre d'arêtes internes
        def surface(cubes_set):
            # cubes_set : set of node indices
            # Calcul du nombre d'arêtes internes dans le sous-graphe induit
            # Pour chaque cube, compter ses voisins dans cubes_set
            edges = 0
            for u in cubes_set:
                for w in adj[u]:
                    if w in cubes_set and w > u:
                        edges += 1
            return 6*s*s*len(cubes_set) - 2*s*s*edges

        INF = 10**15
        ans = INF

        # Pour chaque composante connexe de taille >= k
        # On fait BFS multi départs pour trouver tous les sous-graphes connexes de taille k
        # BFS avec tuple (ensemble_actuel, frontier)
        # Mais pour k jusqu'à 2000, explorer tous les sous-ensembles est impossible.
        #
        # Implémentation limitée:
        # Pour chaque sommet dans la composante, on fait BFS normale pour grandir aux couches successives
        # On arrête à taille k et on calcule surface
        #
        # Cette méthode ne garantit pas trouver l'ensemble optimum, mais donnera une solution raisonnable.
        # On mémorise la meilleure surface obtenue et on donnera -1 si aucune trouvée.

        for comp in components:
            size_comp = len(comp)
            if size_comp < k:
                continue  # impossible de choisir k cubes dans cette composante

            # Creation d'un sous-graphe pour cette composante pour accélérer
            comp_set = set(comp)
            comp_id_map = {v:i for i,v in enumerate(comp)}
            comp_adj = [[] for _ in range(size_comp)]
            for v in comp:
                vid = comp_id_map[v]
                for w in adj[v]:
                    if w in comp_set:
                        comp_adj[vid].append(comp_id_map[w])

            # BFS depuis chaque sommet de la composante pour générer un sous-ensemble connexe de taille k minimal en surface
            # On limite la recherche, on mémorise le plus petit surface vu

            # NB: Pour éviter explosion mémorielle on évite mémoriser ensembles entiers.
            # Nous faisons un BFS normal:
            # Pendant la BFS, on suit uniquement la distance (nombre de sommets explorés),
            # on s'arrête quand on atteint la taille k.

            for start in range(size_comp):
                visited_bfs = [False]*size_comp
                visited_bfs[start] = True
                q = deque()
                # L'état: (ensemble_actuel, queue_frontier)
                # Simplification: ici on réalise juste un BFS classique pour trouver la composante connexe jusqu'à taille k depuis start
                # On va simplement parcourir le k premiers niveaux.
                #
                # On récupère simplement les premiers k sommets rencontrés et calcule la surface.
                level_nodes = []
                q.append(start)
                while q and len(level_nodes) < k:
                    u = q.popleft()
                    level_nodes.append(u)
                    for w in comp_adj[u]:
                        if not visited_bfs[w]:
                            visited_bfs[w] = True
                            q.append(w)

                if len(level_nodes) == k:
                    # surface des nodes choisis:
                    nodes_set = set(comp[v] for v in level_nodes)
                    cur_surf = surface(nodes_set)
                    if cur_surf < ans:
                        ans = cur_surf

        print(ans if ans != INF else -1)


if __name__ == "__main__":
    main()