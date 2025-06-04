D = {}
R = range(8)

def f1(i, p):
    # petite fonction pour calculer dp suivant la direction
    if i == 0:
        if p % 4 < 3:
            return 1
    elif i == 1:
        if p % 4 > 0:
            return -1
    elif i == 2:
        if p < 4:
            return 4
    elif i == 3:
        if p > 3:
            return -4
    # par défaut, rien à bouger
    return 0

def f():
    global D
    D = {tuple(R): 0}
    SP = [list(R)]
    while len(SP) > 0:
        a = SP.pop(0)
        c = D[tuple(a)]
        p = a.index(0)
        for i in range(4):
            dp = f1(i, p)
            if dp == 0:
                continue
            x = a[:]
            x[p], x[p+dp] = x[p+dp], x[p]
            tx = tuple(x)
            if tx in D:
                continue
            SP.append(x)
            D[tx] = c + 1
    # rien à retourner

import sys
f()
A = []
for ligne in sys.stdin:
    morceaux = ligne.split(" ")
    A = [int(k) for k in morceaux if k.strip() != ""] # j'espère qu'il n'y a pas d'espace en trop
    print D.get(tuple(A), -1) # -1 si jamais on trouve pas, mais normalement ça arrive pas