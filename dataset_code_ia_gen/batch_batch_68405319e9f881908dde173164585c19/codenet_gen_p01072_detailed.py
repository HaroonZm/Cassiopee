# Lecture des données d'entrée
W, H, T = map(int, input().split())
p = int(input())

# Liste pour stocker les informations sur les fertilisations : (x, y, t)
fertilisations = []
for _ in range(p):
    x, y, t = map(int, input().split())
    fertilisations.append((x, y, t))

# Lecture de l'état initial de la plante dans chaque case (0 ou 1)
# On construit une grille H lignes, W colonnes
plants = [list(map(int, input().split())) for _ in range(H)]

# Initialisation de la grille des hauteurs, 0 si pas de plante, sinon 0 initialement
heights = [[0]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if plants[y][x] == 1:
            heights[y][x] = 0  # plante initiale de hauteur 0
        else:
            heights[y][x] = -1  # indique pas de plante

# Traitement des fertilisations
# Chaque fertilisation à un temps t < T ; si plante à cet endroit, la hauteur augmente de 1
for (x, y, t) in fertilisations:
    # On ne fertilise qu'avant T (donné dans l'énoncé)
    if t < T and heights[y][x] != -1:
        heights[y][x] += 1

# Calcul de la somme des hauteurs à l'instant T
# Hauteur -1 correspond à pas de plante donc hauteur 0
total_height = 0
for y in range(H):
    for x in range(W):
        if heights[y][x] != -1:
            total_height += heights[y][x]

# Affichage du résultat
print(total_height)