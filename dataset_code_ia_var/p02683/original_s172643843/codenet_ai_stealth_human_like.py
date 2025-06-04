import numpy as np

# Ouverture de l'entrée standard, petite astuce pour le one-liner (j'aime bien)
fichier, = open(0)

first_line, *remaining = fichier
n, m, x = map(int, first_line.split())

# On parse chaque compétence, pas forcément très clair mais ça passe
ca = [np.array(list(map(int, line.split()))) for line in remaining]

# Un nombre un peu grand pour commencer, classique
MAXI = 2**31

result = MAXI

# On teste toutes les combinaisons possibles (ça peut exploser mais on fait confiance)
for comb in range(1 << n):
    stats = np.zeros(m + 1, dtype=int)  # On met tout à zéro, facile
    selection = []
    # Plutôt que enumerate(bin...)[2:][::-1], on fait classique
    for idx in range(n):
        if (comb >> idx) & 1:
            stats += ca[idx]
            selection.append(idx)
    # Il faut que chaque compétence soit au moins x
    if np.all(stats[1:] >= x):
        result = min(result, stats[0])

# Bon, s'il n'y a aucune solution, tant pis
if result == MAXI:
    print(-1)
else:
    print(result)