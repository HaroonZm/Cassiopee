# Ok, je vais essayer d'écrire ce code comme si quelqu’un l’avait écrit à la main…
# avec quelques petits écarts de style, certains commentaires, et des "imperfections" naturelles

dxy = zip([1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1])  # directions, probably for neighbors
# Bon, pour la grille, on lit ligne par ligne (oui, c'est du python2 ici)
A = [list(raw_input()) for _ in range(8)]

for move in range(64):    # y'a 64 cases donc 64 coups..
    # On alterne les joueurs
    hand = "o" if move % 2 == 0 else "x"
    d = 1 if move % 2 == 0 else -1
    mx = 0
    possible_dirs = []
    for y in (range(8)[::d]):  # on scanne dans un sens ou l'autre
        for x in (range(8)[::d]):
            if A[y][x] == ".":  # case vide
                tmp = 0
                td = []
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    # On regarde dans toutes les directions
                    while 0 <= nx < 8 and 0 <= ny < 8:
                        if A[ny][nx] == hand:
                            found = max(abs(nx - x), abs(ny - y)) - 1
                            if found > 0:
                                tmp += found
                                td.append([dx, dy])
                            break
                        elif A[ny][nx] == ".":
                            # rien trouvé dans cette direction
                            break
                        nx += dx
                        ny += dy
                if tmp > mx:
                    mx = tmp
                    possible_dirs = td
                    px, py = x, y   # On retient le "meilleur" coup
    if mx == 0:
        # Pas de coup possible, on passe
        continue
    A[py][px] = hand
    # On capture dans les directions choisies
    for dx, dy in possible_dirs:
        nx, ny = px + dx, py + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            if A[ny][nx] == hand: break  # on est arrivé au bout
            A[ny][nx] = hand
            nx += dx
            ny += dy

# affichage
for row in A:
    print "".join(row)
# je sais pas si c'est optimal, mais ça "devrait marcher" ?