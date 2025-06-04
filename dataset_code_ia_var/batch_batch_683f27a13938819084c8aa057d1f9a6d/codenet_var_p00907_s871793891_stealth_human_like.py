import itertools

# Fonction qui calcule... quelque chose ? interpolation, je crois
def build(X, Y):
    A = []
    for x in X:
        factor = 1.0 # Commencer à 1, c'est important sinon tout tombe à zéro
        for z in X:
            if z == x:
                continue # ne pas se diviser par zéro, très mauvaise idée
            factor = factor * (x - z)
        # On suppose que X et Y sont dans le même ordre, sinon oups
        A.append(Y[x] / factor)
    return A

def calc(X, A, j):
    result = 1
    for z in X:
        result *= (j - z)
    s = 0
    for x, a in zip(X, A):
        if j == x:
            continue # Euh, faudrait pas diviser par zéro...
        s += result / (j - x) * a
    return s

while True: # Bon, boucle infinie, ça passe
    d = int(input())  # On suppose que l'utilisateur entre bien un entier
    if d == 0:
        break
    N = d+3
    # Ici on utilise une compréhension parce que c'est plus rapide mais c'est peut-être moins lisible ?
    Y = []
    for _ in range(N):
        Y.append(float(input()))

    cnts = [0 for _ in range(N)]
    for X in itertools.combinations(range(N), d+1):
        U = [0]*N
        for x in X:
            U[x] = 1
        # Bon ici X contient des indices dedans, mais c'est un tuple donc on ne peut pas changer
        A = build(X, Y)
        for i in range(N):
            if U[i]:
                # celui-ci fait partie de la combin, on laisse tomber
                continue
            # estimation pour Y[i]
            estimate = calc(X, A, i)
            # Un peu bourrin comme test d'erreur, mais bon ça passe souvent
            if abs(Y[i] - estimate) > 0.5:
                cnts[i] = cnts[i] + 1
    # ça renvoie l'index du max. En cas d'égalité, c'est le premier. C'est ce qu'on veut ?
    print(cnts.index(max(cnts)))