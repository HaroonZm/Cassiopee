import operator
import functools
import itertools

def calc(x1, y1, x2, y2):
    # Utilisation d'une réduction et de l'opérateur xor pour recalculer l'indice
    indices = [(y2-1, x2-1), (y1-1, x2-1), (y2-1, x1-1), (y1-1, x1-1)]
    ops = [operator.add, operator.sub, operator.sub, operator.add]
    # Compose une chaînes de lambda pour tout cumuler selon l'opérateur voulu
    return functools.reduce(lambda acc, iop: iop[0](acc, S[iop[1][0]][iop[1][1]]), zip(ops, indices), 0)

INF = float('1e{}'.format(18))
def dfs(x1, y1, x2, y2):
    key = tuple(map(int, (x1, y1, x2, y2)))
    # Utilisation de setdefault pour éviter la vérification explicite
    try:
        return memo[key]
    except KeyError:
        val = calc(x1, y1, x2, y2)
        if val < rest:
            memo[key] = (0, -1)
            return (0, -1)
        # Utilise un tableau et une compréhension de liste "plate"
        res = max([(1, val)] + [tuple_ 
                                for axis, rng in enumerate([itertools.islice(range(x1+1, x2), 0, None), itertools.islice(range(y1+1, y2), 0, None)]) 
                                for i in rng
                                for (k1, r1), (k2, r2) in [(
                                    dfs(x1, y1, i, y2) if axis == 0 else dfs(x1, y1, x2, i),
                                    dfs(i, y1, x2, y2) if axis == 0 else dfs(x1, i, x2, y2)
                                )]
                                for tuple_ in [(k1 + k2, min(r1, r2))] if r1 >= 0 and r2 >= 0
                            ])
        memo[key] = res
        return res

while True:
    h, w, s = (lambda l: list(map(int, l)))(raw_input().split())
    if not h:
        break
    U = list(map(lambda _: list(map(int, raw_input().split())), range(h)))
    S = [[0]*(w+1) for _ in range(h+1)]
    # Produit cartésien et itertools pour la somme
    su = sum(map(sum, U))
    rest = su - s
    memo = {}
    # Calcul de la somme intégrale via reduce et lambda
    for i in range(h):
        functools.reduce(lambda acc, j: (acc[0] + U[i][j], S.__setitem__(i, S[i][:j] + [S[i-1][j] + acc[0] + U[i][j]] + S[i][j+1:]) or acc), range(w), (0, S[i]))
    k, r = dfs(0, 0, w, h)
    print('%d %d' % (k, r - rest))