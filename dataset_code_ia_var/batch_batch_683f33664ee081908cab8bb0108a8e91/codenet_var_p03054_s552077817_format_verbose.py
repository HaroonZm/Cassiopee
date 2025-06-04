import sys

# Lecture des dimensions de la grille et du nombre de mouvements
grid_height, grid_width, movement_count = map(int, input().split())

# Lecture de la position initiale (1-indexée) du joueur
start_row, start_col = map(int, input().split())
start_row -= 1
start_col -= 1

# Lecture de la liste des mouvements du joueur et de l'adversaire
player_moves = list(input())
opponent_moves = list(input())

# Dictionnaires pour correspondre les directions aux indices et décalages
direction_to_index_increase = {"U": 0, "D": 1, "R": 2, "L": 3}
direction_to_index_decrease = {"U": 1, "D": 0, "R": 3, "L": 2}
direction_to_delta = {"U": -1, "D": 1, "R": 1, "L": -1}

# Initialisation des listes de positions pour chaque direction
positions_per_direction = [
    [start_row],  # Up
    [start_row],  # Down
    [start_col],  # Right
    [start_col]   # Left
]

# Construction des séquences de mouvements pour chaque direction
for move_index in range(movement_count):
    # Actions basées sur le mouvement du joueur
    direction_ind_player = direction_to_index_increase[player_moves[move_index]]
    positions_per_direction[direction_ind_player].append(direction_to_delta[player_moves[move_index]])
    # Actions basées sur le mouvement de l'adversaire
    direction_ind_opponent = direction_to_index_decrease[opponent_moves[move_index]]
    positions_per_direction[direction_ind_opponent].append(direction_to_delta[opponent_moves[move_index]])

# Vérification des positions dans chaque direction pour s'assurer que le joueur n'est pas hors de la grille

# Vérification pour les mouvements vers le haut
position_sequence_up = positions_per_direction[0]
for current_step in range(1, len(position_sequence_up)):
    position_sequence_up[current_step] = min(grid_height - 1, position_sequence_up[current_step] + position_sequence_up[current_step - 1])
    if position_sequence_up[current_step] == -1:
        print("NO")
        sys.exit()

# Vérification pour les mouvements vers le bas
position_sequence_down = positions_per_direction[1]
for current_step in range(1, len(position_sequence_down)):
    position_sequence_down[current_step] = max(0, position_sequence_down[current_step] + position_sequence_down[current_step - 1])
    if position_sequence_down[current_step] == grid_height:
        print("NO")
        sys.exit()

# Vérification pour les mouvements vers la gauche
position_sequence_left = positions_per_direction[3]
for current_step in range(1, len(position_sequence_left)):
    position_sequence_left[current_step] = min(grid_width - 1, position_sequence_left[current_step] + position_sequence_left[current_step - 1])
    if position_sequence_left[current_step] == -1:
        print("NO")
        sys.exit()

# Vérification pour les mouvements vers la droite
position_sequence_right = positions_per_direction[2]
for current_step in range(1, len(position_sequence_right)):
    position_sequence_right[current_step] = max(0, position_sequence_right[current_step] + position_sequence_right[current_step - 1])
    if position_sequence_right[current_step] == grid_width:
        print("NO")
        sys.exit()

print("YES")