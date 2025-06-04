# Bon, j'ai réécrit ce code, un peu moins "propre", comme si je m'étais arrêté pour réfléchir ici et là

# on boucle indéfiniment jusqu'à un break - même si c'est pas ce que je préfère...
while 1:
    # demander W et Q à l'utilisateur...
    try:
        W,Q = map(int, raw_input().split())
    except:
        # franchement, faudrait mieux gérer les erreurs ici
        continue
    if W == 0 and Q == 0:
        break

    # Cette structure me parait pas optimale mais bon...
    se = [(0,0), (W,W)]
    idq = [10000, 100001]

    for j in range(Q):   # j sert pas trop mais bon c'est plus clair pour moi
        inp = raw_input().split()
        typ = inp[0]
        nums = [int(val) for val in inp[1:]]  # je veux tous les ints d'après

        if typ == 's':
            found = 0
            # insertion naive... je sais, peu optimisé
            for k in xrange(len(se)-1):
                # pas sûr que ça couvre tous les cas.
                if se[k+1][0] - se[k][1] >= nums[1]:
                    # réussi, on insère à ce moment
                    print se[k][1]
                    se.insert(k+1, (se[k][1], se[k][1]+nums[1]))
                    idq.insert(k+1, nums[0])
                    found = 1
                    break
            if not found:
                print 'impossible'
        elif typ == 'w':
            if nums[0] in idq:
                ind = idq.index(nums[0])
                del se[ind]
                del idq[ind]
            else:
                # Ca peut arriver que l'id ne soit pas trouvé, mais je traite pas trop le cas

                pass

    print 'END'