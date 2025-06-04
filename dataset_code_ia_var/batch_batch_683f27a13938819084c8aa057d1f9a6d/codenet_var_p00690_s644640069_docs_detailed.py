def combi(k, a, w):
    """
    Recherche récursive pour trouver le chemin le plus long sur le réseau ferroviaire,
    sans réutiliser deux fois la même voie ferrée.

    Paramètres :
        k (int) : Indice courant dans le tableau temporaire 'tmp' qui stocke le chemin.
        a (int) : Gare actuelle.
        w (int) : Longueur totale actuelle du chemin parcouru.

    Variables globales utilisées :
        len (int) : Longueur maximale du chemin trouvé jusque-là.
        ans (list) : Liste des gares correspondant au chemin le plus long.
        tbl (list) : Liste des voies ferrées sous forme de [gare1, gare2, longueur].
        f (list) : Liste de booléens indiquant si une voie a déjà été utilisée.
        n (int) : Nombre de gares.
        m (int) : Nombre de voies ferrées.
        tmp (list) : Chemin temporaire courant.
    """
    global len, ans
    # Boucle sur toutes les gares possibles pour chercher un prolongement du chemin
    for b in range(1, n + 1):
        if b == a:
            # Ne pas revenir à la même gare dans cette étape
            continue
        # Parcourt toutes les voies du réseau
        for i in range(m):
            # Si la voie n'est pas utilisée et relie a et b
            if not f[i] and ((tbl[i][0] == a and tbl[i][1] == b) or
                             (tbl[i][0] == b and tbl[i][1] == a)):
                # Marque la voie comme utilisée
                f[i] = 1
                # Ajoute la gare courante au chemin temporaire
                tmp[k] = b
                # Appel récursif pour continuer le chemin
                combi(k + 1, b, w + tbl[i][2])
                # Défait la marque pour permettre d'autres recherches (backtracking)
                f[i] = 0
    # Met à jour le chemin maximum si le chemin courant est plus long
    if w > len:
        len = w
        ans = tmp[:k]


def main():
    """
    Point d'entrée principal du programme.
    Lit les données du problème, puis effectue la recherche du chemin le plus long pour chaque instance.

    Pour chaque jeu de données, le programme lit :
        - n : Nombre de gares.
        - m : Nombre de voies ferrées.
        - m lignes décrivant chaque voie : gare1 gare2 longueur

    Pour chaque instance, affiche :
        - La longueur maximale trouvée
        - La séquence des gares du chemin le plus long
    """
    import sys

    # Préparation des tableaux pour stocker temporairement les résultats et le chemin courant
    global tbl, f, n, m, len, ans, tmp
    ans, tmp = [0] * 12, [0] * 12

    while True:
        # Lit le nombre de gares et de voies ferrées
        try:
            n, m = map(int, sys.stdin.readline().split())
        except ValueError:
            break  # En cas de ligne vide/fichier terminé
        if n == 0:
            break  # Fin de l'entrée

        # Lit la description des voies : [gare1, gare2, longueur] pour chaque voie
        tbl = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
        f = [0] * m  # Tableau de marquage pour les voies utilisées
        len = 0      # Longueur maximale du chemin trouvé
        ans = []     # Initialisation du chemin optimal

        # Cherche le chemin le plus long en partant de chaque couple de gares connecté
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a == b:
                    continue
                for i in range(m):
                    # Vérifie s'il existe une voie non utilisée entre a et b
                    if not f[i] and ((tbl[i][0] == a and tbl[i][1] == b) or
                                     (tbl[i][0] == b and tbl[i][1] == a)):
                        f[i] = 1
                        tmp[0], tmp[1] = a, b  # Démarre le chemin temporaire
                        combi(2, b, tbl[i][2])  # Débute la recherche récursive
                        f[i] = 0

        # Affichage du résultat
        print(len)
        print(*ans)

if __name__ == '__main__':
    main()