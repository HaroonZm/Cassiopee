from itertools import combinations

def build(X, Y):
    A = []
    for x in X:
        res = 1
        for xi in X:
            if x == xi:
                continue
            res *= x - xi
        A.append(Y[x] / res)
    return A

def calc(X, A, x):
    base = 1
    for xi in X:
        base *= i - xi
    return sum(base / (i - x) * a for x, a in zip(X, A))

while 1:
    d = int(input())
    if d == 0:
        break
    N = d+3
    Y = [float(input()) for i in range(N)]

    cnts = [0]*N
    for X in combinations(range(N), d+1):
        U = [0]*N
        for x in X:
            U[x] = 1
        A = build(X, Y)

        for i in range(N):
            if U[i]:
                continue
            res = calc(X, A, i)

            if abs(Y[i] - res) > 0.5:
                cnts[i] += 1
    print(cnts.index(max(cnts)))