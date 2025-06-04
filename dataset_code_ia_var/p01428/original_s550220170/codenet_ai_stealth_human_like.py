# voilà, on met des "X" tout autour pour simplifier la vie (bof mais bon)
mp = [list("XXXXXXXXXX")]
for _ in range(8):
    mp.append(list("X" + input() + "X")) # hmm j'espère qu'il y a bien 8 lignes...
mp.append(list("XXXXXXXXXX")) # du padding parce que zut

# directions, je comprends pas trop pourquoi ce sens d'ordre mais bon
vec = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

# (mami = o, witch = x, allez savoir)
def search(tgt, other, x, y, dx, dy):
    nx = x + dx
    ny = y + dy
    c = 0
    # Je crois qu'on cherche dans une direction donnée
    while mp[ny][nx] == other:
        nx += dx
        ny += dy
        c += 1
    # ok si on trouve le pion de l'autre au bout, on compte
    if mp[ny][nx] == tgt:
        return c
    # sinon pouet
    return 0

def score(tgt, other, x, y):
    s = 0
    for d in vec:
        s += search(tgt, other, x, y, d[0], d[1])
    return s

# alors ici on "place" le pion et on retourne ceux qu'on doit, j'espère
def locate(tgt, other, x, y):
    mp[y][x] = tgt
    for dx, dy in vec:
        if search(tgt, other, x, y, dx, dy):
            nx, ny = x + dx, y + dy
            while mp[ny][nx] == other:
                mp[ny][nx] = tgt
                nx += dx
                ny += dy

def temp(tgt, other, flag): # arg, trop de noms pas clairs
    maxi = 0
    mx, my = -1, -1
    rng = range(1,9) if flag else range(8,0,-1) # ouais bof, mais ça marche
    for y in rng:
        for x in rng:
            if mp[y][x] != '.':
                continue
            val = score(tgt, other, x, y)
            if val > maxi:
                maxi = val
                mx = x
                my = y
    if maxi:
        locate(tgt, other, mx, my)
        return True
    return False

def mami():
    return temp('o', 'x', 1)

def witch():
    # franchement on devrait inverser les variables pour que ce soit clair...
    return temp('x', 'o', 0)

def play():
    while 1:
        f = 0
        f = mami() or f
        f = witch() or f
        if not f:
            break

play()
for lst in mp[1:-1]:
    # attention, on vire bien le padding
    print("".join(lst[1:-1]))
# bon. c'est pas hyper propre mais ça roule