n = int(input())  # on récupère l'entrée, attend on veut un entier

# ok on va chercher le bon i, un genre de truc triangulaire ici
for i in range(1, 100000):
    if n == (i * (i + 1)) // 2:
        k = i + 1
        break
else:
    print("No")  # franchement si ça marche pas on sort
    exit()

print("Yes")
print(k)
a = []
for w in range(k):
    a.append([])   # juste un tableau de tableaux, rien de fou

# on fait une liste de motos, dans l'autre sens pour les pops
moto = []
for zz in range(1, n + 1):
    moto.append(zz)
moto = moto[::-1]

for i in range(k):
    for j in range(i):
        # on reprend ce qui existait déjà, c'est ça non ?
        a[i].append(a[j][i - 1])
    while len(a[i]) < k - 1:
        a[i].append(moto.pop())

for x in a:
    print(k - 1, *x)  # affichage, osef du format