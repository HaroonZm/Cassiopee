# Version débutant : code plus simple, explicite, indentation basique, noms de variables plus parlants

num_cases = int(input())
for case_num in range(num_cases):
    if case_num > 0:
        # Ligne vide entre les cas de test (équivalent à 'print' vide en Python2)
        print()
    # Lecture des dimensions de la carte
    ligne = input()
    h_w = ligne.split()
    H = int(h_w[0])
    W = int(h_w[1])
    
    # Lecture de la carte caractère par caractère
    grille = []
    for i in range(H):
        ligne = input()
        grille.append(list(ligne))
    
    # Trouver la position initiale du tank et sa direction
    for ligne in range(H):
        for colonne in range(W):
            if grille[ligne][colonne] in "^<v>":
                pos_x = colonne
                pos_y = ligne
                direction = grille[ligne][colonne]
                grille[ligne][colonne] = "."
    
    # On ignore la longueur de la commande (lecture pour vider la ligne)
    input()
    commandes = input()
    
    # Exécution des commandes
    for cmd in commandes:
        if cmd == "S":
            # Tirer dans la direction actuelle
            if direction == "^":
                i = pos_y - 1
                while i >= 0:
                    if grille[i][pos_x] == "*":
                        grille[i][pos_x] = "."
                        break
                    if grille[i][pos_x] == "#":
                        break
                    i -= 1
            elif direction == "<":
                i = pos_x - 1
                while i >= 0:
                    if grille[pos_y][i] == "*":
                        grille[pos_y][i] = "."
                        break
                    if grille[pos_y][i] == "#":
                        break
                    i -= 1
            elif direction == "v":
                i = pos_y + 1
                while i < H:
                    if grille[i][pos_x] == "*":
                        grille[i][pos_x] = "."
                        break
                    if grille[i][pos_x] == "#":
                        break
                    i += 1
            elif direction == ">":
                i = pos_x + 1
                while i < W:
                    if grille[pos_y][i] == "*":
                        grille[pos_y][i] = "."
                        break
                    if grille[pos_y][i] == "#":
                        break
                    i += 1
        elif cmd == "U":
            direction = "^"
            if pos_y - 1 >= 0 and grille[pos_y - 1][pos_x] == ".":
                pos_y = pos_y - 1
        elif cmd == "L":
            direction = "<"
            if pos_x - 1 >= 0 and grille[pos_y][pos_x - 1] == ".":
                pos_x = pos_x - 1
        elif cmd == "D":
            direction = "v"
            if pos_y + 1 < H and grille[pos_y + 1][pos_x] == ".":
                pos_y = pos_y + 1
        elif cmd == "R":
            direction = ">"
            if pos_x + 1 < W and grille[pos_y][pos_x + 1] == ".":
                pos_x = pos_x + 1
    
    # Remettre le tank à sa position finale sur la carte
    grille[pos_y][pos_x] = direction
    
    # Afficher la carte
    for ligne in grille:
        print("".join(ligne))