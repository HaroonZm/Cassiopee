import sys
input = sys.stdin.readline
print = lambda *args, **kwargs: __import__('builtins').print(*args, **kwargs, flush=True)

N = int(input())

# Nous savons que la distance entre les indices originaux est |i-j|.
# Nous savons que "1番目に出来たての今川焼き" signifie le numéro de cuisson.
# On doit déterminer pour chaque position (gauche à droite) quel est son rang de production.
# Principe : On requête la distance entre le 1er rang de production et la 2ème rang de production, etc.
# On veut reconstituer la permutation p où p[i] = rang de cuisson de l'ième gâteau sur la bande.

# Stratégie : On sait que la distance entre le gâteau à rang 1 et celui à rang 2 est 1
# On peut interroger paire par paire pour retrouver leur ordre exact.
# Mais on ne connaît pas l'ordre sur la bande, donc on doit retrouver une correspondance entre positions sur la bande (1..N) et rang de cuisson (1..N).

# Utilisons la distance entre le gâteau rang 1 et tout autre gâteau rang i (i=2..N)
# Ces distances correspondent à la distance en mètres entre les centres sur la bande.
# Donc la position sur la bande du gâteau rang i vaut position du gâteau rang 1 plus la distance donnée (ou moins)

# Puisqu'on ne connait pas la position sur la bande du gâteau rang 1, on peut supposer qu'il est en position k.
# On peut fixer rang 1 à position pos, puis tous les autres ont des positions pos + distance (ou pos - distance). 
# Si on suppose que rang 1 est sur la position x, alors pos de rang i = x + d(i,1) ou x - d(i,1)

# On peut choisir arbitrairement la plus petite position = 1, et calculer les autres en conséquence.

# Donc, faisons une requête entre rang 1 et tout autre rang i (2..N)
# Nous obtenons les distances d_i = distance entre rang 1 et rang i

distances = [0]*N
for i in range(2, N+1):
    print("?", 1, i)
    d = int(input())
    distances[i-1] = d

# On peut trouver la position minimale pour que les positions soient dans 1..N

# Les positions sur la bande pour les rangs 1..N sont pos[i] = pos_1 + sign * distances[i]
# sign peut être soit +1 soit -1 suivant le sens de la bande.
# Deux possibilités pour la solution finale, donc on peut choisir le sens.

# Les positions sont donc soit distances par rapport à pos_1 au minimum.
# Nous savons que les positions sont entiers distincts dans [1..N] car ils occupent les positions sur la bande.

# Calculons les positions avec pos_1 = val, sign = 1:
# pos[i] = val + distances[i]
# pos[1] = val

# Il faut que min(pos) = 1 et max(pos) = N or pos_1=val, donc min(pos) = val + min(distances), max(pos) = val + max(distances)
# Pour min pos = 1, val = 1 - min(distances)
# On calcule pos_i = 1 - min(distances) + distances[i]

min_d = min(distances)
max_d = max(distances)

def build_positions(base):
    pos = [0]*N
    for i in range(N):
        pos[i] = base + distances[i]
    return pos

pos1 = build_positions(1 - min_d)
# pos dans pos1 doivent être unique et dans [1..N]
if sorted(pos1) == list(range(1, N+1)):
    # pos1 correspond à permutation rang de cuisson -> position
    # Nous avons besoin de position -> rang de cuisson (inverse)
    ans = [0]*N
    for r in range(1, N+1):
        ans[pos1[r-1]-1] = r
    print("!", *ans)
else:
    # sign = -1
    def build_positions_neg(base):
        pos = [0]*N
        for i in range(N):
            pos[i] = base - distances[i]
        return pos
    pos2 = build_positions_neg(max_d + 1)
    if sorted(pos2) == list(range(1,N+1)):
        ans = [0]*N
        for r in range(1, N+1):
            ans[pos2[r-1]-1] = r
        print("!", *ans)
    else:
        # Dans le cas improbable, on donne la solution en inversant
        # Improbable mais sécuritaire
        ans = [0]*N
        for i in range(N):
            ans[i] = i+1
        print("!", *ans)