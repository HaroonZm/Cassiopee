def count_paths():
    """
    Cette fonction lit plusieurs paires de dimensions (hauteur, largeur) depuis l'entrée standard,
    puis calcule et affiche le nombre de chemins possibles dans une grille modifiée, selon des règles spécifiques.
    
    Le processus s'interrompt dès qu'une hauteur nulle est fournie.
    
    La logique utilise une programmation dynamique stockée dans un dictionnaire 'mp' où chaque clé est un triplet
    (i, j, état) représentant la position dans la grille et l'état du chemin, et la valeur est le nombre de chemins.
    Les états "UU", "RR", "UR" et "RU" correspondent à différentes dernières directions ou combinaisons de mouvements.
    
    Les résultats sont affichés modulo 100000.
    """
    while True:
        # Lecture des dimensions h (hauteur) et w (largeur)
        h, w = map(int, input().split())
        
        # Condition d'arrêt : si la hauteur est nulle, on sort de la boucle
        if h == 0:
            break
        
        # On décrémente h et w pour ajuster les indices à partir de zéro
        h -= 1
        w -= 1
        
        # Initialisation du dictionnaire pour la programmation dynamique avec des cas de base
        # Chaque clé est un tuple (i, j, direction)
        # Rubans de départ en position (0,2), (2,0), (1,1) avec différentes combinaisons de directions
        mp = {
            (0, 2, "UU"): 1,
            (2, 0, "RR"): 1,
            (1, 1, "UR"): 1,
            (1, 1, "RU"): 1
        }
        
        # Parcours de la grille avec indices i (hauteur) et j (largeur)
        for i in range(h + 1):
            for j in range(w + 1):
                # On ignore les cases où la somme des indices est inférieure ou égale à 2, 
                # car elles sont traitées via les cas de base initialisés
                if i + j <= 2:
                    continue
                
                # Calcul du nombre de chemins se terminant par la direction 'UU' en (i, j)
                mp[(i, j, 'UU')] = 0
                # Accumulation des chemins venant de la même direction 'UU' à gauche
                if (i, j - 1, 'UU') in mp:
                    mp[(i, j, 'UU')] += mp[(i, j - 1, 'UU')]
                # Accumulation des chemins venant de la direction 'RU' à gauche
                if (i, j - 1, 'RU') in mp:
                    mp[(i, j, 'UU')] += mp[(i, j - 1, 'RU')]
                
                # Calcul du nombre de chemins se terminant par la direction 'RR' en (i, j)
                mp[(i, j, 'RR')] = 0
                # Accumulation des chemins venant de la même direction 'RR' en haut
                if (i - 1, j, 'RR') in mp:
                    mp[(i, j, 'RR')] += mp[(i - 1, j, 'RR')]
                # Accumulation des chemins venant de la direction 'UR' en haut
                if (i - 1, j, 'UR') in mp:
                    mp[(i, j, 'RR')] += mp[(i - 1, j, 'UR')]
                
                # Calcul du nombre de chemins se terminant par la direction 'UR' en (i, j)
                mp[(i, j, 'UR')] = 0
                # Accumulation des chemins venant de la direction 'UU' en haut
                if (i - 1, j, 'UU') in mp:
                    mp[(i, j, 'UR')] += mp[(i - 1, j, 'UU')]
                
                # Calcul du nombre de chemins se terminant par la direction 'RU' en (i, j)
                mp[(i, j, 'RU')] = 0
                # Accumulation des chemins venant de la direction 'RR' à gauche
                if (i, j - 1, 'RR') in mp:
                    mp[(i, j, 'RU')] += mp[(i, j - 1, 'RR')]
        
        # Calcul du total des chemins possibles en (h, w) en sommant sur tous les états
        total_paths = (
            mp.get((h, w, 'UU'), 0) +
            mp.get((h, w, 'UR'), 0) +
            mp.get((h, w, 'RU'), 0) +
            mp.get((h, w, 'RR'), 0)
        ) % 100000
        
        # Affichage du résultat modulo 100000
        print(total_paths)


# Appel de la fonction principale pour lancer le calcul
count_paths()