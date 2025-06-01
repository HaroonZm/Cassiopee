def process_pairs():
    """
    Lit des paires de dimensions (w, h) depuis l'entrée standard, jusqu'à ce que la paire '0 0' soit rencontrée.
    Pour chaque paire, construit une matrice M en 3D avec une structure spécifique,
    effectue des calculs basés sur les valeurs adjacentes de la matrice,
    puis affiche un résultat calculé modulo 100000.

    Entrée attendue : une série de lignes contenant deux entiers séparés par un espace,
    représentant les dimensions w (largeur) et h (hauteur).
    La lecture s'arrête lorsque la paire '0 0' est entrée.

    Pour chaque paire non nulle :
    - Initialise une matrice M de taille w x h, où chaque élément est une liste de 4 entiers.
    - Met à jour les éléments de la matrice à partir des indices 1 dans chaque dimension,
      en combinant les valeurs de voisins immédiats selon une règle donnée.
    - Calcule un résultat à partir des bords de la matrice et affiche ce résultat modulo 100000.

    Exemple d'entrée :
    3 3
    0 0

    Exemple de sortie :
    4

    (Le chiffre dépend du calcul effectué par la matrice)
    """
    # Lecture des lignes jusqu'à ce que '0 0' soit rencontré
    for e in iter(input, '0 0'):

        # Conversion de la ligne d'entrée en deux entiers : largeur (w) et hauteur (h)
        w, h = map(int, e.split())

        # Initialisation de la matrice 3D M de dimensions w x h
        # Chaque élément est une liste de 4 entiers initialisée à [1, 0, 1, 0]
        # La syntaxe [1,0]*2 crée [1,0,1,0]
        M = [[[1, 0] * 2 for _ in range(h)] for _ in range(w)]

        # Parcours des indices à partir de 1 pour w et h, afin d'éviter les bords (indices 0)
        for i in range(1, w):
            for j in range(1, h):

                # Extraction des quatre valeurs nécessaires depuis les éléments voisins
                # a, b : les deux premiers éléments de l'élément à gauche (i-1, j)
                # c, d : les deux derniers éléments de l'élément en-dessous (i, j-1)
                a, b = M[i - 1][j][:2]
                c, d = M[i][j - 1][2:]

                # Mise à jour de l'élément courant (i, j) avec une nouvelle liste de 4 valeurs
                # La logique est : [d, a + b, b, c + d]
                M[i][j] = [d, a + b, b, c + d]

        # Calcul final :
        # Somme des deux premiers éléments de l'élément en position (w-2, h-1)
        # plus la somme des deux derniers éléments de l'élément en position (w-1, h-2)
        # Le tout modulo 100000
        result = (sum(M[w - 2][h - 1][:2]) + sum(M[w - 1][h - 2][2:])) % 100000

        # Affichage du résultat calculé pour la paire (w, h)
        print(result)

# Appel de la fonction principale pour exécuter le programme
process_pairs()