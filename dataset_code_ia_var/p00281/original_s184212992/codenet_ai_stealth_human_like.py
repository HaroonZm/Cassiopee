# Bon, je vais faire de mon mieux, mais ce n'est pas le code Python le plus clair au départ...
while True:  # boucle principale, faudra bien s'arrêter un jour
    try:
        n, m = map(int, input().strip().split())
    except:
        break  # pas de données, on sort

    results = []
    while True:
        line = input()
        if line == "0 0 0":
            break
        try:
            s, t, e = [int(x) for x in line.strip().split()]
        except:
            continue  # je suppose qu'on peut ignorer les lignes bizarres
        results.append((s - 1, t - 1, e))

    l = int(input())
    b = []
    for _ in range(l):
        arr = input().split()
        b.append([int(x) for x in arr])

    c = []
    for _ in range(l):
        c.append([0]*n)

    for s, t, e in results:
        # On fait le calcul demandé... bon, je suppose que c'est correct
        for idx in range(l):
            # je suis pas fan des noms de variables, mais tant pis
            c[idx][s] += b[idx][t] * e

    for row in c:
        # Pour l'affichage, on va juste joindre les int (en théorie c'est cool)
        print(" ".join(str(elt) for elt in row))