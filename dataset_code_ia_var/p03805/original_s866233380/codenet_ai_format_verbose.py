import sys

# Lecture du nombre de sommets et d'arêtes à partir de l'entrée standard
number_of_vertices, number_of_edges = [int(value) for value in sys.stdin.readline().split()]

# Initialisation du graphe sous forme de dictionnaire d'adjacence
adjacency_list_graph = {vertex_index: [] for vertex_index in range(number_of_vertices)}

# Une valeur représentant l'infini pour d'éventuels besoins (non utilisée ici)
INFINITE_DISTANCE = 10 ** 18

# Lecture des arêtes et construction du graphe non orienté
for edge_index in range(number_of_edges):
    vertex_a, vertex_b = [int(value) for value in sys.stdin.readline().split()]
    # Conversion vers l'index de base zéro
    vertex_a -= 1
    vertex_b -= 1
    adjacency_list_graph[vertex_a].append(vertex_b)
    adjacency_list_graph[vertex_b].append(vertex_a)

# Tableau de mémoïsation pour la programmation dynamique bitmaskée
# memoization_table[state_bitmask][current_vertex] stocke le nombre de chemins pour un état donné et un sommet courant
memoization_table = [
    [-1 for vertex_index in range(number_of_vertices)]
    for state_bitmask in range(1 << number_of_vertices)
]

def count_hamiltonian_paths(state_bitmask, current_vertex):
    """
    Calcule de façon récursive le nombre de chemins hamiltoniens qui visitent chaque sommet exactement une fois,
    en partant du sommet 0, avec les sommets visités codés par state_bitmask et le sommet courant indiqué.
    """
    if memoization_table[state_bitmask][current_vertex] >= 0:
        return memoization_table[state_bitmask][current_vertex]

    # Si tous les sommets ont été visités, il existe un chemin valide.
    if state_bitmask == (1 << number_of_vertices) - 1:
        return 1

    total_paths_from_current = 0

    # Parcours des sommets voisins du sommet courant
    for neighbor_vertex in adjacency_list_graph[current_vertex]:
        has_already_visited_neighbor = (state_bitmask >> neighbor_vertex) & 1
        if not has_already_visited_neighbor:
            updated_state_bitmask = state_bitmask | (1 << neighbor_vertex)
            total_paths_from_current += count_hamiltonian_paths(updated_state_bitmask, neighbor_vertex)

    memoization_table[state_bitmask][current_vertex] = total_paths_from_current
    return total_paths_from_current

# On commence à partir du sommet 0, avec seulement ce sommet visité (bit 0 à 1)
starting_state_bitmask = 1
starting_vertex = 0

number_of_hamiltonian_paths = count_hamiltonian_paths(starting_state_bitmask, starting_vertex)

print(number_of_hamiltonian_paths)