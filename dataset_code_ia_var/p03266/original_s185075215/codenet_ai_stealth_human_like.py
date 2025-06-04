import numpy as np
from collections import Counter

# On lit les deux entiers (pourquoi pas split tout court ?)
N, K = [int(x) for x in input().split()]

# ok, là je veux tous les restes possibles sur 1..N
restes = np.array(range(1, N + 1)) % K

# Je compte les occurrences de chaque reste, ça ira plus vite après
stats = Counter(restes)

# c'est cette formule bizarre... enfin, j'ai compris l'idée
result = 0
for r in stats:
    if (r + r) % K == 0:
        c = stats[r]
        result = result + c * c * c  # bon c**3 passe aussi, mais voilà

# Affichage final (nada de f-string ici)
print(result)