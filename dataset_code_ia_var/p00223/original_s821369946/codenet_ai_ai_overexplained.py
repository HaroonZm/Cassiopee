# Définition d'un tuple contenant 4 directions cardinales différentes
# (droite, gauche, bas, haut) sous forme de déplacements en coordonnées x et y.
# Chaque élément du tuple est un tuple représentant (delta_x, delta_y).
direc = ((1,0),(-1,0),(0,1),(0,-1))

# Boucle principale infinie pour traiter une ou plusieurs grilles (problèmes).
# La boucle se terminera avec une instruction de rupture explicite ("break").
while 1:
    # Lecture d'une ligne contenant deux entiers séparés par un espace, représentant respectivement la largeur X et la hauteur Y de la grille.
    # map(int, input().split()) applique "int" à chaque élément obtenu en coupant la chaîne saisie utilisateur selon les espaces.
    # list() convertit l'objet map en liste.
    X, Y = list(map(int,input().split()))
    
    # Condition d'arrêt : si X vaut 0, cela signifie la fin des saisies et on quitte la boucle principale.
    if X == 0:
        break

    # Lecture des coordonnées initiales de la première pièce (ftx, fty) :
    # - On lit une ligne d'entrée d'où l'on tire deux entiers.
    # - On décrémente chacun par 1 via une fonction lambda car en Python les indices commencent à 0 alors que l'entrée peut être en base 1.
    # - map(int, ...) convertit les valeurs en entiers.
    # - map(lambda x: x-1, ...) applique la décrémentation.
    # - list(...) donne une liste finale de deux éléments assignés à ftx et fty.
    ftx, fty = list(map(lambda x: x-1, map(int, input().split())))
    
    # Même logique que précédemment, pour la deuxième pièce (fkx, fky).
    fkx, fky = list(map(lambda x: x-1, map(int, input().split())))
    
    # Construction de la grille :
    # - m est la matrice représentant le plateau.
    # - On utilise une liste en compréhension pour construire m ligne par ligne.
    # - Pour chaque ligne, on lit une entrée que l'on découpe, convertit en entiers, puis stocke comme une liste.
    # - On répète cela Y fois pour avoir Y lignes.
    m = [list(map(int, input().split())) for i in range(Y)]
    
    # Dictionnaire pour mémoriser les états déjà visités :
    # - Chaque clé est un tuple représentant les coordonnées respectives des deux pièces (ftx, fty, fkx, fky).
    # - La valeur associée à chaque clé est le nombre minimal de mouvements nécessaires pour atteindre cet état.
    # - Initialement, seul l'état de départ (positions initiales) a pour coût 0.
    d = {(ftx, fty, fkx, fky): 0}
    
    # File d'exploration (queue) des états à traiter.
    # - s est une liste de listes, chaque élément contient :
    #   [nombre de mouvements effectués jusque-là, (positions des 2 pièces)]
    # - On commence avec l'état initial, 0 déplacement effectué.
    s = [[0, (ftx, fty, fkx, fky)]]
    
    # Variable qui stockera le résultat final : nombre minimal de déplacements, ou 'NA' si aucun résultat trouvé dans la limite.
    res = 'NA'
    
    # Boucle de parcours en largeur (BFS) : tant que la file d'états (s) n'est pas vide.
    while len(s) > 0:
        # Récupération et suppression du premier état de la file (FIFO).
        # - pop(0) retire le premier élément du tableau.
        spm = s.pop(0)

        # Calcul du nombre de mouvements pour cet état courant.
        # - spm[0] contient les mouvements jusqu'à maintenant, on ajoute 1 pour la suite.
        cnt = spm[0] + 1

        # Si le nombre de mouvements dépasse 100, on arrête de chercher (limite arbitraire selon l'énoncé pour éviter des parcours trop longs).
        if cnt > 100:
            break
        
        # Définition d'une fonction interne search_move qui :
        # - Tente d'effectuer tous les déplacements possibles pour les deux pièces en simultané, dans chaque direction.
        def search_move():
            # Boucle sur toutes les directions cardinales, 4 au total.
            for i in range(4):
                # Calcul des nouvelles positions proposées pour la première pièce (ftx, fty) :
                # Ajout du delta correspondant à la direction à la position actuelle.
                tx = spm[1][0] + direc[i][0]  # Nouvelle abscisse
                ty = spm[1][1] + direc[i][1]  # Nouvelle ordonnée
                
                # Idem, pour la seconde pièce (fkx, fky) mais dans la direction opposée (-delta).
                # Cela simule un "déplacement miroir".
                kx = spm[1][2] - direc[i][0]  # Nouvelle abscisse
                ky = spm[1][3] - direc[i][1]  # Nouvelle ordonnée
                
                # Variable qui comptera le nombre de pièces bloquées (soit par obstacle, soit par sortie de grille).
                hm = 0

                # Test si la nouvelle position de la première pièce est invalide (hors grille ou obstacle "1").
                # Si c'est le cas, on ramène la pièce à sa position initiale, et on incrémente hm.
                if tx < 0 or tx >= X or ty < 0 or ty >= Y or m[ty][tx] == 1:
                    tx = spm[1][0]
                    ty = spm[1][1]
                    hm += 1

                # Pareil pour la deuxième pièce, mêmes raisons, mais avec axes kx, ky.
                if kx < 0 or kx >= X or ky < 0 or ky >= Y or m[ky][kx] == 1:
                    kx = spm[1][2]
                    ky = spm[1][3]
                    hm += 1

                # Si les deux pièces sont entièrement bloquées dans cette direction, on passe à la suivante (continue arrête l'itération en cours).
                if hm == 2:
                    continue

                # Création d'un tuple qui représente l'état résultant de ce déplacement proposé.
                tpl = (tx, ty, kx, ky)

                # Si cet état est déjà dans le dictionnaire d (donc déjà visité), et qu'on l'avait atteint en un nombre de mouvements inférieur ou égal, on l'ignore.
                if tpl in d and d[tpl] <= cnt:
                    continue

                # Si, après déplacement, les deux pièces se retrouvent sur la même case (c'est un état objectif), on renvoie True (succès).
                if tx == kx and ty == ky:
                    return True
                else:
                    # Sinon, on ajoute ce nouvel état à la file d'états à traiter ultérieurement.
                    s.append([cnt, tpl])
                    # On enregistre le nombre de mouvements nécessaires pour atteindre cet état dans le dictionnaire.
                    d[tpl] = cnt
            # Si on a exploré toutes les directions sans succès, on retourne False.
            return False
        
        # On tente les déplacements depuis l'état courant.
        if search_move():
            # Si le but est atteint (les deux pièces se rejoignent), on garde la valeur du nombre de coups et on arrête la recherche.
            res = str(cnt)
            break
    # Une fois la file vide ou solution trouvée, on affiche le résultat pour ce cas de test.
    print(res)