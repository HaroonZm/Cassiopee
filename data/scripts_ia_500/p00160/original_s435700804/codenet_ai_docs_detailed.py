def calculate_points():
    """
    Fonction principale qui lit des séries de données depuis l'entrée standard,
    calcule un score en fonction de critères spécifiques, et affiche ce score.
    Le processus se répète jusqu'à ce que l'entrée '0' soit fournie.

    Pour chaque série :
        - Lit un entier n indiquant le nombre de lignes suivantes à traiter.
        - Si n est 0, la fonction termine.
        - Pour chaque ligne suivante, lit quatre entiers : x, y, h, w.
          Calcule la somme x + y + h pour une variable temporaire.
          En fonction de cette somme et de la valeur de w, incrémente un compteur v selon les règles définies.
        - Affiche le score total v pour la série.
    """

    while True:
        # Lecture du nombre d'entrées pour la série courante et initialisation du score
        n, v = int(input()), 0

        # Si n est 0, on arrête la boucle (fin du programme)
        if n == 0:
            break

        # Boucle sur chaque ligne de données
        for _ in range(n):
            # Lecture des quatre entiers x, y, h, w
            x, y, h, w = map(int, input().split())

            # Calcul de la somme surrogate
            x = x + y + h

            # Attribution des points en fonction des intervalles de x et w
            if x < 61 and w < 3:
                v += 600
            elif x < 81 and w < 6:
                v += 800
            elif x < 101 and w < 11:
                v += 1000
            elif x < 121 and w < 16:
                v += 1200
            elif x < 141 and w < 21:
                v += 1400
            elif x < 161 and w < 26:
                v += 1600

        # Affichage du score total pour la série
        print(v)

# Appel de la fonction principale
calculate_points()