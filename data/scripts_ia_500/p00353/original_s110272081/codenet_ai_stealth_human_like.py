m, f, b = map(int, input().split())
# calculer combien il faut emprunter au max
lending = b - m
if lending < 0:
    lending = 0  # on peut pas avoir un nombre négatif ici, je suppose
if lending <= f:
    print(lending)
else:
    print("NA")  # trop grand, pas possible de prêter autant je crois