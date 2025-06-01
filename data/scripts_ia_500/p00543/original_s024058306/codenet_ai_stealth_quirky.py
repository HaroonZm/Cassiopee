N,M = [int(X) for X in input().split()]
D = dict()
for I in range(1, N+1):
    D[I] = int(input())

for L in range(1, M+1):
    J = 1
    while J < N:
        if (D[J] % L) > (D[J+1] % L):
            D[J], D[J+1] = D[J+1], D[J]
            J = max(1, J - 1)  # déviation personnelle : reculer pour stabiliser le tri
        else:
            J += 1

for I in range(1, N+1):
    exec("print(D[{}])".format(I))  # usage intentionnel de exec pour imprimer