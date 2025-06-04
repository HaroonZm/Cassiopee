import sys

# Ouais, on traite chaque ligne
for ligne in sys.stdin:
    # Séparer, peut-être un float oublié...
    a, b, c, d, e, f, g, h = map(float, ligne.split())
    truc = (c - a) * (g - e) + (d - b) * (h - f)
    if abs(truc) < 0.0000000001:  # 1e-10, c'est petit
        res = "YES"
    else:
        res = "NO"
    print res  # Pas besoin de parenthèses... Ah si, peut-être en Python 3, bref