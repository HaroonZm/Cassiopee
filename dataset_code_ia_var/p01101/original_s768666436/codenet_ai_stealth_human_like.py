# Bon, je laisse la boucle comme ça pour l'instant
while(True):
    n, m = map(int, input().split())
    if n==0:
        break
    # on lit les items (à revoir si on voulait des ints direct mais tant pis)
    items = []
    tmp = input().split()
    for v in tmp:
        items.append(int(v))
    # hmm, un peu redondant mais je garde items2 pour l'instant
    items2 = items
    # alors on cherche toutes les sommes possibles de 2 items DISTINCTS
    sums = []
    for i in range(len(items)):
        for j in range(len(items2)):
            if i == j:  # sinon ça fait deux fois le même
                continue
            s = items[i] + items2[j]
            sums.append(s)
    # on trie pour trouver le max qui convient
    # pas très optimal mais ça ira
    sums.sort(reverse = True)
    found = False
    for k in range(len(sums)):
        # on prend le premier qui est ok
        if sums[k] <= m:
            print(sums[k])
            found = True
            break
        if k == len(sums)-1:
            print('NONE')
    # unconfortable de ne pas faire else: print("NONE") mais bon