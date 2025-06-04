# Demander à l'utilisateur de saisir un nombre entier, et convertir la chaîne de caractères obtenue en entier.
t = int(input())

# Définition d'un tuple nommé 'vec' contenant quatre paires de coordonnées.
# Chaque paire représente un déplacement (delta x, delta y) vers une des quatre directions cardinales :
# (1, 0) : droite
# (0, -1) : haut
# (-1, 0) : gauche
# (0, 1) : bas
vec = ((1, 0), (0, -1), (-1, 0), (0, 1))

# Début d'une boucle for pour traiter plusieurs cas de test.
# La variable '_' est utilisée lorsque la valeur n'est pas exploitée.
for _ in range(t):

    # Déclaration d'une fonction nommée 'check' servant à parcourir et à marquer les cellules adjacentes ayant la même couleur.
    # x, y : coordonnées de départ.
    # lst : liste où l'on stocke les coordonnées des cellules visitées appartenant à un même groupe de couleur.
    # checked : matrice indiquant l'état de chaque cellule (None: non traité, False: ignoré, True: à effacer).
    def check(x, y, lst, checked):
        # Marque la cellule de coordonnées (x, y) comme visitée en assignant False dans 'checked'.
        checked[y][x] = False
        
        # Récupère la couleur présente à la position (y, x) dans la matrice mp.
        color = mp[y][x]
        
        # Parcourt les directions cardinales définies dans 'vec'.
        for dx, dy in vec:
            # Calcule les coordonnées du voisin adjacent en ajoutant dx et dy.
            nx, ny = x + dx, y + dy
            # Vérifie si la cellule voisine a la même couleur et n'a pas encore été vérifiée (checked[ny][nx] == None).
            if color == mp[ny][nx] and checked[ny][nx] == None:
                # Ajoute les coordonnées du voisin au groupe en cours.
                lst.append((nx, ny))
                # Appelle récursivement 'check' sur le voisin afin d'étendre la recherche au groupe de cellules connectées.
                check(nx, ny, lst, checked)
    
    # Lecture de la grille du jeu avec gestion de la bordure. 
    # La grille comporte ici 12 lignes (car l'entrée attend 12 lignes utilisateur).
    # On ajoute une bordure de "X" tout autour pour simplifier la gestion des limites et éviter les erreurs d'indice.
    # Ligne du haut (remplie de "X") + 
    # Pour chaque nouvelle ligne saisie, on l'entoure de "X" à gauche et à droite +
    # Ligne du bas (remplie de "X")
    mp = [list("X" * 8)] + [list("X" + input() + "X") for _ in range(12)] + [list("X" * 8)]
    
    # Initialise le compteur d'opérations à zéro.
    cnt = 0
    
    # Boucle principale du traitement, qui s'exécutera jusqu'à ce qu'aucun groupe ne soit supprimé lors d'une itération.
    while True:
        # Création d'une nouvelle matrice 'checked' qui a les mêmes dimensions que la grille 'mp'.
        # Elle est remplie de 'None', symbolisant que chaque cellule n'a pas encore été vérifiée,
        # et sera mise à jour pendant le traitement.
        checked = [[None] * 8 for _ in range(14)]
        
        # Parcourt l'intérieur de la grille, c'est-à-dire hors bordures ; y varie de 1 à 12 (inclus), x de 1 à 6 (inclus).
        for y in range(1, 13):
            for x in range(1, 7):
                # Si la cellule contient un caractère d'obstacle ou vide ("O", ".", ou "X"),
                # on la marque comme 'False' (sans intérêt pour la suppression de groupe).
                if mp[y][x] in ("O", ".", "X"):
                    checked[y][x] = False
                # Si la cellule contient un autre caractère et n'a pas été vérifiée,
                # on cherche à lui associer un groupe de connectivité.
                elif checked[y][x] == None:
                    # Initialise une nouvelle liste contenant les coordonnées actuelles, représentant un nouveau groupe.
                    lst = [(x, y)]
                    # Appelle la fonction 'check' afin de collecter toutes les cellules voisines du même type.
                    check(x, y, lst, checked)
                    # Le groupe est désormais constitué dans 'lst'
                    length = len(lst)
                    # Si la taille du groupe est inférieure à 4, il ne sera pas supprimé : on ignore ce groupe.
                    if length < 4:
                        continue
                    # Pour les groupes de taille au moins 4, marque toutes les cellules du groupe comme 'True' dans 'checked'.
                    for nx, ny in lst:
                        checked[ny][nx] = True

        # Vérifie s'il reste au moins un groupe marqué comme devant être supprimé dans la matrice 'checked'.
        # Cela consiste à rechercher au moins un 'True' dans 'checked'.
        # Si non, la boucle principale se termine puisque plus rien n'est à supprimer.
        if not any(any(lst) for lst in checked):
            break
        
        # Traite les cellules qui contiennent un "O", c'est-à-dire les obstacles.
        # Pour chaque case "O", on regarde s'il y a à côté une case marquée pour suppression (True dans checked et différent de "O").
        # Si oui, la case "O" est également marquée à supprimer.
        for y in range(1, 13):
            for x in range(1, 7):
                if mp[y][x] == "O":
                    for dx, dy in vec:
                        nx, ny = x + dx, y + dy
                        if mp[ny][nx] != "O" and checked[ny][nx]:
                            checked[y][x] = True

        # Supprime physiquement toutes les cellules marquées comme à retirer en mettant leur case à "." (vide).
        for y in range(1, 13):
            for x in range(1, 7):
                if checked[y][x]:
                    mp[y][x] = "."
        
        # Pour chaque colonne (x de 1 à 6), on "fait tomber" les éléments vers le bas pour combler les trous laissés par les suppressions.
        for x in range(1, 7):
            # On construit une chaîne de caractères représentant la colonne de bas en haut.
            s = ""
            for y in range(12, 0, -1):
                s = mp[y][x] + s
            # On retire tous les points (".") de la chaîne ; seuls les éléments présents restent.
            s = s.replace(".", "")
            # On ajoute suffisamment de points en tête de colonne pour conserver la taille à 12 (remplir le haut avec des cases vides).
            s = "." * (12 - len(s)) + s
            # On réécrit la colonne dans la matrice 'mp', du bas vers le haut (y décroissant).
            for y in range(12, 0, -1):
                mp[y][x] = s[y - 1]
        
        # Incrémente le compteur d'opérations, chaque opération correspondant à une étape où l'on retire des groupes.
        cnt += 1
    
    # Affiche le nombre d'itérations effectuées, c'est-à-dire le nombre de vagues de suppression de groupes.
    print(cnt)