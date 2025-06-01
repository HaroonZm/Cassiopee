while(1):
    # Démarrage d'une boucle infinie. Cette boucle continuera à s'exécuter
    # indéfiniment jusqu'à ce qu'une condition interne provoque une sortie (break).
    
    [n, m, h, k] = [int(x) for x in input().split()]
    # Lecture d'une ligne d'entrée utilisateur, qui contient plusieurs nombres séparés par des espaces.
    # La méthode input() récupère la chaîne de caractères saisie.
    # La méthode split() transforme cette chaîne en une liste où chaque élément est une chaîne représentant un nombre.
    # La compréhension de liste convertit chaque élément en entier.
    # Les valeurs sont ensuite unpackées dans les variables n, m, h, k.
    # n, m, h, k sont des entiers avec des significations spécifiques au problème.
    
    if n == 0:
        # Test si n est égal à 0.
        # Cette condition sert de critère d'arrêt pour la boucle infinie.
        break
        # Sortie immédiate de la boucle while. Le programme arrête la lecture de nouvelles entrées.
    
    A = []
    # Initialisation d'une liste vide A, qui sera utilisée plus tard pour stocker des entiers.
    
    B = [[] for x in range(h)]
    # Création d'une liste B composée de h sous-listes vides.
    # Cela crée une structure à deux dimensions où B[y] représente une liste associée à l'indice y.
    
    C = list(range(n))
    # Création d'une liste C initialisée avec les entiers de 0 à n-1.
    # range(n) génère une séquence d'entiers de 0 à n-1.
    # list(range(n)) convertit cette séquence en liste.
    # C peut représenter une permutation ou un ordre initial dans le contexte du problème.
    
    S = [0 for i in range(n)]
    # Création d'une liste S de longueur n où chaque élément est initialisé à 0.
    # C'est une construction typique pour préparer un tableau de valeurs associées à chaque index.
    
    X = []
    # Initialisation d'une liste vide X, destinée à stocker des couples ou des paires d'entiers.
    
    for i in range(n):
        A.append(int(input()))
        # Boucle qui s'exécute n fois.
        # À chaque itération, on lit une ligne d'entrée utilisateur, on transforme sa valeur en entier,
        # puis on ajoute cet entier à la liste A à la fin.
        # A contiendra ainsi n entiers lus séquentiellement.
    
    for i in range(m):
        [a, b] = [int(x) for x in input().split()]
        # Pour chaque itération, on lit une ligne d'entrée contenant deux entiers séparés par un espace.
        # Ces deux entiers sont convertis en int et assignés aux variables a et b.
        
        B[b].append(a)
        # On ajoute la valeur a à la sous-liste B[b].
        # Cela associe la valeur a à l'indice b dans la structure B.
        # Ici, b agit comme clé ou catégorie dans un regroupement des valeurs a.
    
    for y in range(h):
        # Parcourt chaque indice y de 0 à h-1.
        
        for a in B[y]:
            # Pour chaque élément a dans la liste B[y], on effectue l'opération suivante:
            
            C[a-1 : a+1] = [C[a], C[a-1]]
            # Cette ligne effectue un échange des éléments aux positions a-1 et a dans la liste C.
            # L'opération de slicing C[a-1 : a+1] sélectionne deux éléments: celui à l'indice a-1 et celui à l'indice a.
            # L'affectation les remplace par une liste inversée : [C[a], C[a-1]].
            # C'est un moyen compact et efficace d'échanger deux éléments adjacents d'une liste.
            
            X.append(sorted(C[a-1 : a+1]))
            # On ajoute à la liste X une copie triée des deux éléments échangés.
            # sorted() garantit que la paire est enregistrée dans l'ordre croissant, ce qui peut faciliter la comparaison ultérieure.
    
    for i in range(n):
        S[C[i]] = A[i]
        # Cette boucle associe les valeurs de A aux indices modifiés par la permutation dans C.
        # Pour chaque position i dans 0..n-1:
        #   - on récupère C[i], l'indice final après permutation,
        #   - on place dans S à cet indice la valeur A[i].
        # Ainsi, S est une liste où les valeurs de A sont redistribuées selon la permutation C.
    
    # print(S)
    # Cette ligne est commentée; elle permettrait d'afficher la liste S pour débogage.
    
    ans = sum(S[:k])
    # Calcul de la somme des k premiers éléments de S.
    # S[:k] crée un sous-ensemble de S contenant les éléments d'indice 0 à k-1.
    # La fonction sum() additionne tous ces éléments.
    # Cette somme représente une valeur partielle ou un résultat partiel dans le problème donné.
    
    tmpdif = 0
    # Initialisation de la variable tmpdif à 0.
    # Cette variable sera utilisée pour stocker une différence minimale calculée plus loin.
    
    for xx in X:
        # Pour chaque paire xx dans la liste X:
        
        if xx[0] < k and xx[1] >= k:
            # On teste si le premier élément de la paire est strictement inférieur à k
            # et simultanément si le second élément est supérieur ou égal à k.
            # Cette condition détecte des paires 'limites' par rapport au seuil k.
            
            tmpdif = min(tmpdif, S[xx[1]] - S[xx[0]])
            # On compare la valeur actuelle de tmpdif avec la différence S[xx[1]] - S[xx[0]].
            # La fonction min() retourne la plus petite des deux valeurs.
            # Si cette différence est plus petite que tmpdif (initialement 0),
            # tmpdif sera mis à jour avec cette différence.
            # tmpdif devient donc la plus petite différence négative rencontrée.
    
    print(ans + tmpdif)
    # Affiche la somme ans modifiée par tmpdif.
    # Le résultat final prend en compte la somme initiale et la meilleure correction trouvée.
    # C'est généralement la sortie attendue par le problème auquel ce code répond.