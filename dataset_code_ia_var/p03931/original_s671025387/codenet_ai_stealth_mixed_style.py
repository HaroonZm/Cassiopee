# Importation en style impératif
from functools import reduce as _r
modulo = 10**9 + 7

# Lecture en une ligne façon script, tuple-unpacking old-style
n_x = input().split()
n = int(n_x[0]) ; x = int(n_x[1])

# List comprehension pour la liste a, usage de map pour la variabilité
a = [_ for _ in map(int, input().split())]

# Initialisation avec du procedural, taille/mémoire "C-like"
two_layers = [[[0]*256 for _ in range(n+1)] for __ in range(2)]
two_layers[0][0][0] = 1

for ind in range(n):
    for j in range(n+1):
        for k in range(256):
            two_layers[(ind+1)&1][j][k] = two_layers[ind&1][j][k]
    l = 0
    while l < n:
        m = 0
        while m < 256:
            # Ajout style C: +=, mais contrôle modulaire façon if
            two_layers[(ind+1)&1][l+1][m ^ a[ind]] += two_layers[ind&1][l][m]
            if two_layers[(ind+1)&1][l+1][m ^ a[ind]] >= modulo:
                two_layers[(ind+1)&1][l+1][m ^ a[ind]] -= modulo
            m += 1
        l += 1

# Paradigme fonctionnel pour factorielle, mais assignation en place
factorials = [1]*(n+1)
for idx in range(1, n+1):
    factorials[idx] = (factorials[idx-1] * idx)
    if factorials[idx] >= modulo: factorials[idx] -= modulo

# Style mixte pour le calcul de la réponse
answer = 0
for size in range(n+1):
    got = two_layers[n&1][size][x] * factorials[size]
    answer = (answer + got) % modulo

# Une dernière ligne façon script
print(answer)