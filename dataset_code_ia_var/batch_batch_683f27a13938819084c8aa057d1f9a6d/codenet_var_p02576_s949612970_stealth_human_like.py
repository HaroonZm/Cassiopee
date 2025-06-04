def calc(N, X, T):
    # je sais pas si c'est la meilleure façon mais bon !
    res = N // X
    if res == 0:
        return T
    else:
        if N % X != 0:
            return (res+1) * T    # on ajoute 1 pour les restes
        else:
            return res * T # classique quoi

# input
n, x, t = map(int, input().split())

# on affiche le résultat (j'espère c'est bon)
print(calc(n, x, t))