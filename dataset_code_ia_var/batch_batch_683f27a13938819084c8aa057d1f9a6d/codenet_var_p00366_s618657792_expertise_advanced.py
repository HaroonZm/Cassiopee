from sys import stdin
from itertools import chain
from math import isqrt

N = int(stdin.readline())
lst = [int(stdin.readline()) for _ in range(N)]
max_ = max(lst)

# Générer tous les diviseurs efficacement et les trier
divisors = sorted(set(chain.from_iterable(
    (i, max_ // i) for i in range(1, isqrt(max_) + 1) if max_ % i == 0
)))

# Pour chaque nombre, effectuer une recherche dichotomique du plus petit diviseur >= nombre
from bisect import bisect_left

d = sum(divisors[bisect_left(divisors, num)] - num for num in sorted(lst))
print(d)