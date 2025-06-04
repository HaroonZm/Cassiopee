def make_routes(ns, used, cur):
    """
    Génère récursivement toutes les routes maximales depuis le sommet `cur`.

    Args:
        ns (int): nombre maximal de sommets (identifiés de 0 à ns inclus).
        used (List[List[bool]]): matrice symétrique indiquant si l'arête [i][j] est déjà utilisée.
        cur (int): sommet courant depuis lequel on étend la route.

    Yields:
        List[List[int]]: une liste de paires représentant une suite continue d'arêtes formant une route.

    Cette fonction explore toutes les routes possibles à partir du sommet `cur` 
    en utilisant de manière exhaustive chaque arête non encore utilisée dans
    le graphe (représenté par la matrice `used`), en mode backtracking pour
    retrouver toutes les combinaisons sans répétition d'arêtes.
    """
    # Si toutes les arêtes partant de cur sont utilisées, la route en cours est terminée
    if all(used[cur]):
        yield []
    else:
        # Pour chaque voisin i du sommet cur pour lequel l'arête cur-i est non utilisée
        for i in (d for d, s in zip(range(ns+1), used[cur]) if not s):
            # Marquer l'arête cur-i comme utilisée (symétriquement)
            used[cur][i] = used[i][cur] = True
            # Pour chaque route prolongeant l'arête [cur, i], générer le chemin
            for ret in make_routes(ns, used, i):
                yield [[cur, i]] + ret
            # Défaire le marquage (backtracking)
            used[cur][i] = used[i][cur] = False

while True:
    # Lire le nombre de sommets ns et d'arêtes nl depuis l'entrée utilisateur
    ns, nl = map(int, raw_input().split())
    # Condition d'arrêt: deux zéros
    if ns == 0 and nl == 0:
        break

    # Créer une matrice de coûts initialisée à 0
    costs = [[0] * (ns + 1) for _ in xrange(ns + 1)]
    # Créer une matrice used marquant toutes les arêtes comme utilisées par défaut
    used = [[True] * (ns + 1) for _ in xrange(ns + 1)]

    # Remplir la matrice de coûts et débloquer les arêtes présentes
    for _ in xrange(nl):
        a, b, c = map(int, raw_input().split())
        costs[a][b] = costs[b][a] = c
        used[a][b] = used[b][a] = False  # Arête disponible

    ans = [0, []]  # [meilleur_coût, meilleure_route]

    # Pour chaque sommet de 1 à ns-1 (inclu) comme point de départ (le graphe commence à 0)
    for i in xrange(1, ns):
        # Pour chaque route construite à partir de i
        for route in make_routes(ns, used, i):
            # Calculer le coût total de la route
            cost = sum(costs[a][b] for a, b in route)
            # Garder la route la plus chère (maximale)
            if ans[0] < cost:
                ans[0] = cost
                ans[1] = route

    # Affichage du meilleur coût trouvé
    print ans[0]
    # Affichage du chemin optimal sous forme "départ inter1 inter2 ... arrivée"
    print "{} {}".format(str(ans[1][0][0]), " ".join(str(a[1]) for a in ans[1]))