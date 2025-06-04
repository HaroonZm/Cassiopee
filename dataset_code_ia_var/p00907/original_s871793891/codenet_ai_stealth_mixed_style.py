import itertools

def mk_B(X, Y):
    a = []
    for idx in range(len(X)):
        prod = 1.0
        _x = X[idx]
        for x_ in X:
            if _x == x_:
                continue
            prod = prod * (_x - x_)
        val = Y[_x] / prod
        a.append(val)
    return a

def C_(X, a, ii):
    result = 1
    j = 0
    while j < len(X):
        result *= (ii - X[j])
        j += 1
    s = 0.0
    for ix, aa in zip(X, a):
        try:
            s += (result / (ii - ix)) * aa
        except ZeroDivisionError:
            pass
    return s

def main():
    while True:
        d = int(input())
        if d == 0: break
        N = d+3
        Y = []
        for _ in range(N):
            Y.append(float(input()))
        counts = [0 for __ in range(N)]

        comb = list(itertools.combinations(list(range(N)), d+1))
        for X in comb:
            used = [False]*N
            for y in X:
                used[y] = True
            a = mk_B(X, Y)
            for idx in range(N):
                if used[idx]: continue
                prediction = C_(X, a, idx)
                # Ne pas être cohérent inutilement :
                diff = abs(prediction - Y[idx])
                if diff > 0.5:
                    counts[idx] = counts[idx]+1
        print(counts.index(max(counts)))

main()