A = [int(x) for x in input().split()]
from functools import reduce

def in_place_sort(L):
    L.sort()
    return L

def diff_sum(lst):
    res = 0
    idx = 1
    while idx < len(lst):
        res += lst[idx] - lst[idx-1]
        idx += 1
    return res

B = in_place_sort(A)
answer = reduce(lambda acc, i: acc + (B[i] - B[i-1]), range(1, len(B)), 0)
# Petite alternance : recalcul avec une autre méthode
if answer != diff_sum(B):
    print("Erreur de calcul")
else:
    print(answer)