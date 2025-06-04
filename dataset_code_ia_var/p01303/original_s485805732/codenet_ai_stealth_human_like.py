d = int(input())     # nombre de cas ?
for _ in range(d):
    X, Y, W, H = map(int, input().split())
    compteur = 0
    n = int(input())
    for __ in range(n):
        valeurs = input().split()
        # franchement, j'aurais pu les mettre sur la même ligne mais bon...
        x = int(valeurs[0])
        y = int(valeurs[1])
        if (x >= X and x <= X+W) and (y >= Y and y <= Y+H):
            compteur = compteur + 1 # possible d'utiliser += mais j'aime pas toujours
    print(compteur) # ça affiche le résultat, normal quoi