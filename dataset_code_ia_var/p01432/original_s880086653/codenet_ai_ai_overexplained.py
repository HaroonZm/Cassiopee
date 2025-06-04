import sys  # Importer le module système pour accéder aux entrées et sorties standards

# Raccourcis pour lecture et écriture sur les flux standards (clavier et écran)
readline = sys.stdin.readline   # Fonction pour lire une ligne de l'entrée standard (clavier, ou redirection)
write = sys.stdout.write        # Fonction pour écrire sur la sortie standard (écran, ou redirection de fichier)

# Fonction pour multiplier deux matrices carrées A et B (A = n x n, B = n x n)
# Résultat stocké dans la matrice C
def mul(n, A, B, C):
    # Parcours des lignes de la matrice résultat
    for i in range(n):
        # Parcours des colonnes de la matrice résultat
        for j in range(n):
            # Calcul de l'élément C_{i,j} comme la somme du produit des éléments correspondants sur l'index k
            # Attention, A[i][k] * A[k][j] utilise A deux fois ici, pas B, donc la multiplication n'est pas générique
            C[i][j] = sum(A[i][k] * A[k][j] for k in range(n))

# Fonction pour calculer la puissance rapide d'une matrice 'MA' appliquée à un vecteur 'A' sur 'k' itérations
# n : dimension de la matrice/vecteur
# MA : matrice carrée de dimension n x n (sera élevée à la puissance k)
# A : vecteur ligne de taille n (état initial)
# k : exposant
# Retourne le vecteur après application de la matrice k fois
def fast_pow(n, MA, A, k):
    # Création d'une matrice temporaire (place mémoire pour stocker résultats intermédiaires)
    R = [[0]*n for i in range(n)]
    # Tant que l'exposant k n'est pas nul, on continue
    while k:
        # Si le bit le moins significatif de k est à 1 (k impair), on applique une multiplication supplémentaire au résultat
        if k & 1:
            # Appliquer la matrice MA au vecteur A : pour chaque ligne i, faire le produit scalaire de la ligne MA[i] avec le vecteur A
            A = [sum(e*a for e, a in zip(MA[i], A)) for i in range(n)]
        # Calculer MA * MA et stocker le résultat dans R (carré de la matrice pour exponentiation rapide)
        mul(n, MA, MA, R)
        # Échanger les matrices MA et R pour affecter le carré à MA pour le prochain tour
        MA, R = R, MA
        # Décaler k d'un bit vers la droite (division entière par 2), progression de l'exponentiation binaire
        k >>= 1
    # Retourne le vecteur résultat après avoir appliqué la matrice k fois
    return A

# Fonction principale pour résoudre le problème
def solve():
    # Lecture d'une ligne, découpage sur les espaces, conversion en entiers
    S, N, K = map(int, readline().split())
    S = abs(S)  # On utilise toujours la valeur absolue de S (distance positive)

    # Si la cible est à la position 0 (pas de déplacement nécessaire)
    if S == 0:
        write("0\n")  # Écrire zéro mouvements nécessaires
        return        # On quitte la fonction

    # Si on a qu'une seule valeur possible à chaque étape (N == 1)
    if N == 1:
        # Si S n'est pas divisible par K, il n'est pas possible d'atteindre S exactement avec ces pas
        if S % K:
            write("-1\n")  # Impossible d'atteindre S
        else:
            # Sinon, on affiche le nombre minimum d'étapes
            write("%.16f\n" % (S // K))  # Format flottant sur 16 décimales (demande du problème)
        return   # Sortir après avoir traité ce cas particulier

    # Calcul d'une variable d'état : nombre de positions possibles dans la DP
    M = N * K    # Valeur maximum atteignable sur K étapes de N valeurs

    # Table de programmation dynamique (DP) pour compter les façons d'atteindre chaque somme possible
    dp = [0] * (M + 1)  # On va de 0 à M inclus
    dp[0] = 1           # Il n'y a qu'une seule façon de faire une somme nulle (en ne prenant rien)

    # Remplissage de dp : On fait K transitions de type "faire un pas de 1 à N"
    for t in range(K):
        # On parcourt à l'envers pour ne pas utiliser de valeurs fraîchement modifiées
        for i in range(N*K, -1, -1):
            # Pour chaque somme i, calculer le nombre de façons d'y arriver en prenant un dernier pas de 1 à N
            dp[i] = sum(dp[i-k] for k in range(1, N+1) if i >= k)

    # Calcul du nombre total de séquences (le dénominateur après K transitions)
    s = sum(dp)

    # Construction de la matrice des coefficients pour un système linéaire
    mat = [[0] * (M + 2) for i in range(M + 1)] # Matrice de taille (M+1) lignes et (M+2) colonnes

    mat[0][0] = 1 # Première équation : point de départ

    # Construction pas à pas du système d'équations linéaires
    for i in range(1, M + 1):
        mi = mat[i]  # Raccourci vers la i-ème ligne
        # Pour chaque somme possible j, calculer le coeff pour la transition abs(i-j)
        for j in range(M + 1):
            mi[abs(i-j)] -= dp[j]
        # Ajuster le coefficient pour la variable inconnue courante
        mi[i] += s
        # Normalisation de la ligne : division par s (pour obtenir des probabilités)
        for j in range(M + 1):
            mi[j] /= s
        # Met à 1 la colonne de droite (valeur indépendante)
        mi[M + 1] = 1

    # Rendre la matrice triangulaire supérieure (méthode du pivot de Gauss)
    for i in range(M + 1):
        v = mat[i][i]   # Diagonale principale
        # Normalisation de la ligne courante pour mettre 1 sur la diagonale
        for j in range(M + 2):
            mat[i][j] /= v
        # Élimination des variables dans les autres lignes pour rendre tout sauf la diagonale à zéro
        for k in range(M + 1):
            if k == i:
                continue
            e = mat[k][i]
            for j in range(M + 2):
                mat[k][j] -= e * mat[i][j]

    # Extrait la solution du système (colonne indépendante)
    C = [mat[i][M + 1] for i in range(M, -1, -1)]
    C[-1] = 1   # Fixe la dernière valeur à 1 pour respecter la convention du problème

    # Si S peut être atteint avec les valeurs calculées par DP, répondre directement
    if S <= M:
        write("%.16f\n" % C[M - S])  # On affiche la solution au format requis
        return

    # Cas général : il faut utiliser la puissance matricielle pour extrapoler l'espérance à des valeurs plus grandes de S

    # Construction d'une matrice de transition pour simuler l'évolution des états au-delà de M
    mat2 = [[0] * (M + 1) for i in range(M + 1)]

    # Première ligne de la matrice de transition : calcul des probabilités de transition
    for i in range(M):
        mat2[0][i] = dp[i + 1] / s   # Probabilité de passer de l'état courant à l'état i+1

    # Remplissage des transitions d'états "shift à droite" (simule le déplacement du point C)
    for i in range(M - 1):
        mat2[i + 1][i] = 1  # Passage de l'état i à l'état i+1

    # Bouclage pour garder l'état constant au-delà de M (état absorbant)
    mat2[0][M] = mat2[M][M] = 1

    # Applique la puissance matricielle pour simuler S-M transitions à partir de la position de base
    C1 = fast_pow(M + 1, mat2, C, S - M)

    # Affiche le résultat final : espérance pour atteindre S à partir de 0
    write("%.16f\n" % C1[0])

# Appelle la fonction principale pour exécution
solve()