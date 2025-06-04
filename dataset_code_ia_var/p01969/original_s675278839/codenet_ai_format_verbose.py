from collections import deque

# Lecture et initialisation des dimensions et points de départ/arrivée
grid_height_input, grid_width_input, start_label, target_label = input().split()
grid_height = int(grid_height_input)
grid_width = int(grid_width_input)

# Construction de la matrice avec des bordures de sécurité
grid_with_border = [("." * (grid_width + 2))]
unique_node_positions = {}

for row_index in range(grid_height):
    input_row = input()
    grid_with_border.append("." + input_row + ".")

grid_with_border.append("." * (grid_width + 2))
grid_height_with_border = grid_height + 2
grid_width_with_border = grid_width + 2

# Extraction des noeuds uniques dans le graphe à partir des caractères présents
for row_idx in range(grid_height_with_border):
    for col_idx in range(grid_width_with_border):
        cell_character = grid_with_border[row_idx][col_idx]
        if cell_character not in [".", "-", "|", "o"]:
            unique_node_positions[cell_character] = [row_idx, col_idx]

# Construction du graphe d'adjacence pour chaque noeud unique identifié
adjacency_graph = {node_label: [] for node_label in unique_node_positions.keys()}

for node_label, (node_row, node_col) in unique_node_positions.items():
    # Vérification des connexions horizontales vers la droite
    if grid_with_border[node_row][node_col + 2] == "-":
        offset = 2
        while grid_with_border[node_row][node_col + offset] == "-":
            offset += 1
        adjacent_node_label = grid_with_border[node_row][node_col + offset + 1]
        adjacency_graph[node_label].append(adjacent_node_label)
    # Vérification des connexions horizontales vers la gauche
    if grid_with_border[node_row][node_col - 2] == "-":
        offset = 2
        while grid_with_border[node_row][node_col - offset] == "-":
            offset += 1
        adjacent_node_label = grid_with_border[node_row][node_col - offset - 1]
        adjacency_graph[node_label].append(adjacent_node_label)
    # Vérification des connexions verticales vers le bas
    if grid_with_border[node_row + 2][node_col] == "|":
        offset = 2
        while grid_with_border[node_row + offset][node_col] == "|":
            offset += 1
        adjacent_node_label = grid_with_border[node_row + offset + 1][node_col]
        adjacency_graph[node_label].append(adjacent_node_label)
    # Vérification des connexions verticales vers le haut
    if grid_with_border[node_row - 2][node_col] == "|":
        offset = 2
        while grid_with_border[node_row - offset][node_col] == "|":
            offset += 1
        adjacent_node_label = grid_with_border[node_row - offset - 1][node_col]
        adjacency_graph[node_label].append(adjacent_node_label)

# Initialisation du suivi des noeuds visités pour le parcours
visited_nodes = {node_label: False for node_label in unique_node_positions.keys()}

# Recherche en largeur pour trouver le plus court chemin du départ à la cible
breadth_first_search_queue = deque([[start_label, 0]])

while breadth_first_search_queue:
    current_node_label, current_distance = breadth_first_search_queue.popleft()
    visited_nodes[current_node_label] = True
    for neighbor_label in adjacency_graph[current_node_label]:
        if neighbor_label == target_label:
            print(current_distance + 1)
            breadth_first_search_queue = []
            break
        if visited_nodes[neighbor_label]:
            continue
        else:
            breadth_first_search_queue.append([neighbor_label, current_distance + 1])