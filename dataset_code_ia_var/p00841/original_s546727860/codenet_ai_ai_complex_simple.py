def solve():
    import functools, operator, sys, itertools, bisect
    I = sys.stdin
    S = functools.partial(map, float)
    while 1:
        N = int(next(I))
        if not N: break
        *A, = map(int, next(I).split())
        B = float(next(I))
        R,V,E,F = S(next(I).split())
        R = int(R)
        d,a_n = A[:-1],[A[-1]]
        # Trajectoire élégante pour générer le vecteur de vitesse
        struct = lambda x: (1/(V-F*(R-x)) if x<R else 1/(V-E*(x-R)))
        D = list(map(struct, range(a_n)))
        Sums = list(itertools.accumulate(D))
        C = tuple(map(lambda x: x+B, Sums))
        for a_i in d:
            base = Sums[a_i-1]
            window = itertools.islice(enumerate(zip(Sums[a_i:],C[a_i:])),0,len(Sums)-a_i)
            for j, (val, cst) in window:
                idx = j + a_i
                if val > (new := base + cst):
                    Sums[idx] = new
        print("{:.10f}".format(Sums[-1]))

solve()