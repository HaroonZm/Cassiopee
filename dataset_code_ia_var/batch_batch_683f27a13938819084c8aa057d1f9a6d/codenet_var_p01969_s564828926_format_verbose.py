from collections import deque

# Lecture des dimensions et des points de départ/arrivée
height, width, start_node, target_node = input().split()
height, width = int(height), int(width)

# Création de la carte avec des bordures pour simplifier les vérifications
map_grid = ["#" * (width + 2)]
for _ in range(height):
    row = input()
    map_grid.append("#" + row + "#")
map_grid.append("#" * (width + 2))

# Tableau de vérification pour éviter les doublons de parcours
visited_cells = [[False] * (width + 2) for _ in range(height + 2)]

# Initialisation du graphe, où chaque lettre majuscule est potentiellement un sommet
adjacency_list = {chr(ascii_code): [] for ascii_code in range(ord("A"), ord("Z") + 1)}

# Construction du graphe à partir de la carte
for y in range(1, height + 1):
    for x in range(1, width + 1):

        # Détection et exploration verticale d'un segment '|'
        if map_grid[y][x] == "|" and not visited_cells[y][x]:
            vertical_x, vertical_y = x, y
            start_vertex = map_grid[vertical_y - 2][vertical_x]
            # Parcours du segment vertical entier
            while map_grid[vertical_y][vertical_x] == "|":
                visited_cells[vertical_y][vertical_x] = True
                vertical_y += 1
            end_vertex = map_grid[vertical_y + 1][vertical_x]
            adjacency_list[start_vertex].append(end_vertex)
            adjacency_list[end_vertex].append(start_vertex)

        # Détection et exploration horizontale d'un segment '-'
        if map_grid[y][x] == "-" and not visited_cells[y][x]:
            horizontal_x, horizontal_y = x, y
            start_vertex = map_grid[horizontal_y][horizontal_x - 2]
            # Parcours du segment horizontal entier
            while map_grid[horizontal_y][horizontal_x] == "-":
                visited_cells[horizontal_y][horizontal_x] = True
                horizontal_x += 1
            end_vertex = map_grid[horizontal_y][horizontal_x + 1]
            adjacency_list[start_vertex].append(end_vertex)
            adjacency_list[end_vertex].append(start_vertex)

# Recherche du plus court chemin avec une file BFS
search_queue = deque()
search_queue.append((0, start_node))

visited_nodes = {}
visited_nodes[start_node] = True

while search_queue:
    current_cost, current_node = search_queue.popleft()
    if current_node == target_node:
        print(current_cost)
        break
    for neighbor_node in adjacency_list[current_node]:
        if neighbor_node not in visited_nodes:
            visited_nodes[neighbor_node] = True
            search_queue.append((current_cost + 1, neighbor_node))