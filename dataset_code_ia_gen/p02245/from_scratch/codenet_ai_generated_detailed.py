from collections import deque

# Fonction pour générer les états voisins en déplaçant la case vide (0)
def get_neighbors(state):
    neighbors = []
    # Trouver l'indice de la case vide (0)
    zero_pos = state.index(0)
    # Coordonnées x,y dans la grille 3x3
    x, y = divmod(zero_pos, 3)
    # Directions possibles de déplacement (haut, bas, gauche, droite)
    directions = [(-1, 0),(1, 0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Vérifier que nx,ny est dans la grille
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Nouvel indice après déplacement
            new_pos = nx * 3 + ny
            # Copier l'état pour créer un nouveau voisin
            new_state = list(state)
            # Echanger la case vide avec la pièce voisine
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_puzzle(start_state):
    # Etat final à atteindre
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    # File d'attente pour BFS (état, distance)
    queue = deque([(start_state, 0)])
    # Ensemble des états visités pour éviter les répétitions
    visited = set([start_state])

    while queue:
        current_state, steps = queue.popleft()
        # Si l'état final est atteint, retourner le nombre d'étapes
        if current_state == goal_state:
            return steps
        # Explorer les états voisins
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    return -1  # Théoriquement jamais atteint car il y a toujours une solution

# Lecture de l'état initial à partir de l'entrée standard
initial = []
for _ in range(3):
    initial.extend(map(int, input().split()))

start_state = tuple(initial)
# Calcul et affichage du nombre minimal de déplacements
print(solve_puzzle(start_state))