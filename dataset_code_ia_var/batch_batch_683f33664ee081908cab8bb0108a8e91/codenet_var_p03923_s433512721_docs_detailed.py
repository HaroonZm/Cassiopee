def minimal_time_to_bake_bread():
    """
    Calcule et affiche le temps minimal pour cuire n pains avec a minutes d'attente entre chaque opération "manger".
    Utilise une stratégie de type simulation combinée à une recherche binaire pour minimiser le temps de cuisson.
    Les entrées sont lues depuis raw_input() sous forme de deux entiers séparés par un espace.
    """
    # Lire les valeurs n (nombre de pains à cuire) et a (temps supplémentaire pour chaque session "manger")
    n, a = map(int, raw_input().split())
    
    # Initialiser la réponse avec une très grande valeur (assure que la première solution trouvée sera prise)
    ans = 10 ** 12 + 5

    # Parcourir les différentes possibilités pour le nombre de sessions "manger" (arbitrairement borné à 45 pour les performances)
    for eat_num in xrange(45):
        # Si le nombre de pains potentiels dépasse n, sortir de la boucle
        if 2 ** (eat_num - 1) > n:
            break

        # Calculer le temps passé à attendre à chaque "manger"
        time = eat_num * a

        # Le nombre total de sessions de cuisson
        bake = eat_num + 1

        # Recherche binaire pour trouver la taille minimale du lot permettant de cuire n pains en 'bake' sessions
        l = 0
        r = n
        while r - l > 1:
            # Prendre la moyenne de l et r (division entière)
            m = (r + l) // 2
            if m ** bake >= n:
                r = m
            else:
                l = m

        # Vérifier s'il est bénéfique de répartir certaines sessions avec (r-1) pains cuits
        for surplus in xrange(1, bake + 1):
            # Calculer si en prenant 'surplus' sessions à (r-1) et le reste à r, on peut encore cuire n pains
            if r ** (bake - surplus) * (r - 1) ** surplus < n:
                break
        surplus -= 1  # On retire 1 car 'surplus' a dépassé la limite au dernier tour

        # Calculer le temps total avec cette configuration
        time += r * (bake - surplus) + (r - 1) * surplus

        # Mettre à jour la réponse si on a trouvé un meilleur temps
        ans = min(ans, time)
    
    # Afficher la réponse finale, le temps minimal trouvé
    print ans