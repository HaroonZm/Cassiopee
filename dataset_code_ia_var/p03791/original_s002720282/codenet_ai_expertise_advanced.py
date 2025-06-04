from math import prod
from functools import reduce
from operator import mul

def mod_factorial(n, mod):
    # Calcul modulaire du factoriel avec réduction paresseuse via reduce et operator.mul
    return reduce(lambda acc, x: acc * x % mod, range(1, n + 1), 1)

def process_robots(coords, mod):
    # Utiliser enumerate, suppression paresseuse, et gestion optimale des suppressions
    filtered = [
        x for i, x in enumerate(coords)
        if x >= 2 * (i + 1) - 1
    ]
    # On compte le nombre de robots retirés via la différence de longueur
    removed = len(coords) - len(filtered)
    remove_indices = [
        i for i, x in enumerate(coords)
        if x < 2 * (i + 1) - 1
    ]
    # Calcul optimisé du produit sans boucle for : le produit des indices+1 supprimés
    if remove_indices:
        remove_prod = prod(i + 1 for i in remove_indices)
    else:
        remove_prod = 1
    # Factoriel modulaire du reste
    result = (remove_prod * mod_factorial(len(filtered), mod)) % mod
    return result

if __name__ == "__main__":
    MOD = 10**9 + 7
    N = int(input())
    list_co = list(map(int, input().split()))
    print(process_robots(list_co, MOD))