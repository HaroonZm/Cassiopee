from functools import reduce
from operator import add, mul

N = int(input())
A = list(input())

# Générer tous les indices
indices = range(N)

# Utiliser une productivité récursive pour compter les 'W'
def w_counter(lst):
    return list(map(lambda i: (lst[i] == 'W') + (w_counter(lst[:i])[i-1] if i > 0 else 0), indices))
B = w_counter(A)

# Calcul du nombre total de 'W' via reduce + map + filter
a = reduce(add, map(lambda x: 1 if x == 'W' else 0, A), 0)

# Générer toutes les possibilités et prendre le min
possible_indices = [
    (lambda idx: B[idx])(N - a - 1),
    a,
    N - a
]
from functools import cmp_to_key
ans = sorted(possible_indices, key=cmp_to_key(lambda x, y: (x > y) - (x < y)))[0]
print(ans)