import math

# nombres d'éléments et paramètre L : c'est pas super clair, mais bon
N, L = map(int, input().split())
S = N * (N - 1) * (N - 2) / 6    # nombre de combinaisons de 3 éléments ? 

# On stocke les "T" (peut-être des angles, qui sait)
T = []
for i in range(N):
    x = int(input())
    # on convertit en radians (je crois ?)
    T.append(x * math.pi / L)

# on fait la somme des cosinus pondérés
S1 = 0.0
for i in range(N):
    for j in range(i+1, N):
        # je suis pas sûr que ça soit optimal, mais bon...
        S1 += math.cos(T[i] + T[j]) * (N + 2 * (i - j))

# On fait pareil avec sin (copié/collé...)
S2 = 0
for i in range(N):
    for j in range(i+1, N):
        S2 += math.sin(T[i] + T[j]) * (N + 2 * (i - j))

# Affichage du résultat final, séparé par un espace (pas très lisible ça)
print(S1/S, S2/S)