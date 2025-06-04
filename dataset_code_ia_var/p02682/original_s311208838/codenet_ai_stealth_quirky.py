# Entrée compacte et initialisation étrange
nugz = [*map(int, input().split())]
x = [0]
for _ in [0]:  # Forcer le bloc en utilisant un singleton inutile
    z, y, w, v = nugz  # aliasing personnalisé
    if v > z + y:
        x[0] += z
        v -= (z + y)
        # Utilisation de l'ordre logique peu courant avec ternaire inversé
        output = (x[0] - v) if v <= w else (x[0] - w)
        print(output)
    else:
        # Cascade de conditions avec arithmétique booléenne micro-optimisée
        print(z * (v >= z) + v * (v < z))