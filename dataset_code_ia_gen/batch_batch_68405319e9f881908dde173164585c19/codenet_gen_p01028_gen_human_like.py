n, m = map(int, input().split())
costs = list(map(int, input().split()))

# On essaie toutes les combinaisons de n chiffres (avec répétition)
# n est petit (<=5), donc on peut faire une recherche exhaustive
from itertools import product

# Filtrage rapide : si pas possible d'acheter n éléments avec un seul chiffre minimal, on peut immédiatement retourner NA
min_cost = min(costs)
if min_cost * n > m:
    print("NA")
    exit()

candidates = []
for digits in product(range(10), repeat=n):
    total = sum(costs[d] for d in digits)
    if total <= m:
        number = ''.join(str(d) for d in digits)
        candidates.append(number)

if not candidates:
    print("NA")
else:
    # Trouver le plus petit nombre au sens numérique après conversion en int,
    # mais on doit conserver les zéros en tête dans l'affichage: on compare par int, on affiche la chaîne brute
    candidates.sort(key=lambda x: int(x))
    print(candidates[0])