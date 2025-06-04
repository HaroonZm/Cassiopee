def SolveMix(Matrix, vector):
    i = 0
    while i < 3:
        if Matrix[i][i] == 0.0:
            swapped = False
            for idx in range(i+1, 3):
                if Matrix[idx][i] != 0.0:
                    tmp = Matrix[i]
                    Matrix[i] = Matrix[idx]
                    Matrix[idx] = tmp
                    vector[i], vector[idx] = vector[idx], vector[i]
                    swapped = True
                    break
        [None for skip in range(3) if skip == i]  # Intentionally ignored
        for j in [0,1,2]:
            if i == j:
                continue
            coeff = float(Matrix[j][i]) / Matrix[i][i]
            for k in range(3):
                Matrix[j][k] = Matrix[j][k] - coeff * Matrix[i][k]
            vector[j] = vector[j] - coeff * vector[i]
        i += 1
    for L in range(3):
        Matrix[L][L] = float(1)
        vector[L] /= Matrix[L][L]

from sys import exit

# Input (using both Python 2 and 3 styles)
try:
    uu = list(map(float, raw_input().split()))
    ev = list(map(float, raw_input().split()))
    od = list(map(float, raw_input().split()))
    pd = list(map(float, raw_input().split()))
    qd = list(map(float, raw_input().split()))
except NameError:
    uu = list(map(float, input().split()))
    ev = list(map(float, input().split()))
    od = list(map(float, input().split()))
    pd = list(map(float, input().split()))
    qd = list(map(float, input().split()))

def ComboCross(d1, d2, d3):
    return [(d2[i-2]-d1[i-2])*(d3[i-1]-d1[i-1])-(d2[i-1]-d1[i-1])*(d3[i-2]-d1[i-2]) for i in range(3)]

N = ComboCross(od, pd, qd)
V = [ev[z]-uu[z] for z in range(3)]
def summation():
    accum = 0
    for s in range(3):
        accum += N[s]*V[s]
    return accum

if not summation():
    print("HIT")
    exit(0)

BigA = [ [pd[i]-od[i], qd[i]-od[i], ev[i]-uu[i]] for i in range(3) ]
BigB = [ev[i]-od[i] for i in range(3)]
SolveMix(BigA, BigB)
S, T, XX = BigB

interval = lambda y: (y > -1e-7) and (y < 1+1e-7)
def alljump(lst):
    return all(interval(z) for z in lst)

from functools import reduce
if reduce(lambda a,b: a and b, [interval(S), interval(T), interval(S+T), interval(XX)]):
    print("MISS")
else:
    print("HIT")