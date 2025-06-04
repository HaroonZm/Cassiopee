dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Directions: left, up, right, down

while True:
    # Lire les dimensions de la grille (n lignes, m colonnes)
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        # Condition d'arrêt: si les deux valeurs sont nulles, sortir de la boucle
        break

    # Construction de la grille C:
    # - Chaque ligne saisie est convertie en liste de caractères, un '#' est ajouté à la fin pour faciliter la gestion des bords.
    # - Une ligne supplémentaire remplie de '#' est ajoutée en bas pour fermer la grille.
    C = [list(input() + "#") for _ in range(n)] + ["#" * (m + 2)]

    # Matrice pour marquer les cases visitées (non utilisée dans la logique mais définie)
    used = [[0] * m for _ in range(n)]

    def move(x0, y0, x1, y1, d):
        """
        Tente de déplacer un 'robot' suivant la règle du mur à gauche,
        de la case (x0, y0) à la case (x1, y1) dans la direction initiale d.

        Parameters:
            x0, y0 (int): Point de départ (en coordonnées colonne, ligne)
            x1, y1 (int): Point d'arrivée cible
            d (int): Direction de départ (0=left, 1=up, 2=right, 3=down)

        Returns:
            int: 1 si le déplacement est possible dans le contexte demandé, 0 sinon

        Comportement:
            - Le robot suit la règle du mur à gauche 
            - Le parcours est enregistré, et les cases (sauf l'arrivée) sont bloquées pour les autres parcours.
            - Si le robot revient à sa position initiale sans avoir quitté ou tourne en boucle, retourne 0.
        """
        x = x0  # Position courante (colonne)
        y = y0  # Position courante (ligne)
        moved = 0  # Indique si un déplacement effectif a eu lieu
        cnt = 0    # Nombre de tours pour éviter les boucles infinies
        history = []  # Historique des cases traversées

        while x != x1 or y != y1:
            cnt += 1
            # Calcul de la direction "gauche" et de la direction "avant"
            rx, ry = dd[d - 3]   # d-3 équivaut à tourner à gauche
            dx, dy = dd[d]       # direction actuelle (avant)
            # Si devant c'est libre et à gauche c'est bloqué, avancer
            while C[y + dy][x + dx] != '#' and C[y + ry][x + rx] == '#':
                x += dx
                y += dy
                history.append([x, y])
                moved = 1
            # Si devant c'est bloqué et à gauche c'est bloqué, tourner à gauche
            if C[y + dy][x + dx] == '#' and C[y + ry][x + rx] == '#':
                d = (d - 1) % 4
            # Si à gauche c'est libre, tourner à droite et avancer à gauche
            elif C[y + ry][x + rx] != '#':
                d = (d + 1) % 4
                x += rx
                y += ry
                history.append([x, y])
            # Si on boucle sur la case de départ sans avoir avancé ou trop de tours, retour 0
            if (moved or cnt > 4) and x == x0 and y == y0:
                return 0

        # Bloque tous les points du trajet (sauf l'arrivée) pour les autres parcours
        for hx, hy in history[:-1]:
            C[hy][hx] = '#'
        return 1

    # Tente de faire le tour complet dans le sens horaire, chaque mot "move" représente un segment du périmètre
    if (
        move(0, 0, 0, n - 1, 3) and                  # De (0,0) vers (0,n-1) en bas
        move(0, n - 1, m - 1, n - 1, 2) and          # De (0,n-1) vers (m-1,n-1) à droite
        move(m - 1, n - 1, m - 1, 0, 1) and          # De (m-1,n-1) vers (m-1,0) en haut
        move(m - 1, 0, 0, 0, 0)                      # De (m-1,0) vers (0,0) à gauche
    ):
        print("YES")
    else:
        print("NO")