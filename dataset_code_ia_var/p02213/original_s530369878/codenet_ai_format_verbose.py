# Lecture de la taille de la grille
grid_height, grid_width = map(int, input().split())

# Lecture des lignes de la grille
grid_cells = [list(input()) for _ in range(grid_height)]

# Tableau pour marquer les cellules visitées
visited_cells = [[False] * grid_width for _ in range(grid_height)]

# Initialisation de la pile pour le parcours
# Format de l’élément : (ligne, colonne, orientation_du_dé)
# orientation_du_dé : (haut, droite, face, gauche, bas, arrière)
search_stack = [
    (
        0,  # ligne initiale
        0,  # colonne initiale
        (5, 4, 1, 3, 6, 2)  # orientation initiale (faces du dé)
    )
]

while search_stack:
    current_row, current_column, die_faces = search_stack.pop()
    
    # Vérifications des bornes du tableau
    if (current_row < 0 or
        current_column < 0 or
        current_row >= grid_height or
        current_column >= grid_width):
        continue

    # Vérifie si la cellule actuelle est un obstacle
    if grid_cells[current_row][current_column] == "#":
        continue

    # Vérifie si la cellule a déjà été visitée
    if visited_cells[current_row][current_column]:
        continue

    # Vérifie si le nombre sur la face du dessous correspond à la cellule
    index_face_bottom = 4
    if int(grid_cells[current_row][current_column]) != die_faces[index_face_bottom]:
        continue

    # Marque la cellule comme visitée
    visited_cells[current_row][current_column] = True

    # Ajoute les quatre déplacements possibles dans la pile, avec la nouvelle orientation du dé
    # Déplacement vers le haut (nord)
    new_die_faces_north = (
        die_faces[2],
        die_faces[1],
        die_faces[5],
        die_faces[3],
        die_faces[0],
        die_faces[4]
    )
    search_stack.append((current_row - 1, current_column, new_die_faces_north))

    # Déplacement vers le bas (sud)
    new_die_faces_south = (
        die_faces[4],
        die_faces[1],
        die_faces[0],
        die_faces[3],
        die_faces[5],
        die_faces[2]
    )
    search_stack.append((current_row + 1, current_column, new_die_faces_south))

    # Déplacement vers la gauche (ouest)
    new_die_faces_west = (
        die_faces[0],
        die_faces[2],
        die_faces[3],
        die_faces[4],
        die_faces[1],
        die_faces[5]
    )
    search_stack.append((current_row, current_column - 1, new_die_faces_west))

    # Déplacement vers la droite (est)
    new_die_faces_east = (
        die_faces[0],
        die_faces[4],
        die_faces[1],
        die_faces[2],
        die_faces[3],
        die_faces[5]
    )
    search_stack.append((current_row, current_column + 1, new_die_faces_east))

# Affichage du résultat
if visited_cells[grid_height - 1][grid_width - 1]:
    print("YES")
else:
    print("NO")