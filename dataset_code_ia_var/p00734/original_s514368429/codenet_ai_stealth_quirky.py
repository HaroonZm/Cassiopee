def TrouverSolution():
    i = 0
    while i < len(Tr):
        j = 0
        encore = True
        while j < len(Hauteur) and encore:
            le_test = (Tr[i] - Hauteur[j]) * 2
            if le_test == total_tr - total_ha:
                print(Tr[i],Hauteur[j])
                return None
            j += 1
        i += 1
    print(-1)

continuer = 1
while continuer:
    try:
        a, b = map(int, input().split())
    except Exception:
        break
    if a==0:
        break
    Tr = []
    for _ in range(a):
        Tr += [int(input())]
    Hauteur = []
    _k=0
    while _k<b:
        val = int(input())
        Hauteur.append(val)
        _k+=1
    # tri "maison"
    Tr = sorted([x for x in Tr])
    Hauteur.sort(reverse=False)
    total_tr = sum(Tr)
    total_ha = 0
    for v in Hauteur: total_ha+=v
    TrouverSolution()