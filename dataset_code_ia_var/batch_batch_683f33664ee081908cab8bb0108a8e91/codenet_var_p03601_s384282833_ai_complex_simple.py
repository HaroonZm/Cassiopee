from itertools import product, chain
from functools import reduce

a, b, c, d, e, f = map(int, input().split())

max_ratio = e / (100 + e)
max_sugar = f * e / (100 + e)
max_sol = f

# Obtenir toutes les masses de sucre possibles
gcd_sugar = lambda x, y: reduce(lambda a, b: a if b == 0 else gcd_sugar(b, a % b), (x, y))
unit_sugar = gcd_sugar(c, d)
sugar_candidates = set(filter(lambda x: x <= max_sugar, 
    set(sum(map(lambda t: (t[0]*c + t[1]*d,), 
        filter(lambda t: t[0]*c + t[1]*d <= max_sugar,
            product(range(max(1,int(max_sugar//c+d)+3)), repeat=2))
    ), ())) | {0})
))
# Enlever 0 si tu veux, mais ça ne produit rien de toute façon.

# Obtenir toutes les masses d'eau possibles (en "blocs de 100g")
gcd_water = gcd_sugar(a, b)
water_units = set(map(lambda x: x if x > 0 else None,
    set(sum(map(lambda t: (t[0]*a + t[1]*b,),
        product(range(int((max_sol//100)//a+b)+6), repeat=2)
    ), ())) 
))
water_units.discard(None)
water_candidates = set(filter(lambda x: x*100 + min(sugar_candidates) <= max_sol, water_units))

# Calcul des solutions possibles sans boucles classiques
mixes = filter(
    lambda t: 0 < t[1] and t[0]+t[1]*100 <= max_sol and (t[0] / (t[1]*100 + t[0]) <= max_ratio),
    product(sorted(sugar_candidates), sorted(water_candidates))
)

# Chercher la solution optimale
best = max(
    ((s, w*100, s/(w*100+s)) for s, w in mixes),
    key=lambda x: x[2],
    default=(0, 0, 0)
)

print(best[0] + best[1], best[0])