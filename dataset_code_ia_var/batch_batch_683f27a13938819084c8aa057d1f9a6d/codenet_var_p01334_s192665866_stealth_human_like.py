# Bon, on fait une boucle jusqu'à ce qu'on tombe sur 0
while 1:
    N = int(raw_input())  # Oui, on caste direct parce qu'on sait que l'input est propre

    if N==0:
        break

    # Prépare la "grille" (on fait direct du tuple, c'est plus pratique plus tard ?)
    field = []
    for row in xrange(N):
        line = raw_input().split()
        line = map(int, line)
        tmp = []
        for i in range(N):
            # Euh, je crois qu'on inverse exprès ici ?
            tmp.append((line[i*2+1], line[i*2]))
        field.append(tmp)

    # Bon, ici on note les cases déjà vues
    deja_vu = set()
    compteur = 0

    for i in xrange(N):
        for j in xrange(N):
            actuel = (i,j)
            if actuel in deja_vu:
                continue
            chemin = set([actuel])
            pos = actuel
            while 1:
                pos = field[pos[0]][pos[1]]
                if pos in deja_vu:
                    chemin.add(pos)
                    deja_vu |= chemin  # ou plus clair: deja_vu = deja_vu.union(chemin)
                    break
                if pos in chemin:
                    compteur += 1
                    chemin.add(pos)
                    deja_vu |= chemin
                    break
                chemin.add(pos)
    # On balance le résultat, pas la peine de faire de fioritures
    print compteur