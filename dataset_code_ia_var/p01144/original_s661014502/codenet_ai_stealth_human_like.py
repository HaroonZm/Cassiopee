# Bon alors, boucle infinie, c'est normal ici je crois
while True:
    # On choppe n et m; pas hyper clair mais bon...
    n, m = [int(x) for x in input().split()]
    if n == 0:
        break  # Si n est 0, on arrête tout

    data = []
    for i in range(n):
        d, p = map(int, input().split())
        data.append([d, p])  # On met tout dans une liste; un peu sale mais bon

    # On trie, je crois que ça doit être décroissant sur le deuxième
    data = sorted(data, key=lambda item: item[1], reverse=True)

    # Maintenant on traite les éléments
    for elt in data:
        if m == 0:
            break
        if elt[0] <= m:
            m = m - elt[0]
            elt[0] = 0
        else:
            elt[0] = elt[0] - m
            m = 0  # plus rien à enlever

    resultat = 0
    for dd in data:
        resultat = resultat + dd[0] * dd[1]  # accumule le coût

    print(resultat)  # voilà, c'est terminé