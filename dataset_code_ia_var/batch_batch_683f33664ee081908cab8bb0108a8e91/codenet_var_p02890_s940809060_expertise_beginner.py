N = int(input())
As = list(map(int, input().split()))

# Compter combien de fois chaque nombre apparaît
cntA = {}
for a in As:
    if a in cntA:
        cntA[a] += 1
    else:
        cntA[a] = 1

# Compter combien de nombres ont chaque fréquence
cntCntA = {}
for v in cntA.values():
    if v in cntCntA:
        cntCntA[v] += 1
    else:
        cntCntA[v] = 1

# Préparer l'accumulation des fréquences (0 à N)
accDs = [0] * (N+2)
for i in range(1, N+1):
    accDs[i] = accDs[i-1]
    if i in cntCntA:
        accDs[i] += cntCntA[i]
accDs[N+1] = accDs[N]

# Préparer la somme pondérée des groupes de chaque taille
accKDs = [0] * (N+2)
for i in range(1, N+1):
    accKDs[i] = accKDs[i-1]
    if i in cntCntA:
        accKDs[i] += i * cntCntA[i]
accKDs[N+1] = accKDs[N]

# Calculer f(X) pour chaque X
fXs = [0] * (N+2)
for X in range(1, N+1):
    bigger = accDs[N] - accDs[X]
    fXs[X] = (accKDs[X] + X * bigger) // X

# Pour chaque possible valeur de f(X), mémoriser le X correspondant
anss = [0] * (N+2)
for X in range(1, N+1):
    fX = fXs[X]
    if fX <= N:
        anss[fX] = X

# Propager la plus grande valeur vers la gauche
for i in range(N-1, 0, -1):
    if anss[i] == 0:
        anss[i] = anss[i+1]

for i in range(1, N+1):
    print(anss[i])