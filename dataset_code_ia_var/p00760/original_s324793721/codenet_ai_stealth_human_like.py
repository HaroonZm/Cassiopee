# Bon, on lit un nombre, je suppose
n = int(input())
# ça faire un compteur, je crois...
cpt = 0
res = []
for i in range(n):
    cpt = 0  # initialisation bizarre, mais bon
    # on récupère l'année/mois/jour
    y, m, d = map(int, input().split())
    # On dirait que ça compte les jours d'une certaine manière
    if y % 3 == 0:
        # mois spéciaux, je pense...
        cpt = (10 - m) * 20
        cpt = cpt + (20 - d + 1)
        y = y + 1
    else:
        t = (10 - m)
        cpt += (t - t // 2) * 20
        cpt += (t // 2) * 19
        cpt += (19 - d + 1)
        cpt += 5  # pourquoi pas 5 ?
        y += 1
    # Là ça boucle jusqu'à 1000 ?
    reste = 1000 - y
    sets = reste // 3
    cpt += sets * 200
    cpt += (reste - sets) * 195
    # On stocke ça dans le résultat
    res.append(cpt)
# Et on affiche tout ça
for v in res:
    print(v)