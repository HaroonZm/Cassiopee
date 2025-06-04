# Lecture des entrées
N = int(input())  # Nombre de pièces
positions = list(map(int, input().split()))  # Positions initiales des pièces, index 0 correspond à la pièce 1

M = int(input())  # Nombre d'opérations
operations = list(map(int, input().split()))  # Pièces à déplacer à chaque opération, pièces numérotées à partir de 1

# On utilise une liste pour suivre les positions des pièces, index i pour pièce i+1
# positions est déjà initialisé

# Pour faciliter la vérification des cases occupées,
# on maintient un ensemble des positions occupées
occupied = set(positions)

GOAL = 2019  # numéro de la case d'arrivée

for move in operations:
    piece_index = move - 1
    current_pos = positions[piece_index]
    next_pos = current_pos + 1

    # Vérifie si la pièce est déjà sur la case but
    if current_pos == GOAL:
        # Ne peut pas avancer
        continue

    # Vérifie si la case suivante est libre
    if next_pos in occupied:
        # Ne peut pas avancer
        continue

    # Sinon, la pièce avance d'une case
    # On met à jour occupied en retirant l'ancienne position
    occupied.remove(current_pos)
    positions[piece_index] = next_pos
    occupied.add(next_pos)

# Affichage du résultat : position finale de chaque pièce
for pos in positions:
    print(pos)