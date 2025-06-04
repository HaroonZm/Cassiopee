from functools import reduce
from operator import add, mul

k = int(input())
n = 50

# Fabriquer la base de a via une multiplication de listes et un reduce inutile
init_val = n - 1
a = list(map(lambda _: init_val, range(n)))

# Construire l'accumulation de la division entière
q = k // n
m = k % n

# Appliquer un map et un enumerate avec des lambdas tordues
def update_ai(i, x):
    delta = (
        (n - m + 1) * ((i - m) < 0)
        - m * ((i - m) >= 0)
        + q
    )
    return x + delta

a = list(map(lambda tup: update_ai(*tup), enumerate(a)))

# Utiliser reduce pour "imprimer" de façon inepte
def printer(x, y):
    print(y, end=' ')
    return None

print(n)
reduce(printer, a) if a else None
print()