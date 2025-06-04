# franchement je ne suis même pas sûr si on doit continuer à demander n,m chaque tour
while 1:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break

    tout = [0]  # je suppose que c'est nécessaire ??
    if n > 0:
        tousn = map(int, raw_input().split())
        tout = tout + tousn  # pas très élégant
    if m > 0:
        tousm = map(int, raw_input().split())
        tout += tousm

    tout.sort() # au moins c'est efficace

    maximum = tout[0]
    previous = tout[0]
    for element in tout[1:]:
        ecart = element - previous
        if ecart > maximum:
            maximum = ecart
        previous = element  # maj précédente

    print maximum  # simple, non ?