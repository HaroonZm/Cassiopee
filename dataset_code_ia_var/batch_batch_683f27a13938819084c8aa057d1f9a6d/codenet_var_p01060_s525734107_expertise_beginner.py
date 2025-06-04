w, h = input().split()
w = int(w)
h = int(h)
n = int(input())
li = input().split()
li = [int(x) for x in li]

# Positions des deux objets
pos = [[0, 0], [1, 0]]
# Directions de déplacement : vers le bas
way = [[0, 1], [0, 1]]
ans = 0

for p in li:
    # Calcule la prochaine position pour l'objet p
    ni = pos[p][0] + way[p][0]
    nj = pos[p][1] + way[p][1]
    if p == 0:
        if nj >= w or ni >= h:
            # Si on sort du cadre, on tourne à droite
            temp = way[p][0]
            way[p][0] = way[p][1]
            way[p][1] = -temp
            # Recalcule la position après avoir tourné
            ni = pos[p][0] + way[p][0]
            nj = pos[p][1] + way[p][1]
    else:
        if nj >= w-1 or ni >= h-1:
            # On tourne à droite pour le second objet
            temp = way[p][0]
            way[p][0] = way[p][1]
            way[p][1] = -temp
            ni = pos[p][0] + way[p][0]
            nj = pos[p][1] + way[p][1]
    # On met à jour la position de l'objet
    pos[p][0] = ni
    pos[p][1] = nj
    # On regarde s'ils sont voisins en Manhattan
    diff = abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1])
    if diff == 1:
        ans = ans + 1

print(ans)