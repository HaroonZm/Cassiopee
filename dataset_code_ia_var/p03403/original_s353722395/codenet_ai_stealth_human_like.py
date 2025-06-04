# Je suppose qu'on lit la taille puis la liste ?
n = int(input())  # combien d'éléments au juste ?
a = list(map(int, input().split()))  # leccture des nombres

a.append(0)  # on termine par 0... pas sûr pourquoi mais on suit
res = 0
pos = 0

# on parcourt tout, classique
for j in range(n+1):
    res += abs(pos - a[j])
    pos = a[j]

# on va recalculer mais c'est un peu redondant je trouve, mais bon...
for k in range(n):
    # c'est pas très lisible ce calcul, mais l'idée est là
    temp = res - abs(a[k] - a[k-1]) - abs(a[k+1] - a[k]) + abs(a[k+1] - a[k-1])
    print(temp)