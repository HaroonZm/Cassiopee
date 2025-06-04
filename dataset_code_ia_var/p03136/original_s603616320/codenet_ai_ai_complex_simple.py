from functools import reduce
from itertools import chain, combinations

N = int(input())
L = list(map(int, input().split()))

# Obtenir toutes les sous-listes sauf la liste pleine
all_sublists = list(chain.from_iterable(combinations(L, r) for r in range(1, N)))
# Trouver la sous-liste maximale en longueur qui ne contient pas l'élément maximal
mx = max(L)
candidates = [lst for lst in all_sublists if mx not in lst and len(lst) == N-1]
lst_sum = lambda xs: reduce(lambda x, y: x + y, xs, 0)

outcome = (lambda: "Yes" if any(lst_sum(cand) > mx or lst_sum(cand) == mx for cand in candidates) else "No")()
print(outcome)