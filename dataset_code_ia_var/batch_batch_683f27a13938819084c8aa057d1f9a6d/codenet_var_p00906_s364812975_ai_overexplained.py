def mul(A, B, N, M):
    # Cette fonction réalise la multiplication matricielle
    # de deux matrices carrées A et B de taille N x N,
    # avec tous les calculs faits modulo M.
    # Résultat : retourne la matrice produit de taille N x N.
    
    # Création d'une nouvelle matrice 'result' initialisée
    # à zéro. On utilise une liste en compréhension pour
    # générer N listes contenant N zéros chacune.
    result = [[0]*N for i in range(N)]
    
    # Parcours de chaque ligne de la première matrice A.
    for i in range(N):
        # Parcours de chaque colonne de la deuxième matrice B.
        for j in range(N):
            # Variable temporaire pour accumuler la somme des produits.
            tmp = 0
            # Parcours de chaque élément de la ligne i (A)
            # et de la colonne j (B).
            for k in range(N):
                # Multiplication de l'élément de la ligne i et colonne k de A
                # avec l'élément de la ligne k et colonne j de B.
                tmp += A[i][k] * B[k][j]
                # Prise du modulo à chaque addition pour éviter
                # les débordements et garantir le résultat modulo M.
                tmp %= M
            # Affectation du résultat dans la case correspondante.
            result[i][j] = tmp
    # Retour de la matrice résultat.
    return result

# Boucle infinie afin de traiter plusieurs ensembles d'entrées successives.
while 1:
    # Lecture et décomposition de l'entrée standard.
    # On lit une ligne de chiffres séparés, on les convertit tous en entiers,
    # et on les affecte aux variables N, M, A, B, C, T dans cet ordre.
    N, M, A, B, C, T = map(int, input().split())
    
    # Condition d'arrêt de la boucle : si la taille N vaut 0,
    # on sort de la boucle ; sinon, on continue à traiter.
    if N == 0:
        break
    
    # Lecture d'une nouvelle ligne contenant N entiers.
    # On utilise l'opérateur étoile '*' pour unpack la séquence produite
    # par map(int, ...) directement dans la liste S.
    *S, = map(int, input().split())
    
    # Construction de la matrice N x N nommée 'P', initialisée à zéro.
    # Encore une fois, on utilise une liste en compréhension.
    P = [[0]*N for i in range(N)]
    
    # Remplissage de la diagonale principale de P avec la valeur B.
    # Cela signifie que pour tout i, P[i][i] reçoit la valeur B.
    for i in range(N):
        P[i][i] = B
    
    # Remplissage des éléments diagonaux supérieurs et inférieurs proches :
    # Les éléments directement sous la diagonale principale reçoivent A
    # (P[i+1][i]) et les éléments directement au-dessus reçoivent C (P[i][i+1]).
    for i in range(N-1):
        P[i+1][i] = A  # Sous-diagonale
        P[i][i+1] = C  # Sur-diagonale
    
    # Création de la matrice identité 'base' de dimension N x N.
    # Tous les éléments sont initialisés à zéro puis les éléments de
    # la diagonale principale sont mis à 1.
    base = [[0]*N for i in range(N)]
    for i in range(N):
        base[i][i] = 1  # Affectation du 1 sur la diagonale principale
    
    # Algorithme d'exponentiation rapide de matrices :
    # On veut calculer P^T (matrice P à la puissance T) modulo M.
    # On commence à T et on réduit de moitié à chaque itération.
    while T:
        # Si le bit de poids faible de T est à 1 (T impair),
        # on multiplie la base courante par la matrice P courante et
        # on met à jour base en conséquence.
        if T & 1:
            base = mul(base, P, N, M)
        # On élève la matrice P au carré pour passer à la puissance suivante.
        P = mul(P, P, N, M)
        # Décalage à droite de T d’un bit (équivalent à division entière par 2).
        T >>= 1
    
    # Calcul du produit de la matrice base finale par le vecteur S,
    # pour obtenir le vecteur final U.
    U = [0]*N  # Initialisation du vecteur U à N zéros.
    for i in range(N):
        tmp = 0  # Variable temporaire d'accumulation par ligne.
        for j in range(N):
            # Multiplication de l’élément (i, j) de base par le jème élément de S,
            # accumulation, et réduction modulo M à chaque addition.
            tmp += base[i][j] * S[j]
            tmp %= M
        U[i] = tmp  # Affectation du résultat pour la ième composante.
    
    # Affichage de tous les éléments de U séparés par des espaces,
    # pour former le résultat final de cette entrée.
    print(*U)