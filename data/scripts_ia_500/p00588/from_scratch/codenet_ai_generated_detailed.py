def extraordinary_girl():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        books = input().strip()

        # La bibliothèque a 4N étagères numérotées de 1 à 4N.
        # Chaque position correspond à une étagère, indiquant s'il y a des livres à ranger.
        # On ne peut s'arrêter qu'au milieu des étagères ou aux intersections.
        # Le chemin est constitué de 3 passages principaux horizontaux dans un seul sens (forward)
        # et (N+1) passages secondaires verticaux.
        #
        # Coûts:
        #  - un pas entre intersections adjacentes = 1
        #  - un pas entre intersection et milieu d’étagère adjacente = 0.5
        #
        # Objectif:
        # Trouver le coût minimum pour parcourir la bibliothèque dans l’ordre des passages et
        # déposer tous les livres requis.

        # Modélisation de la disposition:
        # Il y a 4 rangées horizontales (appelées "lignes"):
        # Rangées horizontales: 0 à 3
        # Colonnes verticales: 0 à N (car il y a N+1 sub passages)
        #
        # Etageres sont disposées entre passage verticaux:
        # - dans chaque ligne, il y a N étagères numérotées de 1 à N, mais ici chaque shelf correspond à une position :
        # - les étagères 1..4N sont disposées en lignes horizontales de 4 étagères par colonne verticale.
        # Par exemple:
        # Pour chaque colonne c de 0 à N-1, les étagères sont:
        # (ligne 0, colonne c) -> étagère 4*c +1
        # (ligne 1, colonne c) -> étagère 4*c +2
        # (ligne 2, colonne c) -> étagère 4*c +3
        # (ligne 3, colonne c) -> étagère 4*c +4

        #
        # Contraintes sur mouvement:
        # Elle ne peut marcher que en avant sur les passages principaux horizontaux:
        # donc les mouvements horizontaux ne peuvent aller que dans le sens colonne croissante.
        # Elle peut se déplacer verticalement librement sur les passages verticaux,
        # donc dans les colonnes en haut ou en bas.
        #
        # Notation du problème:
        # Elle démarre à la position blanche => (ligne 0, colonne 0), intersection avant la première étagère.
        # Elle termine à la position noire => (ligne 3, colonne N), intersection après la dernière étagère.
        #
        # On cherche un chemin minimal passant par toutes les étagères où books[i]=='Y',
        # en déposant les livres au milieu des étagères. Arrêt possible aussi aux intersections.
        #
        # Remarques:
        #  - Le coût entre intersection adjacentes verticales ou horizontales = 1
        #  - Le coût entre intersection et milieu d’étagère = 0.5

        # Effectuer la modélisation en termes de colonnes:
        # On modélise l’état à chaque colonne c (de 0 à N)
        # à la sortie de chaque colonne c, on a 4 positions possibles (sur les 4 lignes aux intersections).
        #
        # Pour chaque colonne, il peut y avoir des étagères où déposer:
        # livres à position 4*c + l (l=0..3 pour ligne 0..3).
        #
        # On va progresser de la colonne 0 à la colonne N.
        #
        # A chaque étape, on mémorise le coût minimum pour atteindre chaque position d'intersection située à la sortie de la colonne.
        # Entre les colonnes c et c+1, on calculera les coûts en prenant en compte le fait qu'on doit retourner les livres
        # à la colonne c (milieu des étagères), en se déplaçant verticalement sur la colonne, et horizontalement vers la droite.
        #
        # Pour résoudre cela, on va:
        # - Pour chaque colonne c, déterminer la plage verticale (lignes) à couvrir,
        # - Trouver le coût minimum pour couvrir toutes les étagères avec livres nécessaires dans cette colonne.
        #
        # Entre colonnes:
        # - Elle commence à une intersection en ligne il à la sortie de la colonne c (appelé dp[il]),
        # - Doit atteindre une autre intersection à la sortie de la colonne c+1,
        # - Pour cela, elle se déplace verticalement sur les passages verticaux dans la colonne c (coût 1 par décalage de ligne vers haut/bas),
        #   dépose les livres au milieu (coût 0.5 pour se décaler entre intersection et milieu de l’étagère),
        #   puis se déplace à droite (coût 1) vers l’intersection suivante à la colonne c+1.
        #
        # Stratégie:
        # La marche horizontale est seulement possible vers l’avant (colonne croissante).
        # Les passages verticaux sont "libres" en sens.
        #
        # On va pour chaque colonne calculer une "fonction de coût" interne qui donne le coût pour couvrir toutes les étagères de cette colonne,
        # dépendant de la position verticale d'entrée et de sortie (intersection en haut ou en bas).
        #
        # Puis combiner avec les coûts dp de la colonne précédente.

        # Extraire les livres par colonne en 4 lignes:
        books_per_line = [[False] * N for _ in range(4)]
        for i in range(4 * N):
            line = i % 4
            col = i // 4
            books_per_line[line][col] = (books[i] == 'Y')

        # dp[col][line_intersection]: coût minimum pour être à la sortie de la colonne col (intersection ligne line_intersection)
        # Initialiser dp à l'infini
        INF = 10**9
        dp = [[INF] * 4 for _ in range(N + 1)]

        # position de départ: avant la colonne 0, intersection en ligne 0 (coin haut gauche)
        dp[0][0] = 0

        # Fonction calulant le coût minimal pour couvrir tous les étagères avec livres dans la colonne c,
        # en partant d'une intersection d'entrée (ligne in_line),
        # en terminant à une intersection de sortie (ligne out_line).
        #
        # Elle peut se déplacer verticalement sur cette colonne,
        # faire des arrêts aux milieu des étagères (0.5 coût entrée et sortie),
        # et doit déposer les livres aux étagères avec livres,
        # couvrant toutes les lignes où there is a book.
        #
        # Le problème réduit à:
        # - Trouver la plage de lignes avec livres à couvrir,
        # - Il faut se déplacer verticalement du "in_line" jusque à la ligne min_line du segment,
        #   puis aller jusqu'à la ligne max_line couvrant tous les livres,
        # - Puis se déplacer jusqu'à la ligne "out_line" à la sortie,
        # - Le coût horizontal pour passer à la colonne suivante est toujours +1.

        def cover_column_cost(c, in_line, out_line):
            # trouver les lignes où il faut déposer des livres dans la colonne c
            lines_with_books = [line for line in range(4) if books_per_line[line][c]]

            if not lines_with_books:
                # Pas de livre dans cette colonne: on peut juste aller de in_line à out_line verticalement (coût = distance verticale)
                # puis horizontalement (1)
                vertical_cost = abs(in_line - out_line)
                horizontal_cost = 1
                return vertical_cost + horizontal_cost

            min_line = min(lines_with_books)
            max_line = max(lines_with_books)

            # Pour déposer livres, il faut atteindre tous les lignes entre min_line et max_line inclus.
            # On peut :
            # - descendre ou remonter de in_line à un point de départ dans [min_line, max_line]
            # - parcourir toute la plage min_line -> max_line
            # - sortir vers out_line depuis une extrémité ou l'autre de cette plage,
            # en 4 déplacements verticaux (de lignes).
            #
            # Il faut trouver la meilleur ordre et point d'entrée/sortie dans la colonne:
            #
            # Possibilités:
            # 1) in_line -> min_line ... max_line -> out_line
            # 2) in_line -> max_line ... min_line -> out_line
            #
            # Le déplacement interne (min_line <-> max_line) coûte (max_line - min_line)
            #
            # Pour chaque extrémité, le mouvement d'entrée/sortie coûte la distance verticale.
            #
            # Chaque arrêt au milieu d'étagère coûte 0.5 * 2 = 1 (car on passe 0.5 pour entrer, 0.5 pour sortir)
            # mais les arrêts sont obligatoires sur toutes les étagères c avec livres donc num_lines = len(lines_with_books)
            #
            # Total coût arrêt : num_lines * 1 = num_lines
            #
            # Finalement, total = mouvement vertical + arrêt + 1 (pour le mouvement horizontal vers la prochaine colonne)

            # Calcul des coûts pour les deux parcours
            num_lines = len(lines_with_books)
            horizontal_cost = 1

            # Option A: in_line -> min_line -> max_line -> out_line
            cost_a = abs(in_line - min_line) + (max_line - min_line) + abs(out_line - max_line) + num_lines + horizontal_cost
            # Option B: in_line -> max_line -> min_line -> out_line
            cost_b = abs(in_line - max_line) + (max_line - min_line) + abs(out_line - min_line) + num_lines + horizontal_cost

            return min(cost_a, cost_b)

        # Pour toutes les colonnes, on calcule dp
        for c in range(N):
            # Pour chaque position d'arrivée de la colonne c (intersections lignes 0..3)
            for in_line in range(4):
                if dp[c][in_line] == INF:
                    continue
                # Pour chaque position de sortie à la colonne c+1
                for out_line in range(4):
                    cost = dp[c][in_line] + cover_column_cost(c, in_line, out_line)
                    if cost < dp[c + 1][out_line]:
                        dp[c + 1][out_line] = cost

        # position finale: intersection ligne 3 à la colonne N
        # dp[N][3] est le coût minimal total.
        print(dp[N][3])