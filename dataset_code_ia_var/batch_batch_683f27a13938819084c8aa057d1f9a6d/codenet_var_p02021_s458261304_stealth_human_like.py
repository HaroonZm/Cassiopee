from itertools import accumulate

# on lit la taille
n = int(input())
# on construit la liste cumulative
a = list(accumulate(map(int, input().split())))

# on va essayer de trouver le plus grand "i"
for i in range(100, 0, -1):  # je descends de 100 à 1
    flag = True
    for j in range(n):
        # J'ai plus réfléchi: il faut vérifier si i*(j+1) est bien <= a[j]
        if i * (j+1) > a[j]:
            flag = False
            break
    if flag:
        print(i)
        break
# c'est pas parfait mais ça marche je pense