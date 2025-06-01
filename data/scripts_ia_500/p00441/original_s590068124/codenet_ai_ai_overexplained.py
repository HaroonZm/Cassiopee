# Début d'une boucle infinie qui continuera à s'exécuter jusqu'à ce qu'une condition de sortie soit rencontrée.
while True:
    # Lecture d'une entrée utilisateur, convertie en entier, et assignée à la variable n.
    # Cette entrée représente le nombre de "poteaux" (points) à lire ensuite.
    n = int(input())
    
    # Condition pour sortir de la boucle infinie : si n est égal à 0 (faux en booléen),
    # alors on arrête la boucle avec 'break'. Cela signifie qu'on ne traite plus d'autres cas.
    if not n:
        break

    # Création d'une liste de tuples, chaque tuple contenant deux entiers.
    # La liste 'poles' contient n éléments, lus un par un.
    # Chaque ligne d'entrée est lue, séparée en deux valeurs, converties en entier, puis groupées en tuple (x, y).
    poles = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Conversion de la liste 'poles' en un ensemble (set) pour permettre une recherche rapide (O(1) en moyenne).
    # Cela facilite le test de présence d'un point dans le groupe.
    poles_set = set(poles)

    # Initialisation d'une variable 'max_square' à 0.
    # Cette variable contiendra la plus grande valeur de côté au carré d'un carré détecté parmi les poteaux.
    max_square = 0
    
    # Première boucle for pour parcourir tous les points indexés par i.
    for i in range(n):
        # Extraction des coordonnées du poteau i.
        x1, y1 = poles[i]
        
        # Deuxième boucle for pour parcourir les points indexés par j à partir de i.
        # Cela évite de recomparer les mêmes paires inversées et optimise la recherche.
        for j in range(i, n):
            # Extraction des coordonnées du poteau j.
            x2, y2 = poles[j]
            
            # Calcul de la différence des coordonnées en x et y entre les points i et j.
            # Ces différences représentent le vecteur orienté du segment entre les deux points.
            dx, dy = x2 - x1, y2 - y1
            
            # Test pour vérifier si deux autres points existent afin de former un carré :
            # Les points recherchés sont ceux qui forment un carré avec les points i et j.
            # Pour cela, on regarde deux orientations possibles à 90 degrés du vecteur original.
            # L'égalité pour les deux cas vérifie que dans l'ensemble des poteaux,
            # les points nécessaires existent.
            if ((x2 + dy, y2 - dx) in poles_set and (x1 + dy, y1 - dx) in poles_set) \
                    or ((x2 - dy, y2 + dx) in poles_set and (x1 - dy, y1 + dx) in poles_set):
                
                # Le carré est possible, calcul de la longueur du côté au carré (dx^2 + dy^2).
                edge = dx ** 2 + dy ** 2
                
                # Mise à jour de max_square si la longueur calculée est plus grande que la valeur courante.
                if max_square < edge:
                    max_square = edge
    
    # Affichage de la plus grande longueur au carré trouvée pour un carré parmi les poteaux.
    print(max_square)