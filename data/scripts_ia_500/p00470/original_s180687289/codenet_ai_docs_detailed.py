def process_input():
    """
    Lit plusieurs paires de dimensions (w, h) depuis l'entrée standard jusqu'à ce que la paire '0 0' soit rencontrée.
    Pour chaque paire, construit une matrice spéciale et calcule une valeur basée sur cette matrice.
    Affiche le résultat pour chaque paire de dimensions donnée.
    """
    # Boucle infinie qui itère sur les entrées utilisateur, s'arrêtant quand la chaîne '0 0' est rencontrée
    for e in iter(input, '0 0'):
        # Conversion de la chaîne d'entrée en deux entiers w (largeur) et h (hauteur)
        w, h = map(int, e.split())

        # Initialisation de la matrice M de dimensions w x h
        # Chaque élément est une liste de 4 entiers: [1,0,1,0]
        # Construite via des compréhensions imbriquées:
        # Pour chaque position (i, j), on crée une liste [1,0,1,0]
        M = [[[1, 0] * 2 for _ in [0]*h] for _ in [0]*w]

        # Parcours des indices à partir de 1 jusqu'à w-1 et 1 jusqu'à h-1
        # Ces indices servent à mettre à jour les éléments de la matrice M
        for i in range(1, w):
            for j in range(1, h):
                # Récupération des deux premiers éléments de M[i-1][j], notés a et b
                a, b = M[i-1][j][:2]

                # Récupération des deux derniers éléments de M[i][j-1], notés c et d
                c, d = M[i][j-1][2:]

                # Mise à jour de M[i][j] avec une liste composée de [d, a+b, b, c+d]
                M[i][j] = [d, a+b, b, c+d]

        # Calcul du résultat final basé sur les sommes d'éléments spécifiques de M:
        # somme des deux premiers éléments de M[w-2][h-1] + somme des deux derniers éléments de M[w-1][h-2]
        # puis le résultat est modulo 100000 (10^5)
        result = (sum(M[w-2][h-1][:2]) + sum(M[w-1][h-2][2:])) % 10**5

        # Affiche le résultat calculé pour la paire (w, h)
        print(result)

# Appeler la fonction principale pour lancer le traitement
process_input()