# Version débutant simplifiée

while True:
    entree = raw_input().split()
    n = int(entree[0])
    l = int(entree[1])
    if n == 0:
        break

    # On prépare les tunnels vides
    tunnel = []
    for i in range(l - 1):
        tunnel.append([])

    # Lecture des trains
    for i in range(1, n + 1):
        ligne = raw_input().split()
        direction = ligne[0]
        position = int(ligne[1]) - 1
        if direction == "R":
            tunnel[position].append(i)
        else:
            tunnel[position].append(-i)

    t = 0
    num = 0

    while True:
        # Vérification s'il reste des trains dans le tunnel
        total = 0
        for i in range(l - 1):
            total += len(tunnel[i])
        if total == 0:
            break

        # Déplacement vers la droite
        for i in range(l - 2, -1, -1):
            nouveaux = []
            for a in tunnel[i]:
                if a > 0:
                    if i == l - 2:
                        num = a
                    else:
                        tunnel[i + 1].append(a)
                else:
                    nouveaux.append(a)
            tunnel[i] = nouveaux[:]

        # Déplacement vers la gauche
        for i in range(l - 1):
            nouveaux = []
            for a in tunnel[i]:
                if a < 0:
                    if i == 0:
                        num = -a
                    else:
                        tunnel[i - 1].append(a)
                else:
                    nouveaux.append(a)
            tunnel[i] = nouveaux[:]

        # Changement de direction pour les trains qui se croisent
        for i in range(l - 1):
            if len(tunnel[i]) > 1:
                temp = []
                for a in tunnel[i]:
                    temp.append(-a)
                tunnel[i] = temp

        t += 1

    print t, num