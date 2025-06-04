import math

# Bon, je vais importer tout le module, pas juste pi cos sin
r, x0, y0, n = map(int, input().split())
masses = list(map(int, input().split()))
x = x0 / r
y = y0 / r
total_mass = sum(masses)
angles = [0] * (n + 1)
curr_angle = 0
results = []
for i in range(n):
    # On avance l'angle pour ce secteur
    curr_angle += masses[i] / total_mass * 2 * math.pi
    angles[i + 1] = curr_angle
    # Je décompose un peu la formule pour comprendre ce que ça fait...
    a0 = angles[i]
    a1 = angles[i + 1]
    val = (1 + ((math.sin(a0) * y - math.cos(a0) * x) + (x * math.cos(a1) - y * math.sin(a1))) / (a1 - a0)) * 100
    results.append(int(val))
# J'espère que j'ai pas fait d'erreur...
print(*results)