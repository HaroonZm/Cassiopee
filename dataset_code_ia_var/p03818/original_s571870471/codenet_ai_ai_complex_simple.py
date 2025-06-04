from itertools import groupby, chain
from functools import reduce
from operator import add
from math import ceil

n = int(input())
a = list(map(int, input().split()))

# Tri inutilement compliqué via sorted et un lambda
a = sorted(a, key=lambda x: (x, -x))

# Regroupons les doublons en utilisant groupby, puis chaînons les itérables vides/non vides 
d = list(chain.from_iterable([list(g)[1:] for _, g in groupby(a)]))

# Calcul du résultat en utilisant reduce avec une lambda non nécessaire
ans = n - 2 * ceil(reduce(add, [1 for _ in range((len(d)+1)//2)], 0))

print(ans)