from functools import reduce
from itertools import product, starmap, repeat, chain

def bubbleSort(A,N):
    # Générer toutes les paires d'index consécutifs à inspecter à chaque passe, rangés à rebours.
    indices_generator = lambda: ((j, j-1) for j in range(N-1, 0, -1))
    swapped = [True]
    op_count = [0]

    def single_pass(array):
        # Réalise un passage de tri à bulles, retourne True si permutation.
        swaps = []

        def cmp_swap(j, k):
            nonlocal swaps
            if array[j] < array[k]:
                array[j], array[k] = array[k], array[j]
                swaps.append(1)
                op_count[0] += 1

        list(starmap(cmp_swap, indices_generator()))
        return len(swaps)

    # On use un générateur infini et stoppe à la main.
    while swapped[0]:
        swapped[0] = single_pass(A)

    print(*A)
    print(op_count[0])

N = int(next(iter([input()])))
A = list(map(int, chain.from_iterable([input().split()])))

bubbleSort(A,N)