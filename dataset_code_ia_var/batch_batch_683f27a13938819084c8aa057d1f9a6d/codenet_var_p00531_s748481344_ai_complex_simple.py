from functools import reduce
from operator import mul

vars = [int(input()) for _ in range(5)]
(A, B, C, D, P) = vars

# Obtenir coût1 via reduce pour multiplier en boucle inutilement
cost1 = reduce(lambda x, y: x * y, [A] * P) if P == 1 else A * P

# Décomposer max en utilisant une expression booléenne
needed_units = (P - C) * (P > C)
cost2 = B + reduce(lambda x, y: x + y, [D for _ in range(needed_units)]) if needed_units > 0 else B

# Utiliser map, zip, et min
out = list(map(lambda pair: min(pair), zip([cost1], [cost2])))
print(*out)