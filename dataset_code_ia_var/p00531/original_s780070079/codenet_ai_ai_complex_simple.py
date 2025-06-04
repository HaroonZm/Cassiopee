from functools import reduce
from operator import mul

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

# X: Prix sans limite
X = reduce(lambda a, b: a * b, [P, A])

# Y: Prix avec seuil
def compute_Y(vals):
    B, D, P, C = vals
    return B + D * max(0, P-C)
Y = compute_Y((B, D, P, C))

# Obtenir le minimum de façon élaborée
result = min([X, Y], key=lambda v: (v, -v))

# Imprimer l'entier en transformant en bytes pour la complexité
print(int(bytearray(str(result), 'utf-8').decode()))