from collections import deque  # Importation de la classe deque (file double) du module collections pour faire du parcours en largeur (BFS)

n = int(input())  # Lecture de la taille de la grille, convertie depuis une chaîne en entier, et stockée dans la variable n

# Création d'une liste de n chaînes, chaque chaîne étant une ligne de la grille, littéralement lue depuis l'entrée standard
A = [input() for i in range(n)]

cnt = 0  # Initialisation d'un compteur à 0, ce compteur sera utilisé pour compter le nombre de composantes 'o' connectées

# Définition des 4 directions cardinales (gauche, haut, droite, bas) à explorer pour le parcours en largeur
dd = [[-1, 0], [0, -1], [1, 0], [0, 1]]

used = {}  # Dictionnaire vide utilisé pour mémoriser les cellules déjà visitées afin d'éviter de les revisiter

# Première boucle (par lignes) allant de 0 à n-1 : i représente l'indice de la ligne
for i in range(n):
    # Seconde boucle (par colonnes) allant de 0 à n-1 : j représente l'indice de la colonne
    for j in range(n):
        # Vérifie si la cellule à la position (i, j) contient le caractère 'x'
        # ou si cette position a déjà été visitée (présente dans used)
        # Si l'une des conditions est vraie, on saute tout le reste du bloc et passe à la prochaine itération
        if A[i][j] == 'x' or (i, j) in used:
            continue  # Passage à la prochaine cellule sans faire la suite

        # Sinon, cette cellule est une nouvelle composante de 'o' non encore explorée
        # On initialise ici une nouvelle file (deque) pour un parcours en largeur
        # On met dans la file un tuple de coordonnées (j, i)
        deq = deque([(j, i)])

        # On marque la cellule (i, j) comme visitée dans le dictionnaire used en mettant n'importe quelle valeur (ici 1)
        used[i, j] = 1

        # On incrémente le compteur cnt, car on vient d'en trouver une nouvelle composante
        cnt += 1

        # On commence ici le parcours en largeur classique
        # Tant que la file n'est pas vide, on effectue les instructions suivantes
        while deq:
            # On enlève et retourne le premier élément de la file (FIFO) : ce sont les coordonnées x, y à traiter
            x, y = deq.popleft()

            # Parcours des 4 directions possibles grâce à la liste dd, chaque élément étant un déplacement (dx, dy)
            for dx, dy in dd:
                nx = x + dx  # Calcul de la nouvelle abscisse en ajoutant l'incrément dx
                ny = y + dy  # Calcul de la nouvelle ordonnée en ajoutant l'incrément dy

                # Vérifie que les nouvelles coordonnées (nx, ny) restent bien à l'intérieur de la grille (indices de 0 à n-1)
                if 0 <= nx < n and 0 <= ny < n:
                    # Vérifie que la cellule (ny, nx) contient un 'o' (on cherche à étendre la composante)
                    # et que cette cellule n'a pas encore été visitée
                    if A[ny][nx] == 'o' and (ny, nx) not in used:
                        # On marque la cellule (ny, nx) comme visitée dans le dictionnaire used
                        used[ny, nx] = 1
                        # On ajoute cette nouvelle cellule à la file pour exploration ultérieure
                        deq.append((nx, ny))

# Après avoir exploré toute la grille et compté toutes les composantes 'o', on affiche le résultat
# La division entière (//) par 3 est faite pour obtenir le résultat demandé
print(cnt // 3)  # Affichage du résultat final, cnt divisé par 3 avec troncature des décimales