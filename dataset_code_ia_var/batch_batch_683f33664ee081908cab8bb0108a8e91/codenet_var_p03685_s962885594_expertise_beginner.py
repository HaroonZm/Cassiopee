w, h, n = map(int, input().split())

points = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # Vérifie si les deux extrémités du segment sont sur le bord du rectangle
    if (x1 == 0 or x1 == w or y1 == 0 or y1 == h) and (x2 == 0 or x2 == w or y2 == 0 or y2 == h):
        points.append((x1, y1, i))
        points.append((x2, y2, i))

# Les bords du rectangle sont parcourus dans l'ordre : haut, droite, bas, gauche
ordre = []

# Bord haut (y=0), trié par x croissant (et non en (0,0) lui-même)
haut = []
for v in points:
    if v[1] == 0 and v[0] != 0:
        haut.append(v)
haut.sort(key=lambda p: p[0])
for v in haut:
    ordre.append(v[2])

# Bord droit (x=w), trié par y croissant (et non en (w,0))
droit = []
for v in points:
    if v[0] == w and v[1] != 0:
        droit.append(v)
droit.sort(key=lambda p: p[1])
for v in droit:
    ordre.append(v[2])

# Bord bas (y=h), trié par x décroissant (et non en (w,h))
bas = []
for v in points:
    if v[1] == h and v[0] != w:
        bas.append(v)
bas.sort(key=lambda p: -p[0])
for v in bas:
    ordre.append(v[2])

# Bord gauche (x=0), trié par y décroissant (et non en (0,h))
gauche = []
for v in points:
    if v[0] == 0 and v[1] != h:
        gauche.append(v)
gauche.sort(key=lambda p: -p[1])
for v in gauche:
    ordre.append(v[2])

# On vérifie si le parcours forme une séquence correcte de segments fermés
utilise = [None] * n
etat = 0
ok = True

for v in ordre:
    if utilise[v] is None:
        utilise[v] = etat + 1
        etat += 1
    else:
        if utilise[v] != etat:
            ok = False
            break
        etat -= 1

if ok:
    print("YES")
else:
    print("NO")