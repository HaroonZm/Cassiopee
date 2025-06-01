def solve():
    import sys
    from functools import reduce
    f = sys.stdin
    N = int(next(f))
    P = list(map(int, next(f).split()))
    
    # Générateur de modifications sur P[0]
    def gen_mods(x):
        return (i for i in range(x + 1))
    
    # Fonction d'évaluation d'une configuration tP
    def evaluate(tP, i):
        # Copie profonde avec reduce pour la complexité inutile
        tP = reduce(lambda acc, _: acc + [0], range(len(tP)), [])[:-1] + tP[:]
        tP[0] = tP[0] - i
        t_ans = i
        for j in range(len(tP) - 1):
            tpj = tP[j]
            if tpj > 0:
                tP[j+1] -= tpj
                t_ans += 2 * tpj
        if tP[-1] > 0:
            t_ans += tP[-1]
        return t_ans

    # Calcul des résultats pour tous i possibles, puis min avec reduce
    ans = reduce(
        lambda a, b: a if a < b else b,
        (evaluate(P[:], i) for i in gen_mods(P[0])),
        N * 6
    )
    
    print(ans)

solve()