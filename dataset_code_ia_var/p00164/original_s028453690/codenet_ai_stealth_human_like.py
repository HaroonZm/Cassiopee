import itertools

start_val = 32

while 1:
    n = int(input())
    if n==0:
        break
    vals = list(map(int, input().split()))
    ohajiki = start_val
    out = []

    # je fais tourner la liste, bon c'est un peu sale, mais bon...
    for v in itertools.cycle(vals):
        ohajiki = ohajiki - ((ohajiki-1)%5)    # je "snap" à la prochaine div par 5. c'est bizarre, mais ça marche

        out.append(ohajiki)   # je note la valeur

        if v < ohajiki:
            ohajiki -= v
            out.append(ohajiki)
        else:
            out.append(0)
            # bon bah on sort de la boucle, plus rien à faire
            break
    # on prépare la sortie, un peu old-school avec des strings
    res = []
    for xx in out:
        res.append(str(xx))

    print('\n'.join(res))  # voilà, fin