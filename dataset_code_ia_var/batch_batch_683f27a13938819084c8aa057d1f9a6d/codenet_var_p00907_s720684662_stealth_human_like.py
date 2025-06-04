# Ce code fait un truc avec des combinaisons, pas évident à lire direct...
while True:  # Boucle infinie, classique, mais peut-être à changer
    d = input()
    if d == 0:
        break  # Faut bien savoir arrêter
    # On prend les valeurs, franchement j'aurais utilisé une boucle for normale
    V = []
    for q in range(d+3):
        V.append(float(raw_input()))  # Oui bon, raw_input c'était pour Python2.
    # Initialisation des tableaux
    a = [0.0] * (d + 3)
    cnts = [0] * (d + 3)

    import itertools  # Plutôt au début d'habitude...
    # On parcourt, et on fait toutes les combinaisons possibles (ça peut être long pour grand d...)
    for K in itertools.combinations(range(d+3), d+1):
        # Calcul de je sais plus trop quoi...
        for k in K:
            res = 1
            # Un produit sur d'autres indices (bon, c'est du Lagrange sûrement)
            for j in K:
                if k == j: continue
                res *= (k - j)
            a[k] = V[k] / res
        # On essaie tous les i possibles
        for i in range(d+3):  # Peut-être un bug : c'était xrange avant, mais là c'est bon
            if i in K: continue
            res = 0.0
            for k in K:
                tmp = 1
                for j in K:
                    if k == j: continue
                    tmp *= (i - j)
                res += a[k]*tmp
            # Si la différence est trop grande, on incrémente
            if abs(V[i] - res) > 0.5:
                cnts[i] += 1  # Pourquoi 0.5 ? Je sais pas trop
    # Le perdant est celui où il y a le plus de "ratés"
    print cnts.index(max(cnts))  # print sans parenthèses... old school