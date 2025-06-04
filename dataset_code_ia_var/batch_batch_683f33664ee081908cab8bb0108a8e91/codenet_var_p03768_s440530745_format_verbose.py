from collections import deque

# Lecture des entrées
number_of_nodes, number_of_edges, *input_list = map(int, open(0).read().split())

# Construction de la liste d'adjacence pour les arêtes du graphe
adjacency_list = [[] for _ in range(number_of_nodes + 1)]

for node_a, node_b in zip(*[iter(input_list[:2 * number_of_edges])] * 2):
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

# Initialisation des couleurs et du suivi des visites
node_colors = [0] * (number_of_nodes + 1)
max_depth_visited = [-1] * (number_of_nodes + 1)

# Traitement des opérations de colorations en commençant par la dernière
for start_node, depth_limit, color_id in reversed(tuple(zip(*[iter(input_list[2 * number_of_edges + 1:])] * 3))):
    node_queue = deque([(depth_limit, start_node)])
    while node_queue:
        current_depth, current_node = node_queue.popleft()

        if max_depth_visited[current_node] >= current_depth:
            continue

        if node_colors[current_node] == 0:
            node_colors[current_node] = color_id

        max_depth_visited[current_node] = current_depth

        if current_depth > 0:
            for neighbor in adjacency_list[current_node]:
                node_queue.append( (current_depth - 1, neighbor) )

# Affichage des couleurs assignées à chaque noeud (hors noeud 0)
for node_color in node_colors[1:]:
    print(node_color)