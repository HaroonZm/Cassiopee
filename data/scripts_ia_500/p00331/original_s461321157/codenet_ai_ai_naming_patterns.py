hauteur, racine = [int(nombre) for nombre in input().split()]
if hauteur == -racine:
    print(0)
elif hauteur > -racine:
    print(1)
else:
    print(-1)