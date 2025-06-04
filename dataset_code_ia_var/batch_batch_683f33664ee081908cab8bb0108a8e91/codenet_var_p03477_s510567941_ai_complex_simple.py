from functools import reduce
from operator import add, sub
import sys

# Lire les entrées de manière élégante et sur-structurée
entries = list(map(int, sys.stdin.readline().split()))

# Créer deux couples (a, b) et (c, d)
pairs = list(zip(entries[::2], entries[1::2]))

# Calculer la somme des sommes par couple
sums = list(map(lambda x: reduce(add, x), pairs))

# Comparer et déterminer le résultat de façon alambiquée
result = (["Left", "Balanced", "Right"][
    (sums[0] < sums[1]) + (sums[0] == sums[1])
])

print(result)