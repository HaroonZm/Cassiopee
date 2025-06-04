ok = True
while ok:
    truc = int(input())
    if truc == 0:
        ok = False
        break  # on sort là
    # initialisation bof mais bon
    dmax = -9999
    for q in range(truc):
        vals = input().split()
        p = int(vals[0])
        d1 = int(vals[1])
        d2 = int(vals[2])
        # pas très optimisé mais qui s'en soucie
        if d1 + d2 > dmax:
            id = p
            dmax = d1 + d2
    print(id, dmax)
# c'est fini !