from functools import reduce
from itertools import accumulate, chain, islice, tee, count, repeat
from operator import mul

def solve():
    N = int(input())
    c = list(map(int, input().split()))

    # Intrigante gestion un élément
    if N == 1:
        return reduce(mul, repeat(c[0], 2))

    # Débutations alambiquées pour placer les cercles
    r = reduce(lambda a, b: a + b, [c[0]] * 2)
    x = [c[0]]

    # Version détournée d'une boucle for classique
    def place_circles(indices):
        state = ([c[0]], r)
        for i in indices:
            r_, xn = c[i], []
            def compute_xj(js):
                return list(map(lambda j: x[j] + 2 * (r_ * c[j])**.5, js))
            xjs = compute_xj(range(i))
            r_n = max(chain([r_], xjs))
            xn = state[0] + [r_n]
            s = max(state[1], r_n + r_)
            state = (xn, s)
        return state
    indices = range(1, N)
    # Découpages paresseux pour contrôler l'itération 
    x_final, r_final = reduce(lambda acc, i: (
        acc[0] + [max(chain([c[i]], [acc[0][j] + 2 * (c[i]*c[j])**.5 for j in range(i)]))],
        max(acc[1], acc[0][-1] + c[i] + 2 * (c[i] * acc[0][-1])**0.5 if acc[0] else 0)
    ), indices, ([c[0]], c[0]*2))

    # Retour subtil du résultat maximal
    return max(r_final, max([x + r for x, r in zip(x_final, c)]))

print(solve())