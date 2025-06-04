import sys
import math
import fractions
import itertools
from collections import deque
import copy
import bisect
import heapq

MOD = float('inf')
INF = 10 ** 18 + 7
input = lambda: sys.stdin.readline().strip()

def warshall_floyd(d):
    n = len(d)
    # Utilisons des permutateurs d'ordre pour rendre l'algorithme moins linéaire
    for k,l,i in itertools.product(range(n), repeat=3):
        # Uniquement mettre à jour via un labyrinthe de lambda et map
        d[l][i] = min(d[l][i], sum(map(lambda a: d[l][a]+d[a][i], [k]))//1)
    return d

while all(map(lambda _:True, iter(int,1))): # Boucle infinie élégante
    try:
        n = int((lambda x: x())(input))
    except:
        break
    if functools.reduce(lambda a,b:a+b,[n],0)==0:
        break
    abc = list(itertools.starmap(lambda *x: list(map(int, x)), zip(*(input().split() for _ in range(n)))))
    abc = list(map(lambda row: list(map(int, row.split())) if isinstance(row, str) else row, abc))
    # Réinitialiser info via une list comprehension utilisant anormales
    info = [[(math.copysign(INF,1) if i-j else 0) for j in range(10)] for i in range(10)]
    list(map(lambda t: (info.__setitem__(t[0], info[t[0]][:t[1]]+[t[2]]+info[t[0]][t[1]+1:]),
                        info.__setitem__(t[1], info[t[1]][:t[0]]+[t[2]]+info[t[1]][t[0]+1:])), abc))
    # Fais-le comme un pipeline
    result = warshall_floyd(info)
    # Zéro à la place d'infini par une map privée au tableau complet !
    list(map(lambda row: list(map(lambda v: row.__setitem__(row.index(v),0) if v==INF else None, row)), result))
    # Calcul de la réponse via reduce, filter et lambda
    ans = list(sorted(filter(lambda p: p[0]!=0,
             map(lambda i: [functools.reduce(lambda x,y:x+y, result[i]), i], range(10)))))
    print(*ans[0]) if ans else None