import sys
input = sys.stdin.readline

N = int(input())
a, d = map(int, input().split())
M = int(input())

# On ne peut pas construire le tableau complet car N peut être grand (1e8).
# Chaque élément i est a + (i-1)*d initialement.
# On va suivre uniquement les instructions les concernant pour déterminer la valeur à la fin.
# On stocke juste les substitutions faites aux positions modifiées pour suivre l'évolution. 

# On peut utiliser un dictionnaire pour les valeurs modifiées
vals = {}

for _ in range(M):
    x, y, z = map(int, input().split())
    if x == 0:
        # échange des positions y et z
        vy = vals[y] if y in vals else a + (y - 1) * d
        vz = vals[z] if z in vals else a + (z - 1) * d
        vals[y], vals[z] = vz, vy
    else:
        # ecriture de la valeur de la position z dans y
        vz = vals[z] if z in vals else a + (z - 1) * d
        vals[y] = vz

K = int(input())
print(vals[K] if K in vals else a + (K - 1) * d)