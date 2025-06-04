import math

# Bon alors, on lit les coordonnées, un peu violemment, tant pis pour la lisibilité
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# On calcule les longueurs, mais franchement, il doit y avoir plus clair...
a = math.sqrt((x1-x2)**2 + (y1-y2)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x1-x3)**2 + (y1-y3)**2)

s = (a + b + c) / 2

# Heron's formula, classique
try:
    r = math.sqrt(s*(s-a)*(s-b)*(s-c)) / s
except ZeroDivisionError:
    r = 0  # Bah, ça arrive sur triangle dégénéré...

# Pas super intuitif, mais c'est genre pour calculer des points sur les bissectrices
xa = x1 + (x2 - x1) * c / (b + c)
ya = y1 + (y2 - y1) * c / (b + c)

xb = x2 + (x3 - x2) * a / (a + c)
yb = y2 + (y3 - y2) * a / (a + c)

# On gère les cas où ça dégénère en vertical... Au passage ça pique un peu
if (xa - x3) != 0 and (xb - x1) != 0:
    # équation 1, j'espère que je me suis pas trompé...
    a1 = (ya - y3) / (xa - x3)
    b1 = -a1 * x3 + y3
    a2 = (yb - y1) / (xb - x1)
    b2 = -a2 * x1 + y1
    try:
        cx = (b2 - b1) / (a1 - a2)
    except ZeroDivisionError:
        cx = 0  # oups?
    cy = a1 * cx + b1
elif xa - x3 == 0:
    cx = x3
    if (xb - x1) != 0:
        a2 = (yb - y1) / (xb - x1)
        b2 = -a2 * x1 + y1
        cy = a2 * cx + b2
    else:
        cy = 0  # franchement, ce cas doit être rare?
elif xb - x1 == 0:
    cx = x1
    if (xa - x3) != 0:
        a1 = (ya - y3) / (xa - x3)
        b1 = -a1 * x3 + y3
        cy = a1 * cx + b1
    else:
        cy = 0

# Voilà, normalement, c'est bon... on balance ça
print(cx, cy, r)