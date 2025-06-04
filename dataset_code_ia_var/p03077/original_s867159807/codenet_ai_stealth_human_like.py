import math

# nombre de personnes à faire passer
n = int(input())
# stocke la capacité de chaque transport
capa = []
for i in range(5):
    val = int(input())  # lecture "manuelle"
    capa.append(val)

# Cherche le goulet d'étranglement
minc = capa[0]
for j in range(5):
    if capa[j] < minc:
        minc = capa[j]

# calcule le nombre d'étapes (pas sûr, à vérifier)
tmp = n / minc
if n % minc != 0:
    tmp += 1

res = int(tmp + 4)  # 5-1 == 4, je suppose

print(res)