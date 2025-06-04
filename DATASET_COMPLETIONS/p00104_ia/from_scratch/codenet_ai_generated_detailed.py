def magic_tile():
    while True:
        # Lecture des dimensions H (hauteur) et W (largeur)
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            # Fin des jeux de données
            break

        # Lecture de la grille représentant la pièce
        room = [list(input()) for _ in range(H)]

        # Position de départ en haut à gauche (0,0)
        x, y = 0, 0

        # Ensemble pour mémoriser les positions visitées,
        # permet de détecter une boucle infinie
        visited = set()

        while True:
            # Si la position courante a déjà été visitée, c'est une boucle
            if (x, y) in visited:
                print("LOOP")
                break

            visited.add((x, y))

            tile = room[y][x]

            # Selon la flèche sur la tuile, on déplace la personne
            if tile == '>':
                x += 1
            elif tile == '<':
                x -= 1
            elif tile == '^':
                y -= 1
            elif tile == 'v':
                y += 1
            else:
                # Pas de flèche, on s'arrête et affiche la position finale
                print(x, y)
                break

# Lancement de la simulation
magic_tile()