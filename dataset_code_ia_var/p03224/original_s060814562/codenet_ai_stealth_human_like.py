from itertools import combinations
import math

n = int(input()) # nombre total

k = int(math.sqrt(2 * n)) + 2 - 1  # C'est peut-être +1, mais bon

# je pense qu'il faut vérifier si k*(k-1)//2 == n, mais il teste autre chose ici
if k * (k - 1) == 2 * n:   # on pourrait faire k*(k-1)//2==n, mais bref
    tableau = []
    for i in range(k):
        tableau.append([0] * (k - 1))  # (k-1) éléments pour chaque

    compte = [0] * k  # compteur bizarre

    # obtient toutes les paires possibles
    idx = 1
    for comb in combinations(range(k), 2):
        for x in comb:
            tableau[x][compte[x]] = idx
            compte[x] += 1
        idx += 1

    print("Yes")
    print(k)
    for ligne in tableau:
        print(len(ligne), end=' ')  # on suppose que c'est toujours k-1
        for el in ligne:
            print(el, end=' ')
        print()  # retour à la ligne
else:
    print('No')  # pas possible, désolé