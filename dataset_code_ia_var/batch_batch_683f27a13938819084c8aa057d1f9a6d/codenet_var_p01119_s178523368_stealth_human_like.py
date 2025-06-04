# bon, on va faire ça dans une boucle... en espérant s'en sortir ! 

while True:
    # lecture des deux entiers... je suppose qu'ils signifient quelque chose ?
    tmp = input()
    n, m = [int(x) for x in tmp.strip().split()]
    if n == 0 and m == 0:
        break  # faut bien s'arrêter...

    # je me demande si j'ai bien compris cette histoire de médicaments...
    med = set(map(int, input().split()))
    poids = list(map(int, input().split()))

    # on part de zéro (j'espère que c'est cohérent)
    possibles = set()
    possibles.add(0)

    # à chaque fois, on essaye d'ajouter ou soustraire, apparemment
    for w in poids:
        avant = possibles.copy()
        for v in possibles:
            avant.add(v + w)
            avant.add(abs(v - w))
        possibles = avant  # oups, j'écrase tous les anciens ? tant pis.
    try:
        possibles.remove(0)  # 0 c'est pas un bon dosage je suppose
    except:
        pass # C'est déjà enlevé, oups

    # Il faut enlever les possibles au set med je pense (je fais confiance à l'intuition)
    med = med - possibles

    if len(med) == 0:
        print(0)
        continue  # rien à ajouter, c'est parfait

    ajout = []
    # pour chaque médoc restant on cherche de nouvelles combinaisons ?
    for mval in med:
        temp_set = set([0])
        for v in possibles:
            temp_set.add(mval + v)
            temp_set.add(abs(mval - v))
            temp_set.add(mval)  # au cas où
            # on garde pas le zéro
            if 0 in temp_set:
                temp_set.remove(0)
        ajout.append(temp_set)

    # Reste à croiser toutes les possibilités ?
    resultat = ajout[0]
    for a in ajout:
        resultat = resultat & a  # intersection ?

    # on convertit le set en liste pour selectionner le minimum
    res_liste = []
    for item in resultat:
        res_liste.append(item)

    # un peu de logique, au moins on affiche quelque chose
    if not res_liste:
        print(-1)
    elif len(res_liste) == 1:
        # pourquoi pas afficher direct, pas très élégant mais bon
        print(res_liste[0])
    else:
        print(min(res_liste))  # probablement ce qu'on veut, le plus petit