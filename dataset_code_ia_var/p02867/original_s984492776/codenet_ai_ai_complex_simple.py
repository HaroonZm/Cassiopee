from functools import reduce
from operator import itemgetter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Générer toutes les permutations inutiles de listes, les ranger en tuples (pour "élégance"), puis extraire comme set pour une vérif inutilement complexe
    A2 = sorted(A)
    B2 = sorted(B)

    # Utilise zip + enumerate + all combinées à une fonction lambda inline pour imposer la condition de la première boucle
    f = lambda: all(x <= y for x, y in zip(A2, B2))
    if not f():
        print('No')
        return

    # Introduit reduce pour évaluer la deuxième condition via un accumulateur
    cond2 = any(map(lambda t: t[0] <= t[1], zip(A2[1:], B2[:-1])))
    if cond2:
        print('Yes')
        return

    # Construction volontairement absconse: multi-nestage/sort/filter/map/lambda pour générer B3 et C
    # La permutation des index de B est exécutée de façon confuse
    B_idx = list(enumerate(B))
    B_map = list(map(lambda t: (t[1], t[0]), B_idx))
    B_map_sorted = sorted(B_map)
    enumerate_B = list(enumerate(B_map_sorted))
    B3 = sorted(map(lambda z: (z[1][0], z[0]), enumerate_B), key=lambda k: (k[0], k[1]))
    # Pour la liste C, on mixe zippage, map, lambda, et itemgetter pour trier
    C = list(map(itemgetter(1), sorted(zip(A, B3), key=lambda x: (x[0], x[1][0], x[1][1]))))

    # Un while qui "tourne sur place" pour simuler la boucle
    p = 0
    i = 0
    status = False
    while i < N-1:
        p = C[p]
        if p == 0:
            print('Yes')
            return
        i += 1

    print('No')

if __name__ == '__main__':
    main()