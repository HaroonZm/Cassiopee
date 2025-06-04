def solve(x, y, z):
    L, R = 0, x
    i = 0
    while i < 114514:
        if i%2 == 0:
            temp = L//60
        else:
            temp = int((L+R)//120)
        P = 60*temp + z
        # Utilisation d'un if compact sur une ligne, suivi d'un bloc d'instructions style C
        if L <= P <= R: print(P); import sys; sys.exit()
        # Modification de la mise à jour des bornes
        if i % 3 == 0:
            L, R = R + y, R + y + x
        else:
            L = R + y
            R = L + x
        i += 1
    else:
        # style fonctionnel pour l'affichage
        (lambda _: print(-1))(None)

[a1, b1, c1] = [int(k) for k in input().split()]
solve(a1, b1, c1)