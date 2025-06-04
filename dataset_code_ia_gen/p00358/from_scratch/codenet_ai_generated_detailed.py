# Solution au problème AOTC Loading

# Contexte :
# La salle de chargement a une largeur fixe de 4 mètres (soit 4 partitions de 1m x 1m)
# et une profondeur H (nombre de partitions en longueur).
# Les cargaisons à charger font chacune 2m x 2m, soit 2 partitions en largeur et 2 partitions en profondeur.
# L'objectif est de placer le maximum de ces cargaisons dans cet espace,
# sachant que certaines partitions sont interdites (chargement interdit),
# et que chaque cargaison doit être posée parfaitement alignée sur la grille de 1m x 1m,
# sans chevauchement ni placement penché ou empilé.

# Approche :
# - Chaque cargaison occupe un carré de 2x2 partitions.
# - Le nombre de positions candidates sur la largeur est 3 (colonnes 0,1,2 car 2m oblige une largeur de 2 partitions),
#   et sur la profondeur de 0 à H-2.
# - Pour chaque position candidate (x,y), on vérifie si les 4 partitions couvertes (2x2) sont toutes autorisées.
# - Le problème revient à sélectionner un ensemble maximal de positions 2x2 non chevauchantes et autorisées.
# 
# Cela peut se modéliser comme un problème de placement maximum de dominos sur une grille avec cases interdites,
# mais ici les dominos font 2x2 blocs, et restriction de non-chevauchement.
#
# Remarques sur les contraintes:
# - La largeur est fixe (4m), donc largeur en partitions = 4.
# - Profondeur H peut aller jusqu'à 10^4.
# - Nombre de partitions interdites N peut aller jusqu'à 4*10^4.
#
# Algorithme efficace :
# - Parcourir toutes les positions candidates (x = 0..2, y=0..H-2)
# - Vérifier la disponibilité des 4 partitions 2x2: (x,y), (x+1,y), (x,y+1), (x+1,y+1)
# - Construire un graphe de conflits entre positions overlapping.
# - Puis trouver un maximum matching ou maximum independent set.
#
# Cependant, vu la structure, on peut remarquer que les positions 2x2 peuvent être représentées comme des sommets sur une grille qui se chevauchent si adjacentes.
# On peut modéliser ce placement comme un maximum matching sur un biparti. C’est un problème classique pour placer des pièces 2x2 sur grille 4xH.

# But plus simple : On peut colorier les positions candidates (de 2x2) en noir/blanc en damier selon (x+y)%2.
# Deux positions candidates adjacentes se chevauchent. Toutes les positions candidates de couleur noire sont en conflit avec certaines blanches.
# Construire un graphe biparti où les sommets sont les positions candidates (2x2) noires et blanches,
# une arête existe si deux positions chevauchent (une noire, une blanche).
# Ensuite un maximum matching dans ce graphe donne le placement maximum.

# Pour construire le graphe :
# - La largeur est 4, positions de x possibles: 0,1,2
# - Profondeur y: 0..H-2
# Position candidate (x,y) correspond à un rectangle de 2x2 partitions.

# Deux positions candidates chevauchent si elles partagent au moins une partition.
# Vu la topologie, seuls les voisins directs dans certaines directions se chevauchent.

# Les arcs de chevauchement dans le graphe seront générés selon les positions adjacentes:
# Une position noire et une blanche sont adjacentes s'ils se chevauchent.

# Enfin, le résultat du maximum matching est substracté au nombre total de positions candidates autorisées pour obtenir
# le maximum de cargaisons placées.

# Implémentons cette approche avec un algorithme de Hopcroft-Karp pour le maximum matching biparti.

import sys
sys.setrecursionlimit(10**7)

