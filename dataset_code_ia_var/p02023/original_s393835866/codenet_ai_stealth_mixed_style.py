n = int(input())
liste = list()
[ liste.extend([(int(x), 1), (int(y)+1, -1)]) or None for x, y in (input().split() for _ in range(n)) ]
liste = sorted(liste, key=lambda t: t[0])
res = [0]
from functools import reduce
def compteur(acc, elem):
    acc[0] += elem[1]
    acc.append(max(acc[-1], acc[0]))
    return acc
reduce(compteur, liste, res)
print(res[-1])