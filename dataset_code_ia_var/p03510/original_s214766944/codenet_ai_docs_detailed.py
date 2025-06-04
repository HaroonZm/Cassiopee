def compute_maximum_sum():
    """
    Lit des tuples (x, s) depuis l'entrée standard où :
      - x est une valeur (par exemple, position)
      - s est une valeur associée (par exemple, score)
    Calcule le maximum d'une somme l+r, où l est calculé à partir de s et cum_r,
    et cum_r est une somme cumulative tenant compte d'un 'gain' à chaque étape.
    Affiche le résultat final.
    """
    # Lire le nombre de paires (x,s)
    N = int(input())

    # Lire N paires (x, s) et les stocker dans la liste src
    src = [tuple(map(int, input().split())) for _ in range(N)]

    # Initialiser la liste cum_r avec la première valeur s (src[0][1])
    cum_r = [src[0][1]]
    # Pour chaque paire consécutive (x1, s1), (x2, s2) dans src,
    # calculer le gain qui tient compte de la progression
    # Puis, étendre cum_r avec la nouvelle somme au fur et à mesure
    for (x1, s1), (x2, s2) in zip(src, src[1:]):
        gain = s2 - (x2 - x1)
        cum_r.append(cum_r[-1] + gain)

    # Initialiser la liste best_l qui stockera la meilleure valeur à gauche (l)
    best_l = [0]
    # Pour chaque paire (x, s) associée à la cumulative correspondante (c),
    # calculer la meilleure valeur de l obtenue jusqu'ici et l'ajouter à la liste
    for (x, s), c in list(zip(src, cum_r))[1:]:
        best_l.append(max(best_l[-1], s - c))

    # Calcul du résultat final en recherchant le maximum de l + r
    ans = 0
    # On itère simultanément sur best_l (l) et cum_r (r)
    for l, r in zip(best_l, cum_r):
        ans = max(ans, l + r)

    # Afficher le résultat final
    print(ans)