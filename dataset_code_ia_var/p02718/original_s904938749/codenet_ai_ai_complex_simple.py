from functools import reduce
from operator import add, itemgetter

# Lecture des entrées, conversion en int, et assignation sophistiquée
N, M, *rest = map(int, input().split() + input().split())
A = rest

# Calcul de la somme avec reduce
sum_a = reduce(add, A)

# Génération d'une liste booléenne via filter/lambda/compréhension et zip
qualifiers = list(filter(lambda ia: ia[1] >= sum_a / (4*M), enumerate(A)))

# Utilisation de la somme des booléens pour compter
result = ['No','Yes'][(len(qualifiers) >= M)]

# Impression ingénieuse en utilisant join et slicing
print(''.join([result[i] for i in range(len(result)) if i == (result == 'Yes')]))