def main():
    import sys

    input = sys.stdin.readline

    H, N = map(int, input().split())

    # Garder une grille indiquant partitions interdites
    # Grille taille 4 x H
    forbidden = [[False]*H for _ in range(4)]
    for _ in range(N):
        x_i, y_i = map(int, input().split())
        forbidden[x_i][y_i] = True

    # Positions candidates de 2x2 possibles :
    # x in [0,1,2], y in [0..H-2]
    # On ne peut placer un cargo si au moins une des 4 partitions est interdite
    positions = []
    # Indexation des positions pour construire graph
    pos_index = dict()

    idx = 0
    for y in range(H-1):
        for x in range(3):
            # vérifier 2x2 zones: (x,y),(x+1,y),(x,y+1),(x+1,y+1)
            if (not forbidden[x][y] and not forbidden[x+1][y] and
                not forbidden[x][y+1] and not forbidden[x+1][y+1]):
                positions.append( (x,y) )
                pos_index[(x,y)] = idx
                idx +=1

    # Si aucun emplacement possible
    if idx == 0:
        print(0)
        return

    # Colorier les positions selon (x+y)%2 (damier)
    # Ceci permet de construire un biparti
    black = set()
    white = set()
    for p in positions:
        x,y = p
        if (x + y) % 2 == 0:
            black.add(p)
        else:
            white.add(p)

    # Construire un graphe biparti:
    # Chaque sommet -> un position candidate
    # Arête entre deux positions si elles se chevauchent
    # Deux positions qui chevauchent doivent avoir une case commune

    # Pour un position p=(x,y), on checka les positions voisines qui chevauchent
    # Vu la structure: une position chevauche une autre si elles partagent au moins une partition

    # Construire la liste d'adjacences: pour chaque position noire, sa liste de positions blanches voisines

    graph = [[] for _ in range(idx)]

    # Fonction pour vérifier chevauchement entre 2 positions candidates (2x2)
    def overlap(p1, p2):
        x1,y1 = p1
        x2,y2 = p2
        # Ensemble des partitions couvertes par p1
        s1 = set([(x1,y1),(x1+1,y1),(x1,y1+1),(x1+1,y1+1)])
        s2 = set([(x2,y2),(x2+1,y2),(x2,y2+1),(x2+1,y2+1)])
        return len(s1 & s2) >0

    # Pour accélérer, on peut indexer les positions par coordonnées pour rechercher voisins potentiels
    # Positions sont sur grille 3 x (H-1), on teste seulement positions blanches proches d’une noire

    # Construire une recherche rapide
    white_positions_set = white

    # Pour chaque noire, on cherche les blanches voisines dans une zone proche (+-1 en x,y)
    for p_black in black:
        x_b, y_b = p_black
        idx_b = pos_index[p_black]
        # on teste toutes blanches dans zone x_b+-1, y_b+-1
        candidate_white = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                x_c = x_b + dx
                y_c = y_b + dy
                if 0 <= x_c <=2 and 0 <= y_c <= H-2:
                    p_white = (x_c, y_c)
                    if p_white in white_positions_set:
                        # Si chevauchent, on ajoute l'arete
                        if overlap(p_black, p_white):
                            idx_w = pos_index[p_white]
                            graph[idx_b].append(idx_w)

    # Nombre de sommets sets:
    # G= (U,V,E)
    # U=black vertices (indices = pos_index for black positions)
    # V=white vertices (indices also from pos_index for white positions)
    # Positions indices cover both sets, so on Matching, we use the index sets for black and white.

    # Construire structures de sommets noirs et blancs
    # Créer une liste des sommets noirs par leur indices
    black_indices = [pos_index[p] for p in black]
    white_indices = [pos_index[p] for p in white]

    # Pour matching, reconstruire un mapping:
    # Indices dans graph correspond aux positions candidates (noir + blanc)
    # Mais seuls les noirs ont des arêtes vers les blancs (graph est de taille = nombre positions)

    # On va réaliser Hopcroft-Karp pour maximiser le matching dans ce graphe biparti,
    # où les sommets de U sont black_indices, et les sommets de V sont white_indices.

    # Construire un tableau pour vérifier si un noeud est black or white
    is_black = [False]*idx
    for i in black_indices:
        is_black[i] = True

    # Adapter graph pour que graph[u] soit liste de voisins dans V pour u in U
    # Ici u est un noeud noir
    # Hopcroft-Karp standard :

    from collections import deque

    INF = 10**9

    # U = sommets noirs
    # V = sommets blancs

    # On numeote U de 0 à len(black_indices)-1
    # et V de 0 à len(white_indices)-1
    # Donc on doit faire une correspondance d'indices

    black_id = dict()
    for i,u in enumerate(black_indices):
        black_id[u] = i

    white_id = dict()
    for i,v in enumerate(white_indices):
        white_id[v] = i

    # Construire le graphe biparti simplifié
    G = [[] for _ in range(len(black_indices))]
    for u in black_indices:
        u_i = black_id[u]
        for v in graph[u]:
            if v in white_id:
                v_i = white_id[v]
                G[u_i].append(v_i)

    # Variables du matching
    pair_u = [-1]*len(black_indices)
    pair_v = [-1]*len(white_indices)
    dist = [0]*len(black_indices)

    def bfs():
        queue = deque()
        for u in range(len(black_indices)):
            if pair_u[u]<0:
                dist[u]=0
                queue.append(u)
            else:
                dist[u]=INF
        d = INF
        while queue:
            u = queue.popleft()
            if dist[u]<d:
                for v in G[u]:
                    w = pair_v[v]
                    if w<0:
                        d = dist[u]+1
                    elif w>=0 and dist[w]==INF:
                        dist[w] = dist[u]+2
                        queue.append(w)
        return d!=INF

    def dfs(u):
        for v in G[u]:
            w = pair_v[v]
            if w<0 or (dist[w]==dist[u]+2 and dfs(w)):
                pair_u[u]=v
                pair_v[v]=u
                return True
        dist[u]=INF
        return False

    matching =0
    while bfs():
        for u in range(len(black_indices)):
            if pair_u[u]<0 and dfs(u):
                matching+=1

    # Total positions candidates = idx
    # Maximum independent set dans ce graphe biparti = total_positions - matching
    # Cela correspond au maximum nombre de positions 2x2 plaçables sans conflit

    print(idx - matching)

if __name__ == "__main__":
    main()