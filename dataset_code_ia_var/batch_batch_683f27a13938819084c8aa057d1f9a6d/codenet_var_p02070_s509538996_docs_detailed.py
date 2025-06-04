def gcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b
    en utilisant l'algorithme d'Euclide.

    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Returns:
        int: Le PGCD de a et b.
    """
    # Si b est plus grand que a, on échange leurs places
    if b > a:
        return gcd(b, a)
    # Si b est nul, le PGCD est a
    if b == 0:
        return a
    # Appel récursif avec b et le reste de a divisé par b
    return gcd(b, a % b)

def extgcd(a, b):
    """
    Calcule le couple (x, y) tel que a*x + b*y = pgcd(a, b) en utilisant
    l'algorithme d'Euclide étendu. Ici, on s'arrête dès que le reste est 1.

    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Returns:
        tuple: Un tuple (x, y) tel que a*x + b*y = 1.
    """
    # Initialisation des coefficients de Bezout
    r = [1, 0, a]  # [coefficient pour a, coefficient pour b, valeur courante]
    w = [0, 1, b]  # [coefficient pour a, coefficient pour b, valeur courante]
    # Itère jusqu'à ce que w[2] == 1
    while w[2] != 1:
        # Calcul du quotient entier de la division
        q = r[2] // w[2]
        # Mise à jour des coefficients et des restes
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    # Retourne les coefficients (x, y)
    return w[0], w[1]

def main():
    """
    Fonction principale qui résout un problème de système d'équations de type
    permutation-composition et recherche de cycle en utilisant le PGCD,
    l'algorithme d'Euclide étendu et des techniques de dynamiques.

    Lit les entrées depuis stdin :
        - n : taille des permutations
        - p : permutation de 1 à n
        - q : permutation associée

    Affiche la réponse selon les contraintes du problème.
    """
    # Lecture de la taille n
    n = int(input())
    # Lecture de la permutation p
    p = list(map(int, input().split()))
    # Lecture de la permutation q
    q = list(map(int, input().split()))

    # Préparation d'une table pour la dynamique.
    # dp[i][j] : point d'arrivée après avoir appliqué j fois la permutation q à i
    # dp[0][*] n'est pas utilisé car les élts commencent à l'indice 1 pour cohérence avec la logique
    dp = [[0] * 401 for _ in range(201)]  # Assez pour indexer n et pour itérer jusqu'à 400 fois

    # Initialisation pour chaque élément du tableau
    for i in range(1, n + 1):
        dp[i][0] = i  # 0 composition: reste à sa place
        dp[i][1] = q[i - 1]  # 1 composition: saute à la valeur de q

    # Remplissage de la table dynamique sur 2 à 400 itérations
    for j in range(2, 401):
        for i in range(1, n + 1):
            # La destination après j compositions est la destination de la précédente
            dp[i][j] = dp[dp[i][j - 1]][1]

    # Liste pour stocker pour chaque i : [ai, bi]
    # ai = ordre de pi dans son cycle de q (profondeur du cycle)
    # bi = nombre de fois qu'il faut appliquer q pour aller de pi à i+1
    ab = [[0, 0] for _ in range(n)]

    # Pour chaque élément du tableau p
    for i in range(n):
        pi = p[i]
        bi = -1
        # Recherche du nombre minimal d'applications de q pour passer de pi à i+1
        for b in range(401):
            if dp[pi][b] == i + 1:
                bi = b
                break
        # Impossible d'atteindre, fin du programme
        if bi == -1:
            print(-1)
            exit()

        ai = -1
        # Recherche de l'ordre du cycle de pi sous q
        for a in range(1, 401):
            if dp[pi][a] == pi:
                ai = a
                break
        # Enregistrement des valeurs trouvées
        ab[i] = [ai, bi]

    # Calcul du point commun pour tous les éléments via le théorème des restes chinois
    tmp_a = ab[0][0]  # Première période (ordre du cycle)
    tmp_b = ab[0][1]  # Première position pour s'aligner
    # Pour chaque autres éléments
    for i in range(1, n):
        A = tmp_a
        B = ab[i][0]
        C = ab[i][1] - tmp_b  # Décalage de la solution courante au nouvel alignement

        # Calcul du PGCD de A et B
        G = gcd(A, B)
        # Si pas de solution, sortie immédiate
        if C % G != 0:
            print(-1)
            exit()
        # Coefficients de Bezout pour la combinaison linéaire
        K1, K2 = extgcd(A // G, B // G)
        # Nouvelle période : PPCM de A et B
        tmp_a = G * (A // G) * (B // G)
        # Mise à l'échelle du coefficient pour s'aligner sur la solution particulière
        K1 *= C // G
        # Mise à jour du point d'alignement
        tmp_b = A * K1 + tmp_b
        # On ramène tmp_b dans l'intervalle [0, tmp_a)
        tmp_b = (tmp_b % tmp_a + tmp_a) % tmp_a
    # Affichage du résultat final (nombre minimal recherché)
    print(tmp_b)

if __name__ == "__main__":
    main()