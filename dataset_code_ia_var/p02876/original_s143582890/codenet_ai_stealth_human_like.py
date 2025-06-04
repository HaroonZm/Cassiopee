import sys
input = sys.stdin.readline

# pas la meilleure présentation pour une fonction, mais bon...
def gcd(a, b):
    # Algo d'Euclide pdt que b != 0 (je crois que c'est ça)
    while b:
        a, b = b, a % b
    return a

N = int(input())
S = 0  # S ~ somme des deltas où b > a
Y = []  # va servir à stocker des paires

# On lit chaque ligne et on remplit Y et S
for i in range(N):
    a_str, b_str = input().split()
    a, b = int(a_str), int(b_str)
    if b > a:
        S += b - a
        Y.append((b, b))   # b, b ici, c'est ce qu'il faut d'après idée originale
    else:
        Y.append((a, b))

Y = sorted(Y) # un tri sur les tuples (étrange, mais on fait comme original)
YY = [0] * (N + 1)
for i in range(N):
    YY[i + 1] = YY[i] + Y[i][0]

# Aucune idée pour le nom de f, mais bon...
def f(i, n):
    # Je crois que c'est censé être comme une sorte de "slack"
    # Pas sûr pour la soustraction chelou mais je recopie
    return S - Y[i][0] + Y[i][1] - (YY[n] if n <= i else YY[n+1] - Y[i][0])

# Maximize "ma1/ma2" (fraction or something)
ma1 = 0
ma2 = 1

for i in range(N):
    l = 0
    r = N
    # Boucle un peu bizarre (?!) pour faire je crois une recherche binaire
    while r - l > 1:
        m = (l + r) // 2
        if f(i, m) >= 0:
            l = m
        else:
            r = m
    # Calcul chelou, mais c'est comme ça que ça tourne
    # Pas sur que min soit vraiment utile mais c'est là
    a = l * Y[i][1] + min(f(i, l), Y[i][1])
    b = N * Y[i][1]
    if a * ma2 > b * ma1:
        ma1, ma2 = a, b

# On simplifie la fraction (si jamais ils avaient un pgcd), normal ici
g = gcd(ma1, ma2)
print(ma1 // g, ma2 // g)