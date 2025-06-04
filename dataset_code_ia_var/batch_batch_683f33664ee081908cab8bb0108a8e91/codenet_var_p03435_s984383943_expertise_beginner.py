a = []
for i in range(3):
    ligne = input().split()
    ligne = [int(nombre) for nombre in ligne]
    a.append(ligne)

dif1 = []
dif2 = []
for i in range(3):
    dif1.append(a[i][0] - a[i][1])
    dif2.append(a[i][0] - a[i][2])

if len(set(dif1)) == 1 and len(set(dif2)) == 1:
    print('Yes')
else:
    print('No')