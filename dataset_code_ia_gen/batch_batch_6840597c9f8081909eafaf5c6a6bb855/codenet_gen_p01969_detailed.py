# Solution complète en Python pour le problème AA Graph
# L'idée est de parser la grille ASCII, identifier les sommets (lettres majuscules),
# puis construire un graphe de connectivité entre ces sommets en suivant les contraintes données.
# Ensuite, on effectue un BFS pour obtenir la distance minimale entre s et t.

from collections import deque

def main():
    # Lecture des entrées
    H, W, s, t = input().split()
    H, W = int(H), int(W)
    grid = [list(input()) for _ in range(H)]

    # On va stocker les positions des sommets sous la forme dict : lettre -> (i,j)
    vertices = {}
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if 'A' <= c <= 'Z':
                vertices[c] = (i, j)

    # Un sommet est entouré par des 'o' de 8 voisins :
    # ooo
    # oAo
    # ooo
    # Nous devons repérer les connections aux sommets voisins par les 'o' reliés par '-' ou '|'

    # Pour faciliter la recherche, on note les directions de connexion possibles:
    # Un sommet peut avoir au plus 1 arête dans chaque direction: haut, bas, gauche, droite.
    # Chaque arête relie la lettre à un 'o' adjacent, puis à une chaîne continue de '-' (horizontal)
    # ou '|' (vertical) qui mène à un autre 'o', adjacent enfin à un autre sommet.
    # Les 'o' entourent les sommets sur 8 positions, mais les arêtes partent strictement vers N,S,E,O.

    # Définition de décalages pour les voisins autour d'un sommet (8 voisins)
    neighbors_8 = [(-1,-1), (-1,0), (-1,1),
                   ( 0,-1),         ( 0,1),
                   ( 1,-1), ( 1,0), ( 1,1)]

    # Les directions principales et leurs caractéristiques :
    # (di, dj, symbole attendus sur le chemin)
    directions = {
        'up':    (-1,  0, '|'),
        'down':  ( 1,  0, '|'),
        'left':  ( 0, -1, '-'),
        'right': ( 0,  1, '-'),
    }

    # Fonction pour vérifier si une position est dans la grille
    def in_grid(i,j):
        return 0 <= i < H and 0 <= j < W

    # Fonction pour trouver la position du 'o' entourant un sommet dans une direction donnée
    # Le 'o' sort d'un sommet A est une des 8 cases autour du sommet.
    # Pour que ce soit une direction valide (up, down, left, right),
    # on sait que l'o correspondant est au voisin dans la direction verticale ou horizontale,
    # ou à un des 'o' directement diagonaux proches (parfois nécessaires à vérifier)
    # mais selon l'énoncé, les arêtes sortent des 'o' qui sont dans 4 directions N,S,E,O.
    # En testant la figure, il semble que le 'o' sans ambiguïté est dans la direction immédiate
    # N,S,E,O (pas diagonale).

    # Donc on va chercher pour chaque direction si à la position (i + di, j + dj) on trouve un 'o'.
    # Sinon, pas d'arête dans cette direction.

    # On construira un graphe : dict de sommet -> liste de sommets atteignables par une arête
    graph = { key: [] for key in vertices.keys() }

    for v, (vi,vj) in vertices.items():
        # Pour chaque sommet, rechercher pour chaque direction s'il y a une arête
        for di, dj, symbol in directions.values():
            oi, oj = vi + di, vj + dj  # Position du 'o' adjacent au sommet dans cette direction
            
            if not in_grid(oi, oj): 
                continue
            if grid[oi][oj] != 'o': 
                # Pas de départ d'arête dans cette direction
                continue

            # Depuis ce premier 'o', on suit la chaîne d'arête constituée de symbol (| ou -)
            # On descend le long de la direction jusqu'à trouver un 'o' voisin d'un autre sommet
            # : le deuxième 'o' sera adjacent à une autre lettre majuscule

            # Parcours le chemin de l'arête
            ci, cj = oi, oj
            while True:
                ni, nj = ci + di, cj + dj
                if not in_grid(ni, nj):
                    # Arrêt hors grille => pas d'arête valide
                    break

                c_next = grid[ni][nj]

                if c_next == 'o':
                    # Ce 'o' devrait être adjacent à une lettre majuscule dans l'une des 8 positions autour
                    # Cherchons la lettre correspondante (autre que v)
                    found_vertex = None
                    for ddi, ddj in neighbors_8:
                        vi2, vj2 = ni + ddi, nj + ddj
                        if not in_grid(vi2, vj2):
                            continue
                        c2 = grid[vi2][vj2]
                        if 'A' <= c2 <= 'Z' and c2 != v:
                            found_vertex = c2
                            break
                    if found_vertex is not None:
                        # On a trouvé une arête entre v et found_vertex
                        graph[v].append(found_vertex)
                        # Comme le graphe est non orienté (on peut cheminer dans les 2 sens),
                        # on ajoute aussi la connexion dans l'autre sens.
                        # NB: On peut faire ça plus tard, mais on le fait ici directement.
                        if found_vertex not in graph:
                            graph[found_vertex] = []
                        if v not in graph[found_vertex]:
                            graph[found_vertex].append(v)
                    break

                elif c_next == symbol:
                    # Continuer à suivre la chaîne de '-' ou '|'
                    ci, cj = ni, nj
                    continue
                else:
                    # Chemin interrompu
                    break

    # Maintenant, on a le graphe construit avec des arrêtes de longueur 1
    # On effectue une recherche en largeur (BFS) pour trouver la distance minimale entre s et t

    dist = {key: -1 for key in graph.keys()}
    dist[s] = 0
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        if cur == t:
            print(dist[cur])
            return
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    # Si pas trouvé, cela ne devrait pas arriver car le graphe est connecté
    print(-1)

if __name__ == "__main__":
    main()