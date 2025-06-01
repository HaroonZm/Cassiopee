def s():
    """
    Traitement itératif d'entrées jusqu'à la chaîne '0 0' incluse.

    Pour chaque paire d'entiers (w, h) saisie, le programme construit une matrice 3D M de dimensions w x h,
    contenant des listes de quatre entiers par cellule. La matrice est initialisée avec une structure particulière,
    puis mise à jour selon une règle itérative parcourant les indices de 1 à w-1 et 1 à h-1.

    Enfin, pour chaque paire (w, h), le programme calcule une valeur spécifique à partir des dernières lignes/colonnes de M,
    puis affiche le résultat modulo 10^5.

    Entrée attendue :
        - Plusieurs lignes au format "w h" où w et h sont des entiers.
        - Arrêt de la lecture lorsque l'entrée est "0 0".

    Sortie :
        - Pour chaque paire (w, h) différente de "0 0", affiche un entier calculé.
    """
    for e in iter(input, '0 0'):
        # Lecture des dimensions w (largeur) et h (hauteur) à partir de la chaîne saisie
        w, h = map(int, e.split())

        # Initialisation de la matrice M de taille w x h
        # Chaque élément de M est une liste de quatre entiers initialisés sur [1,0,1,0]
        # Cette ligne crée une liste de la forme [[[1,0,1,0], ..., [1,0,1,0]], ..., [...]]
        M = [[[1, 0] * 2 for _ in range(h)] for _ in range(w)]

        # Remplissage de la matrice M selon la relation récursive définie
        for i in range(1, w):
            for j in range(1, h):
                # Extraction des valeurs précédentes nécessaires au calcul
                a, b = M[i - 1][j][:2]      # premiers deux éléments de la cellule au-dessus
                c, d = M[i][j - 1][2:]      # derniers deux éléments de la cellule à gauche

                # Calcul des quatre nouveaux éléments pour la cellule actuelle
                # On remplace M[i][j] par [d, a + b, b, c + d]
                M[i][j] = [d, a + b, b, c + d]

        # Calcul final basé sur la somme modulaire des éléments spécifiques des deux dernières lignes et colonnes
        result = (sum(M[w - 2][h - 1][:2]) + sum(M[w - 1][h - 2][2:])) % 10**5

        # Affichage du résultat
        print(result)


if __name__ == '__main__':
    s()