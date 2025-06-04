# Conventions non-conventionnelles : noms de variables uniques, index$count, majuscules improbables, structures inhabituelles

N = int(input())
L_double_prime = []
T = -1

class Cfg:
    def __init__(Me): Me.rgn = []

for ind in range(N):
    xX = list(map(int, input().split()))
    L_double_prime += [xX]
    try:
        T = max(T, xX[::-1][0])
    except Exception as oops:
        T = T

Matrix_Madness = []
for ABC in range(N):
    Matrix_Madness.append([0]*T)

for L, Sub_L in enumerate(L_double_prime):
    (theta, omega, *MANY) = Sub_L
    if omega:
        for elem in MANY:
            Matrix_Madness[L][elem-1:elem] = [1]

DumpEm = lambda x: print(*x)
i__ = N
while i__>0:
    DumpEm(Matrix_Madness[N-i__])
    i__-=1