def submit():
    # Lire deux entiers depuis une seule ligne d'entrée standard; ces deux entiers sont séparés par un espace.
    # map(int, input().split()) :
    # - input() lit une ligne saisie par l'utilisateur (ex: "5 3")
    # - split() coupe cette ligne en éléments de texte selon les espaces (ex: ["5", "3"])
    # - map(int, ...) convertit chaque élément du tableau obtenu en un entier (ex: [5, 3])
    # Ici, on assigne ces deux entiers à n et k respectivement
    n, k = map(int, input().split())

    # Lire n entiers représentant une séquence de nombres (souvent appelée a ou un tableau)
    # De façon similaire à la ligne précédente:
    # - input().split() lit des nombres séparés par espaces
    # - map(int, ...) transforme chaque chaîne en int
    # - list(...) convertit l'objet de type map en une liste d'entiers python
    # Cela veut dire qu'après cette ligne, a = [a_1, a_2, ..., a_n] avec n éléments
    a = list(map(int, input().split()))

    # Définir une constante modp égale à 10**9 + 7. Ce nombre premier est couramment utilisé dans la programmation compétitive
    # pour éviter les débordements d'entiers, notamment lors des calculs avec de grands nombres.
    modp = 10 ** 9 + 7

    # Initialiser un tableau 2D dp avec n+1 lignes et k+1 colonnes. 
    # Chaque valeur est initialisée à 0.
    # dp[i][j] va représenter le nombre de façons de distribuer j bonbons parmi les i premiers enfants
    # La compréhension de liste crée d'abord une ligne [0, 0, ..., 0] (k+1 zéros) puis la duplique (n+1) fois pour les lignes.
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Remplissage des cas où l'on distribue 0 bonbon parmi n'importe quel nombre d'enfants (càd j=0).
    # Pour tout i de 0 à n (inclus), il n'y a qu'une seule façon de ne rien distribuer (ne rien donner à personne).
    for i in range(n + 1):  # i varie de 0 à n inclus
        dp[i][0] = 1

    # Boucles imbriquées pour remplir le tableau dp en calculant le nombre de façons pour chaque nombre d'enfants et de bonbons.
    # Parcourir chaque enfant (de 0 à n-1) [l'indice i représente le i-ème enfant]
    for i in range(n):
        # Parcourir chaque nombre possible de bonbons à distribuer (de 1 à k inclus).
        for j in range(1, k + 1):
            # On calcule dp[i+1][j] en utilisant la programmation dynamique et une technique d'optimisation par somme cumulée.
            # On regarde combien de façons il y a de distribuer j bonbons aux i+1 premiers enfants.
            
            # Vérifier si on peut soustraire dp[i][j-1-a[i]] sans déborder à gauche (c'est-à-dire si l'index reste >=0)
            if j - 1 - a[i] >= 0:
                # Il y a assez de bonbons pour que l'enfant courant prenne jusqu'à a[i]; on enlève le surplus.
                # La formule correspond à une inclusion-exclusion, et utilise la contribution du préfixe pour accélérer les calculs.
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j - 1] - dp[i][j - 1 - a[i]]
            else:
                # Si on ne peut pas soustraire parce que l'indice serait négatif, on ne retire rien.
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j - 1]

            # Prendre le reste modulo modp pour éviter les grands nombres négatifs ou positifs.
            # Cela s'assure que la valeur reste dans l'intervalle [0, modp-1].
            dp[i + 1][j] %= modp

    # Afficher le nombre total de façons de distribuer k bonbons à n enfants (avec les contraintes données), ce qui
    # correspond à la valeur finale calculée dans dp[n][k].
    print(dp[n][k])

# Appeler la fonction submit pour commencer le programme.
submit()