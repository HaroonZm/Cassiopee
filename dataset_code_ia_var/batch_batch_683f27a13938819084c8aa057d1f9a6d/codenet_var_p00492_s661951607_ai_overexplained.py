def solve():
    # Importation du module deque depuis la bibliothèque collections.
    # deque (double-ended queue) est une structure de donnée similaire à une file (queue)
    # mais permettant également d'ajouter ou enlever des éléments en début ou fin avec une complexité constante.
    from collections import deque

    # Importation de la fonction deepcopy du module copy.
    # deepcopy permet de faire une copie profonde d'un objet.
    # Ici, c'est utilisé pour avoir une copie indépendante de la matrice a.
    from copy import deepcopy

    # Lecture de deux entiers depuis l'entrée standard (stdin) :
    # W : largeur (nombre de colonnes), H : hauteur (nombre de lignes).
    # input().split() lit une chaîne de caractères, la découpe par espace, map(int, ...) convertit chaque morceau en entier.
    W, H = map(int, input().split())

    # Construction de la matrice a représentant la carte/terrain :
    # La matrice a sera de taille (H+2) x (W+2) pour ajouter une bordure de zéros tout autour.
    # Ceci permet d'éviter des erreurs d'index hors limites lors des parcours voisins.
    # Explications détaillées :
    # - [[0]*(W+2)] : ligne du haut (bordure de zéros)
    # - [list(map(int, ("0 "+input()+" 0").split())) for _ in [0]*H] :
    #   Pour chaque ligne du terrain, on ajoute un 0 au début et à la fin,
    #   puis on convertit l'entrée saisie en liste d'entiers (split sur les espaces).
    # - [[0]*(W+2)] : ligne du bas (autre bordure de zéros)
    a = (
        [[0] * (W + 2)] +  # Ligne supérieure de zéros
        [list(map(int, ("0 " + input() + " 0").split())) for _ in [0] * H] +  # Lignes réelles avec bordures
        [[0] * (W + 2)]  # Ligne inférieure de zéros
    )

    # Initialisation du résultat (compteur global) à 0.
    result = 0

    # Création d'une copie profonde de la matrice a pour servir de matrice de contrôle de visite :
    # visited gardera la trace des cases déjà explorées par l'algorithme BFS.
    visited = deepcopy(a)

    # Initialisation de la file FIFO (deque) pour la recherche en largeur :
    # On démarre depuis la case (0, 0), c'est-à-dire tout en haut à gauche (coin extérieur de la bordure).
    dq = deque([(0, 0)])

    # Pour optimiser légèrement l'accès, on crée des variables locales pour append (ajout à la fin) et popleft (retrait du début).
    append = dq.append
    popleft = dq.popleft

    # Début de la boucle principale du BFS (parcours itératif tant que la file n'est pas vide).
    while dq:
        # On retire le couple (x, y) courant de la file (la prochaine position à explorer).
        x, y = popleft()

        # Détermination de la liste des déplacements (voisins) selon la parité de la coordonnée y (ligne) :
        # Sur une grille hexagonale, les voisins diffèrent selon que la ligne courante est paire ou impaire,
        # d'où ce calcul conditionnel particulier.
        # La liste neighbour contient les déplacements sous forme de couples (dx, dy).
        neighbour = (
            [(-1, 0), (1, 0)] +  # Voisins gauche et droite (présents dans tous les cas)
            (
                [(-1, -1), (0, -1), (-1, 1), (0, 1)]  # Coordonnées pour lignes paires (y%2==0)
                if y % 2 == 0
                else [(0, -1), (1, -1), (0, 1), (1, 1)]  # Coordonnées pour lignes impaires (y%2!=0)
            )
        )

        # Première boucle : on regarde tous les voisins immédiats de la case (x, y).
        # Objectif : compter, pour chaque case extérieure (explorée par BFS), le nombre de faces/côtés connectés à des cases non-vides ("1")
        # On refait cette opération dans la boucle suivante pour l'exploration proprement dite.
        for dx, dy in neighbour:
            # Calcul des coordonnées absolues du voisin
            nx, ny = x + dx, y + dy

            # Vérification que les coordonnées du voisin sont bien dans les limites de la matrice (évite les erreurs d'index)
            if 0 <= nx < W + 2 and 0 <= ny < H + 2:
                # On ajoute à result la valeur (0 ou 1) contenue dans a à la position du voisin.
                # Cela correspond à la présence (1) ou non (0) d'un bâtiment/mur/obstacle sur la case voisine.
                result += a[ny][nx]

        # Deuxième boucle : exploration effective (BFS) des cases voisines non visitées et vides ("0").
        for dx, dy in neighbour:
            # Calcul des coordonnées absolues du voisin
            nx, ny = x + dx, y + dy

            # Vérification que les coordonnées sont dans les bornes
            # ET que la case voisine est extérieure (0) et encore non visitée.
            # Note : visited est initialisé avec la carte, donc visited[ny][nx]==0 si non visité et vide.
            if 0 <= nx < W + 2 and 0 <= ny < H + 2 and visited[ny][nx] == 0:
                # On marque cette case comme visitée pour éviter de la revisiter
                visited[ny][nx] = 1
                # On ajoute cette case à la file pour poursuivre la recherche en largeur à partir de là
                append((nx, ny))

    # Affichage du résultat final (nombre de côtés exposés des cellules "1" entourant les espaces extérieurs)
    print(result)

# Bloc principal de lancement du programme :
# Cette structure permet de ne lancer solve() que si ce fichier est exécuté comme programme principal,
# et pas s'il est importé comme module dans un autre script Python.
if __name__ == "__main__":
    solve()