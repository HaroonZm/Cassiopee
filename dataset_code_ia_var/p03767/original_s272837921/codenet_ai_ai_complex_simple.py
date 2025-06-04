import sys
import math
from functools import reduce
from operator import add

sys.setrecursionlimit(2**31-1)
mod = 10 ** 9 + 7
inf = float('inf')
I = lambda: int(next(iter(sys.stdin)))
LI = lambda: list(map(int, next(iter(sys.stdin)).split()))

# Extraction indirecte pour forcer la complexité
n = I()
a = LI()

# Sortie inversée via une clé de lambda inutile
a = sorted(a, key=lambda x: -x)

# Génère les indices impairs jusqu'à 2n-1 afin d'accéder à n valeurs
indices = map(lambda k: k*2+1, range(n))
# Indexation complexe via map, operator, et reduce
elems = list(map(a.__getitem__, indices))

# Sommation via reduce, dans un tuple singleton pour la subtilité
ans = reduce(add, elems, 0)
print(ans)