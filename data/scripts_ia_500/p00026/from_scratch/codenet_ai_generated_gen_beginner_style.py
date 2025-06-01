# initialisation du papier 10x10 avec des densités à 0
paper = [[0 for _ in range(10)] for _ in range(10)]

def apply_drop(x, y, size):
    # définir les cellules affectées par la goutte selon sa taille
    # taille 1 : point (x,y) uniquement
    # taille 2 : point + ses 4 voisins orthogonaux
    # taille 3 : taille 2 + les 4 voisins diagonaux
    coords = []
    if size == 1:
        coords = [(x,y)]
    elif size == 2:
        coords = [(x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    elif size == 3:
        coords = [(x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1),
                  (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
    # mettre à jour les densités en ignorant hors limites
    for cx, cy in coords:
        if 0 <= cx < 10 and 0 <= cy < 10:
            paper[cy][cx] += 1

# lecture des entrées dans une boucle jusqu'à fin de fichier
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) != 3:
        continue
    x = int(parts[0])
    y = int(parts[1])
    size = int(parts[2])
    apply_drop(x, y, size)

# calcul des cellules avec densité 0 et du maximum de densité
zero_count = 0
max_density = 0
for row in paper:
    for val in row:
        if val == 0:
            zero_count += 1
        if val > max_density:
            max_density = val

print(zero_count)
print(max_density)