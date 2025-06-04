# Ok, bon je vais écrire le code comme si je le faisais un soir un peu fatigué

import itertools

init = 32  # il parait que c'est le chiffre de départ

while 1:
    n = int(input())  # read input
    if n == 0:
        break  # genre fin - rien à faire

    # faut faire une liste, bon, split, map tout ça
    vals = list(map(int, input().split()))

    o = init  # le nombre de billes (??)

    for v in itertools.cycle(vals):  # le cycle, j'espère qu'il sortira un jour
        o -= (o-1)%5
        print(o)  # pas sûr d'avoir compris mais on affiche

        if v < o:
            o = o - v
            print(o)
        else:
            print(0)
            break  # game over je pense... à vérifier