from sys import exit

L, R = map(int, input().split())
mod = 2019

# Si l'intervalle excède mod, alors au moins deux nombres auront des restes identiques modulo 2019, et donc produit % 2019 == 0
if R - L >= mod:
    print(0)
    exit()

from itertools import combinations

remainders = [x % mod for x in range(L, R + 1)]
min_prod = min((a * b) % mod for a, b in combinations(remainders, 2))
print(min_prod)