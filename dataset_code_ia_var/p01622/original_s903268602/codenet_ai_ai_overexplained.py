# Boucle principale infinie, qui va continuer jusqu'à ce qu'on sorte avec un 'break'
while True:
    # Demande de la saisie utilisateur, qui est stockée dans la variable N
    N = input()  # input() lit une ligne de l'utilisateur, ici on ne convertit pas en int, donc N reste de type 'str'
    # Vérifie si l'entrée utilisateur N est égale à 0
    if N == 0:    # Attention, ici la comparaison compare N (str) avec 0 (int), il faudrait convertir pour la robustesse
        # Si c'est le cas, on sort de la boucle avec 'break'
        break

    # Création d'une liste 'data' avec une compréhension de liste. On itère N fois.
    # Pour chaque tour, on lit une ligne à l'aide de raw_input() (qui lit une chaîne depuis l'entrée standard)
    # Ensuite, .split() découpe la chaîne en une liste de sous-chaînes selon les espaces
    # map(int, ...) convertit chaque sous-chaîne en un entier
    # data sera donc une liste de listes, où chaque sous-liste contient des entiers
    data = [map(int, raw_input().split()) for _ in xrange(N)]

    # On trie la liste 'data' par ordre décroissant selon le premier élément de chaque sous-liste
    # La clé de tri est lambda x:-x[0], ce qui signifie qu'on trie sur moins le premier élément (donc décroissant)
    data.sort(key = lambda x: -x[0])

    # On extrait deux listes à partir de 'data' en utilisant zip(*) pour séparer les premiers et deuxièmes éléments
    # R contiendra tous les premiers éléments de chaque sous-liste
    # W contiendra tous les deuxièmes éléments
    R, W = zip(*data)

    # Calcul de 'empty' :
    # sum(R[1:]) somme tous les éléments de R sauf le tout premier (sous-liste de R)
    # On soustrait cette somme du premier élément R[0], puis on prend max avec 0 pour éviter les valeurs négatives
    # empty représente un certain "reste" ou "espace vide" calculé à partir de R
    empty = max(0, R[0] - sum(R[1:]))

    # Création de la liste 'dp' (pour programmation dynamique), de longueur empty+1, contenue de 'False'
    # Cette liste servira à stocker l'information sur les sommes atteignables avec les poids dans W
    dp = [False] * (empty + 1)
    
    # On sait qu'une somme de 0 est toujours atteignable (en prenant rien)
    dp[0] = True

    # Initialisation de la variable 'ma', qui va garder la plus grande somme atteignable <= empty
    ma = 0

    # On va itérer sur les poids de W du dernier jusqu'au deuxième (on saute le premier); W[-1:0:-1] génère cette séquence
    for w in W[-1:0:-1]:
        # Si le poids w est supérieur à la capacité restante 'empty', on ne peut pas l'ajouter, on quitte la boucle
        if empty < w:
            break
        # On balaie tous les indices de dp de empty vers 0 (décroissant)
        for i in xrange(empty, -1, -1):
            # Si la somme i est atteignable (dp[i] est True) et que i + w <= empty (on reste dans la limite)
            if dp[i] and i + w <= empty:
                # On met à jour ma si i+w est plus grand
                ma = max(ma, i + w)
                # On marque la somme i+w comme atteignable
                dp[i + w] = True

    # On calcule le résultat final :
    # sum(R) : somme de tous les R
    # sum(W) : somme de tous les W
    # empty-ma : différence entre 'empty' et la plus grande somme atteinte
    print sum(R) + sum(W) + (empty - ma)