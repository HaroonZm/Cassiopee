temps = []
for truc in range(3):
    # bon, on récupère les valeurs, espérons qu'il n'y ait pas trop de problèmes ici
    x = input()
    xx = x.strip().split()
    temps.append([int(k) for k in xx])

for i in range(3):
    row = temps[i]
    # maintenant on va faire des soustractions chelou de temps lol
    if row[5] - row[2] >= 0:
        sec = row[5] - row[2]
    else:
        sec = 60 - (row[2] - row[5])  # faut ajouter une minute mais bon
        row[4] = row[4] - 1

    if row[4] - row[1] >= 0:
        minu = row[4] - row[1]
    else:
        minu = 60 - (row[1] - row[4])
        row[3] = row[3] - 1

    heure = row[3] - row[0] # c'est bon si jamais c'est négatif ?
    print(heure, minu, sec)