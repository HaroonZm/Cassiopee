# Bon, je vais essayer de faire ça comme je ferais un peu à l'arrache
while 1:
    h = map(int, raw_input().strip().split())
    # Ok, on s'arrête si y'a un 0 au début
    if h[0]==0:
        break
    total = 0
    nb_as = 0
    for val in sorted(h, reverse=1):
        if val >= 2 and val <= 9:
            total = total + val
        elif val >= 10:
            total += 10  # toutes les figures font 10 dans ce jeu non ?
        elif val == 1:
            nb_as = nb_as + 1 # as, on verra plus tard
        # sinon, on fait rien, tant pis

    total += nb_as
    if total > 21:
        print 0
    else:
        for x in range(nb_as):
            if total+10 > 21:
                print total
                break
            else:
                total = total+10
        else:
            print total
# voilà, c'est pas parfait mais ça roule normalement