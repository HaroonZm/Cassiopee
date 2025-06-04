# Commence une boucle infinie afin de traiter plusieurs cas jusqu'à une condition de sortie explicite.
while True:
    # Lit une ligne de l'entrée standard, la découpe en éléments séparés par un espace, puis les convertit en entiers.
    # Ces deux valeurs représentent la largeur (w) et la hauteur (h) de la grille à traiter.
    w, h = map(int, input().split())
    
    # Vérifie si la largeur vaut 0 (condition d'arrêt du programme).
    if w == 0:
        break  # Sort immédiatement de la boucle while, interrompant le traitement de cas.

    # Construit la carte (mp) à partir de l'entrée utilisateur (ligne par ligne).
    # Chaque ligne saisie est encadrée par des zéros sur la gauche et la droite pour simplifier la gestion des bords.
    # Cela signifie que pour chaque ligne, on ajoute un 0 au début et à la fin, formant un "contenant" autour de la grille.
    mp = [ [0] + list(input()) + [0] for _ in range(h) ]
    
    # Insère une ligne de zéros en haut de la grille pour avoir une bordure supérieure.
    mp.insert(0, [0] * (w + 2))
    # Ajoute une ligne de zéros en bas de la grille pour la bordure inférieure.
    mp.append([0] * (w + 2))

    # Convertit chaque case de la carte selon sa nature :
    # - Si la case contient un ".", elle représente un espace vide (sol, air), donc assignée à 0.
    # - Sinon, il s'agit normalement d'un chiffre (sous forme de chaîne), on le convertit en entier correspondant.
    for y in range(1, h + 1):  # Parcourt toutes les lignes "utilisables", excluant les bordures
        for x in range(1, w + 1):  # Parcourt chaque colonne "utile"
            if mp[y][x] == ".":
                mp[y][x] = 0  # Un espace: on met 0
            else:
                mp[y][x] = int(mp[y][x])  # Chiffre : on le convertit vers l'entier

    # Initialise la variable de dernier identifiant utilisé pour marquer des composantes connectées.
    last_id = 10  # On commence à 10 pour éviter la confusion avec les valeurs 0 à 9 d'origine

    # Liste de tous les déplacements possibles en coordonnées (droite, gauche, bas, haut).
    vec = ( (0, 1), (0, -1), (1, 0), (-1, 0) )

    # Définit une fonction récursive pour étiqueter toutes les cellules connectées entre elles ayant la même valeur.
    # - last_id : l'identifiant unique qui marquera le groupe courant.
    # - target : la valeur à identifier (généralement 1 - 9 à l'origine)
    # - x, y : coordonnées actuelles dans la grille.
    def update(last_id, target, x, y):
        # Ne procède que si la case courante possède la valeur recherchée
        if mp[y][x] != target:
            return  # Si ce n'est pas la bonne valeur, on arrête la récursion immédiatement

        # Attribue à la case courante l'identifiant unique du groupe
        mp[y][x] = last_id

        # Pour chaque direction dans "vec" (haut, bas, gauche, droite), on propage l'identifiant de groupe
        for dx, dy in vec:
            update(last_id, target, x + dx, y + dy)

    # Parcourt toute la grille à l'intérieur des bordures pour marquer chaque composante connectée d'origine
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            # Si la case contient une valeur entre 1 et 9 (groupe à identifier)
            if 1 <= mp[y][x] <= 9:
                # Propage l'identifiant de groupe courant dans la composante connectée
                update(last_id, mp[y][x], x, y)
                # Prépare le prochain identifiant pour la prochaine composante
                last_id += 1

    # Le nombre total de groupes (blocs) est calculé, il correspond à la différence entre l'identifiant final et 10 (valeur de départ)
    node_num = last_id - 10

    # Initialise une liste (de taille node_num) de sets pour représenter les arêtes (edges) du graphe.
    # Chaque set contiendra les identifiants des groupes supportés par le groupe courant
    edges = [set() for _ in range(node_num)]

    # Remplit le graphe edges : chaque fois que deux groupes sont adjacents verticalement, on enregistre la relation supporteur/supporté.
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            # Si la valeur d'au-dessus diffère de la valeur courante, et qu'aucune n'est 0 (c-à-d. l'air), il existe une relation
            if mp[y - 1][x] != mp[y][x] and mp[y - 1][x] != 0 and mp[y][x] != 0:
                # On ajoute le groupe du dessus comme support pour le groupe courant
                edges[ mp[y][x] - 10 ].add( mp[y - 1][x] - 10 )

    # Recherche du "root" (groupe le plus bas), le premier groupe trouvé sur la ligne du bas sera la racine du graphe
    for x in range(1, w + 1):
        if mp[h][x] != 0:
            root = mp[h][x] - 10  # Détermine l'indice du groupe racine
            break  # Arrête dès qu'il en trouve un

    # Prépare deux listes :
    # - center stockera l'abscisse pondérée (centre de masse) horizontale de chaque groupe
    # - ground stockera les coordonnées minimales et maximales au sol occupées par chaque groupe
    center = [0] * node_num
    ground = [None] * node_num

    # Parcourt toute la grille pour déterminer les informations de centre de gravité et position "au sol" de chaque groupe
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if mp[y][x] != 0:
                target = mp[y][x] - 10  # Récupère l'indice du groupe concerné
                center[target] += (x + 0.5) / 4  # Ajoute l'abscisse pondérée (centre de la case= x+0.5) avec normalisation
                # Teste si en dessous de (x, y) il y a du vide ou une case du même groupe (solide continu)
                if mp[y + 1][x] in (0, target + 10):
                    continue  # Si oui, on ne traite pas le contact avec le sol
                # Si c'est la première fois qu'on trouve ce groupe au contact du "sol", on initialise l'intervalle.
                if ground[target] == None:
                    ground[target] = [x, x + 1]
                else:
                    # Étend l'intervalle minimal/maximal occupé par le groupe au sol
                    ground[target][0] = min(ground[target][0], x)
                    ground[target][1] = max(ground[target][1], x + 1)

    # Assure que le groupe racine a bien son intervalle d'appui au sol renseigné,
    # même si pour une raison quelconque il n'a pas été trouvé précédemment.
    for x in range(1, w + 1):
        if mp[h][x] == root + 10:
            if ground[root] == None:
                ground[root] = [x, x + 1]
            else:
                ground[root][0] = min(ground[root][0], x)
                ground[root][1] = max(ground[root][1], x + 1)

    # Prépare un cache où sera stocké pour chaque groupe le total_center (centre de gravité composite du sous-arbre supporté)
    total_center = [None] * node_num

    # Définition de la fonction de calcul du centre de masse composite pour un sous-arbre du graphe,
    # exploitant la récursivité pour additionner la masse (nombre de blocs) et leur centre de masse
    def get_total_center(node):
        # Initialisation du moment (somme pondérée des positions) du groupe courant
        mom = center[node]
        # son "poids" (masse) est 1 (lui-même)
        wei = 1
        # Pour chaque groupe supporté (parent direct dans le graphe)
        for to in edges[node]:
            # Calcule récursivement le centre de masse et la masse du sous-groupe supporté
            to_wei, to_pos = get_total_center(to)
            # Ajoute au moment total la contribution du sous-groupe (masse * centre de masse)
            mom += to_wei * to_pos
            # Incrémente la masse totale du sous-arbre
            wei += to_wei
        # Calcule le centre de masse final de tout le sous-arbre (mom / wei)
        total_center[node] = mom / wei
        return wei, total_center[node]  # Retourne la masse et le centre de masse composite

    # Lance la fonction sur le groupe racine pour remplir le cache total_center de tous les sous-arbres
    get_total_center(root)

    # Pour chaque groupe, vérifie que son centre de masse se projette dans l'intervalle de contact au sol (stabilité)
    for gr, cen in zip(ground, total_center):
        l, r = gr  # l = borne gauche, r = borne droite
        # Si le centre sort de la zone d'appui, c'est instable
        if not (l < cen < r):
            print("UNSTABLE")
            break  # Inutile de poursuivre, il suffit d'une instabilité
    else:
        # Si la boucle n'a jamais "break", alors toutes les vérifications sont passées : le tout est stable
        print("STABLE")