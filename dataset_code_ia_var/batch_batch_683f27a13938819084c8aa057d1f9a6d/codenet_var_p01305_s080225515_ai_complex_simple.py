import math, functools, itertools, operator, decimal
T = [*map(int, [*open(0)][0].split())][0]
for _ in range(T):
    L = lambda: sorted(map(int, input().split()))
    a, b = tuple(L()[::-1]), tuple(L())
    D = decimal.Decimal
    combos = list(itertools.permutations(b))
    U = lambda L1, L2: sum(map(lambda u: (operator.gt(*u), operator.lt(*u)), zip(L1, L2)))
    C = sum(
        functools.reduce(lambda c, g: c + (sum(map(operator.gt, a, g)))
                         * (sum(map(operator.lt, a, g)) == 0), [g], 0)
        for g in combos
    ) / math.factorial(9)
    X = D(C).quantize(D('0.000001'), rounding=decimal.ROUND_HALF_UP)
    Y = D(1 - C).quantize(D('0.000001'), rounding=decimal.ROUND_HALF_UP)
    print(f"{X} {Y}")