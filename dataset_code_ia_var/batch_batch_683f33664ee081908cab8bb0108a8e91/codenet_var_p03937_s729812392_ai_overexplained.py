# Demander à l'utilisateur d'entrer deux entiers séparés par un espace, qui désigneront la hauteur (h) et la largeur (w) de la grille
h, w = (int(i) for i in input().split())  # Utilisation d'une expression génératrice pour convertir chaque valeur d'entrée en entier

# Initialisation d'une liste vide pour stocker les lignes de la grille
a = []

# Initialisation du compteur de '#' à 0
ct = 0

# Boucle pour lire chaque ligne de la grille
for i in range(h):  # Pour chaque ligne de la grille (de 0 à h-1)
    s = input()  # Lire une ligne de la grille sous forme de chaîne de caractères
    a.append(s)  # Ajouter la ligne lue à la liste 'a'
    ct += s.count('#')  # Compter le nombre de '#' dans cette ligne et l'ajouter au compteur total

# Initialiser une file (queue) avec le point de départ (0, 0)
queue = [(0, 0)]  # Représente la position actuelle à explorer ; commence par le coin supérieur gauche

# Initialiser une liste pour garder trace des cellules déjà visitées
check = []  # Cette liste stockera les tuples (i, j) déjà visités

# Vérifier si la cellule de départ (0, 0) contient bien un '#'
if a[0][0] == '.':  # Si la case de départ n'est pas un mur
    print('Impossible')  # Il n'est pas possible de commencer, donc afficher 'Impossible'
    exit()  # Arrêter immédiatement le programme

# Boucler tant qu'il y a des éléments à explorer dans la file (queue)
while queue != []:  # Continuer tant que la file n'est pas vide
    # Prendre la première position dans la file (FIFO - comportement de file standard)
    i, j = queue[0]  # Récupérer la position (ligne i, colonne j) à explorer
    queue.pop(0)  # Enlever cette position de la file

    if not (i, j) in check:  # Vérifier si cette position n'a pas déjà été visitée
        # Vérifier si le déplacement vers le bas est possible :
        if i + 1 < h:  # Si la position sous la position actuelle est dans la grille
            if a[i + 1][j] == '#':  # Si la case en dessous est un mur '#'
                queue.append((i + 1, j))  # Ajouter cette nouvelle position à explorer

        # Vérifier si le déplacement vers la droite est possible :
        if j + 1 < w:  # Si la position à droite de la position actuelle est dans la grille
            if a[i][j + 1] == '#':  # Si la case à droite est un mur '#'
                queue.append((i, j + 1))  # Ajouter cette nouvelle position à explorer

        # Marquer cette position comme visitée
        check.append((i, j))

        # Vérifier un cas d'ambiguïté : arriver sur une case où on peut aller vers le bas et la droite en même temps
        if i + 1 < h and j + 1 < w:  # Les deux cases (en bas et à droite) existent dans la grille
            if a[i + 1][j] == '#' and a[i][j + 1] == '#':  # Si les deux cases sont des murs
                break  # Finir la boucle immédiatement (cas où le chemin se divise)

        # S'assurer que la file n'est pas vide avant de vérifier la prochaine position
        if queue != []:
            # Si la prochaine position à explorer est le coin final de la grille et que c'est aussi un mur
            if queue[0] == (h - 1, w - 1) and a[h - 1][w - 1] == '#':
                # Vérifier si le nombre total de '#' est bien égal à h + w - 1 (le nombre minimal pour un chemin unique)
                if h + w - 1 == ct:
                    print('Possible')  # Il existe un chemin unique du début à la fin utilisant tous les '#'
                    exit()  # Fin du programme après avoir trouvé la solution

# Si aucune des conditions de succès n'a été rencontrée, alors le chemin est impossible
print('Impossible')  # Afficher que la configuration ne permet pas un chemin unique avec ces contraintes