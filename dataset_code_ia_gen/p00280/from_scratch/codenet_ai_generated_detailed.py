# Solution complète en Python avec commentaires détaillés

# Problème résumé :
# Deux joueurs (ジョウ君 et ヤエさん) jouent au tennis avec des règles de score spécifiques :
# - Si un joueur atteint 5 points avant que l'autre ait 4, il gagne.
# - Si les deux atteignent 4 points (4-4), il faut qu’un joueur prenne deux points consécutifs pour gagner.
# - Si après 4-4, les joueurs marquent chacun un point (5-5), c’est un match nul.
# Le problème : donné un score final (j, y), trouver et afficher toutes les séquences possibles de points (A=ジョウ君 marque, B=ヤエさん marque) menant de 0-0 à ce score, selon les règles.

def tennis_paths(j_target, y_target):
    # On cherche toutes les séquences de 'A' et 'B' qui mènent de (0,0) à (j_target, y_target)
    # en respectant les règles ci-dessus.

    # Vérification initiale des contraintes des entrées
    # j et y dans [0..6], avec conditions particulières sur les scores 6-4 ou 4-6 ou autre cas
    # Conditions du problème :
    # (j, y) != (0, 0)
    # Si j=6 => y=4
    # Si y=6 => j=4
    # Sinon 0 <= j,y <=5 ou 5 max si pas 6.
    # Ces conditions seront considérées valides dans l'entrée.

    # Cette fonction vérifiera la validité d'un état selon les règles du score.
    def valid_state(j, y):
        # Cas fin : un joueur gagne clairement
        # Le jeu s'arrête si un joueur a gagné, aucun point supplémentaire n'est possible après cela.
        
        # Règle 1: Un joueur gagne s'il a 5 points et son adversaire 3 ou moins.
        if j == 5 and y <= 3:
            return True
        if y == 5 and j <= 3:
            return True

        # Règle 2 & 3: Reprise après 4-4
        # Si les deux ont au moins 4 points:
        if j >= 4 and y >= 4:
            # 4-4 spécifiquement
            if j == 4 and y == 4:
                # C'est l'état initial de deuce, toujours possible.
                return True
            # Après 4-4, un joueur doit prendre 2 pts consécutifs pour gagner
            # C-à-d état possible :
            # - quelqu'un a 6 pts et l'autre 4 => victoire comme indiqué dans l'entrée (6-4 ou 4-6)
            if (j == 6 and y == 4) or (j == 4 and y == 6):
                return True
            # 5-5 cas de match nul possible
            if j == 5 and y == 5:
                return True
            # autoriser d'autres scores (p.ex 5-4 ou 4-5) qui représentent les étapes enchainées
            if (j == y+1 and y >=4) or (y == j+1 and j >=4):
                return True
            # états autres que ci-dessus ne sont pas valides
            return False
        
        # Pour tous les autres cas, tant que les scores sont <= 5 et pas gagnés, c'est valide
        if 0 <= j <= 5 and 0 <= y <= 5:
            # Le jeu continue
            return True

        return False

    # Vérifie si l'état final est un état de fin de partie (victoire ou match nul)
    def is_end_state(j, y):
        # Si l'état correspond au score final donné, on doit considérer si c'est un score possible final.
        
        # condition victoire :
        if j == 5 and y <= 3:
            return True
        if y == 5 and j <= 3:
            return True
        if (j == 6 and y == 4) or (j == 4 and y == 6):
            return True
        if j == 5 and y == 5:
            return True
        return False

    # On utilisera une recherche DFS depuis (0,0) jusqu'à (j_target, y_target).
    # On accumulera les séquences et on retournera celles qui mènent à l'état final.
    # Comme les séquences sont à trier en ordre lexicographique, on explorera d'abord A puis B.

    results = []

    def dfs(j, y, path):
        # Si on a atteint le score cible, on ajoute la séquence si c'est bien une fin valide
        if (j, y) == (j_target, y_target):
            if is_end_state(j, y):
                results.append("".join(path))
            return

        # Les gains possibles pour l'étape suivante : A (ジョウ君 marque) ou B (ヤエさん marque)
        # On teste A en premier, puis B - pour s'assurer que les résultats sont en ordre lex.
        # On vérifie que l'état résultant est valide avant d'y aller.

        # A marque
        j_next = j + 1
        y_next = y
        if valid_state(j_next, y_next):
            dfs(j_next, y_next, path + ['A'])

        # B marque
        j_next = j
        y_next = y + 1
        if valid_state(j_next, y_next):
            dfs(j_next, y_next, path + ['B'])


    # Lancement recherche
    dfs(0, 0, [])

    # Résultats triés (la recherche suit déjà l'ordre lex du fait de dfs(A puis B))
    results.sort()

    # Affichage
    for res in results:
        print(res)


# --- Lecture des données ---
j, y = map(int, input().split())

tennis_paths(j, y)