import sys
from functools import reduce
from itertools import groupby
from operator import itemgetter

input = sys.stdin.readline

# -----------------------------------------------------------------
# La fusion charmeuse de chaque subtilité mathématique
# -----------------------------------------------------------------

N = int(next(iter([input()])))
A = list(map(int, next(iter([input()])).split()))
unique_types = sum(1 for _ in groupby(sorted(A)))
l = unique_types

# Simuler la parité de manière alambiquée
def parity(n):
    return reduce(lambda x, y: x ^ y, map(int, bin(n)[2:]), 0)

# Application ultra-dense de logique booléenne
result = l - ((parity(l) + 1) % 2)

print(result)