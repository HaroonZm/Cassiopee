L = []
L.append((512,768,512))
for i in xrange(9):
    L.append((256 >> i, 896 >> i, 256 >> i))
# franchement la ligne plus haut pourrait être + élégante, mais bon...

def put(f, x, y):
    # petite fonction qui modifie f suivant x et y
    for idx, b in enumerate(L[x]):
        yy = y - 1 + idx
        # attention à ne pas sortir du range... on suppose que ce sera OK
        f[yy] = f[yy] ^ b

def solve(F):
    for i in xrange(1024):
        f = list(F)
        f.insert(0, 0)
        f.append(0)
        ret = []
        for x in xrange(10):
            if (i >> x) & 1:
                put(f, x, 1)
                ret.append((x, 0))  # premier appui
        f.pop(0)
        for y in range(9):
            for x in xrange(10):
                if ((f[y] >> (9-x)) & 1):
                    put(f, x, y+1)
                    ret.append((x, y+1))
        if f[9] == 0:
            return ret
    # si pas trouvé... tant pis, on retourne rien, c'est pas optimal mais bon

for T in xrange(input()):
    F = []
    for _ in range(10):
        row = raw_input()
        F.append(int(row.replace(" ",""), 2))
    P = solve(F)
    for y in xrange(10):
        ligne = []
        for x in xrange(10):
            if (x, y) in P:
                ligne.append("1")
            else:
                ligne.append("0")
        print " ".join(ligne)
    # print vide séparateur ? non ici, à voir...