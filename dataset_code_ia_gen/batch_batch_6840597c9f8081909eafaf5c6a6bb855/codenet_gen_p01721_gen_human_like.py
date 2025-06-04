w, h, v, t, x, y, p, q = map(int, input().split())

max_dist = v * t

count = 0

# On considère les images réfléchies du point (p, q)
# dans un nombre suffisant de "chambres" virtuelles
# pour couvrir la distance max_dist dans toutes les directions.
# Le déplacement total possible est max_dist, donc on calcule
# combien de répétitions sont nécessaires en x et y.

max_rep_x = max_dist // w + 2
max_rep_y = max_dist // h + 2

def reflect(coord, length, i):
    # Calcule la position réfléchie en fonction de i (image virtuelle)
    # i pair : pas de réflexion, i impair : réflexion
    if i % 2 == 0:
        return i * length + coord
    else:
        return (i + 1) * length - coord

for i in range(int(-max_rep_x), int(max_rep_x) + 1):
    for j in range(int(-max_rep_y), int(max_rep_y) + 1):
        # position réfléchie du point (p, q)
        img_x = reflect(p, w, i)
        img_y = reflect(q, h, j)

        dx = img_x - x
        dy = img_y - y
        dist = (dx * dx + dy * dy) ** 0.5

        # On compte les coups si dist <= max_dist et dist != 0 (pas la source elle-même)
        if dist <= max_dist and dist > 1e-15:
            count += 1

print(count)