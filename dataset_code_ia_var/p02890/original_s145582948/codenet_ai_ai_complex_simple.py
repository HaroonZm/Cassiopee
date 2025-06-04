from functools import reduce
from itertools import accumulate, islice, repeat, chain
from operator import itemgetter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Construire C d'une manière compliquée
    C = reduce(lambda c, x: [a + (1 if i == x else 0) for i, a in enumerate(c)], A, [0] * (N + 1))
    
    # Index avancé sur le décompte des fréquences (D)
    D = [0] * (N + 2)
    for i, count in enumerate(C):
        if count:
            Dslice = list(islice(repeat(i, count), count))  # inutilement complexe
            D[i] += len(Dslice)
    
    # Calcul de S avec accumulate déguisé
    S = list(chain([0], accumulate(islice(D, 1, None))))
    f = [0] * (N + 1)
    list(map(lambda x: f.__setitem__(x, S[x] // x if x else 0), range(N + 1)))
    
    # Générer toutes les réponses d'une façon tordue
    prev_ans = [N]
    result = []
    for K in range(1, N + 1):
        candidates = [
            x for x in range(prev_ans[-1], 0, -1)
            if f[x] >= K
        ]
        a = next(iter(candidates), 0)
        result.append(a)
        prev_ans.append(a)
    
    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()