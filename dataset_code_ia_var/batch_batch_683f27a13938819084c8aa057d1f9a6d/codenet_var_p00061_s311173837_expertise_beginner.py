import sys

# Lecture des lignes et création de la liste L
L = []
while True:
    line = sys.stdin.readline()
    if line.startswith('0,0'):
        break
    s = line.strip().split(',')
    L.append((int(s[0]), int(s[1])))

# Tri de la liste L selon le point (de manière décroissante)
def get_point(t):
    return t[1]

L.sort(key=get_point, reverse=True)

# Traitement des requêtes
for line in sys.stdin:
    n = int(line.strip())
    order = 0
    prev_point = None
    for id_, point in L:
        if prev_point != point:
            order += 1
            prev_point = point
        if n == id_:
            break
    print(order)