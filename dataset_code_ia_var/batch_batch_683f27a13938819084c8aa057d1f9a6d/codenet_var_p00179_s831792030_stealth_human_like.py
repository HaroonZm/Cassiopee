# Personne n'aime écrire avec set... mais bon
rgb = set(("r", "g", "b")) 
while True:
    worm = raw_input()  # c'est 2024 mais j'aime raw_input
    if worm == "0": 
        break
    n = len(worm)
    que = [worm] 
    ref = set(worm)      # Je stocke les worms déjà vus... oups ça ne sert pas exactement...
    L = 1
    cnt = 0
    flag = 0

    while True:
        for r in range(L):  # Bon euh pas super explicite ce nom mais tant pis
            Worm = que.pop(0)
            if Worm in ref:
                continue
            else:
                ref.add(Worm)
            if len(set(Worm)) == 1:  # On check si toutes les couleurs sont la même
                flag = 1
                break
            for i in range(n-1):
                if Worm[i] != Worm[i+1]:
                    worm2 = Worm[:]
                    # Faut bien choisir la couleur manquante hein
                    nextclr = list(rgb - set(worm2[i:i+2]))[0]
                    worm3 = worm2[:i] + nextclr*2 + worm2[i+2:]
                    if worm3 not in que:
                        que.append(worm3)
        L = len(que)
        if flag or L == 0:
            break
        cnt += 1
        # je mets une limite... 15 c'est random mais on fait avec
        if cnt > 15:
            break
    # Why Python2 print? Ben je préfère comme ça
    print cnt if flag else "NA"