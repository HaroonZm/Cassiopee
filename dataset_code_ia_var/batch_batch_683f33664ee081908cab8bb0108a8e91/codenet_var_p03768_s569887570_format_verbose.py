from collections import deque

# Lecture des entrées pour le nombre de sommets et d'arêtes
number_of_vertices, number_of_edges = map(int, input().split())

# Initialisation de la liste d'adjacence pour le graphe
adjacency_list = [[] for _ in range(number_of_vertices)]

# Construction de la liste d'adjacence d'après les entrées
for _ in range(number_of_edges):
    vertex_start, vertex_end = map(int, input().split())
    adjacency_list[vertex_start - 1].append(vertex_end - 1)
    adjacency_list[vertex_end - 1].append(vertex_start - 1)

# Lecture du nombre de requêtes
number_of_queries = int(input())

# Lecture et stockage de toutes les requêtes sous forme de liste
queries = [list(map(int, input().split())) for _ in range(number_of_queries)]

# Initialisation des couleurs (ou valeurs) des sommets à 0 (non coloriés)
vertex_colors = [0] * number_of_vertices

# Initialisation de la profondeur maximale déjà visitée pour chaque sommet
visited_depth = [-1] * number_of_vertices

# Traitement des requêtes en partant de la dernière vers la première
for vertex_query, depth_query, color_query in reversed(queries):

    # File pour le parcours en largeur, stockant : sommet courant, profondeur restante, couleur à appliquer
    bfs_queue = deque([(vertex_query - 1, depth_query, color_query)])

    while bfs_queue:
        current_vertex, current_depth, current_color = bfs_queue.popleft()

        # Vérifie si ce sommet a été déjà visité à profondeur supérieure ou égale
        if visited_depth[current_vertex] >= current_depth:
            continue

        # Met à jour la profondeur maximale pour ce sommet
        visited_depth[current_vertex] = current_depth

        # Applique la couleur si ce sommet n'a pas déjà été colorié par une requête ultérieure
        if vertex_colors[current_vertex] == 0:
            vertex_colors[current_vertex] = current_color

        # Si la profondeur permet de propager, empile les sommets voisins
        if current_depth > 0:
            for adjacent_vertex in adjacency_list[current_vertex]:
                bfs_queue.append((adjacent_vertex, current_depth - 1, current_color))

# Affichage de la couleur finale de chaque sommet du graphe
for vertex_index in range(number_of_vertices):
    print(vertex_colors[vertex_index])