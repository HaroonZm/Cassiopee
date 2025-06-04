import sys

sys.setrecursionlimit(10**7)

def solve_connect(R, C, strings):
    # Pour chaque ligne i, on doit choisir les colonnes où placer les lettres de strings[i] dans l'ordre, sans changer la séquence.
    # Objectif : maximiser la somme des points.
    # Point pour une case non vide = nombre de voisins (haut, bas, gauche, droite) avec la même lettre.
    # Contraintes :
    # - R ≤ 128, C ≤ 16
    # - |s_i| ≤ C
    # Les positions choisies par ligne sont croissantes, donc on place letters i sur colonnes a_j avec a_1 < a_2 < ... < a_|s_i|.
    # 
    # Approche :
    # L'optimisation se fait par programmation dynamique ligne par ligne.
    #
    # Remarque importante :
    # - Le score total dépend des adjacents verticaux et horizontaux.
    # - Le score horizontal dans la même rangée est déterminé uniquement par le choix des colonnes pour la même ligne.
    # - Le score vertical dépend des lettres aux mêmes colonnes dans les lignes i et i-1.
    # 
    # Donc on peut :
    # - Pour chaque ligne, on choisit un sous-ensemble de colonnes pour s_i respectant ordre.
    # - On modélise chaque choix comme un masque binaire avec exactement |s_i| bits à 1, dans l'ordre.
    #
    # Il faut générer tous les sous-ensembles de colonnes de taille |s_i| (avec C ≤ 16 et |s_i| ≤ C, c'est faisable).
    #
    # Pour chaque ligne, on calcule:
    # - score horizontal sur cette ligne (lettres adjacentes en horizontal qui sont identiques)
    # - pour chaque combinaison précédente ligne (mask et les lettres placées), on calcule score vertical (lettres identiques à cette colonne)
    #
    # DP:
    # On note states à la ligne i comme des tuples (mask, string_placé) mais le string placé est fixe (s_i), on n'a que mask à stocker.
    # On mémorise pour la ligne i, pour chaque mask valide, le score max total cumulée.
    #
    # Il faut aussi garder en mémoire les lettres placées ligne i-1 pour calcul vertical.
    #
    # Pour gérer cela:
    # - On stocke en DP la meilleure score finale pour chaque mask ligne i.
    # - On stocke les modèles de ligne précédente pour calculer vertical.
    #
    # Pour la ligne i=0, pas de score vertical.
    #
    # Implémentation détaillée :
    # 1. Pour chaque ligne, générer toutes les positions possibles (masques) de taille |s_i|.
    # 2. Calculer score horizontal de chaque masque.
    # 3. Pour dp, on a dp[i][mask] = meilleur score jusqu'à la ligne i avec la configuration mask à ligne i.
    # 4. Initialisation dp[0][mask] = score_horizontal(mask).
    #
    # 5. Pour i>0, on calcule pour chaque mask_i (ligne i), tous les mask_j (ligne i-1):
    #    - calculer score vertical entre mask_i et mask_j (lettres identiques aux colonnes activés dans les deux masques)
    #    - dp[i][mask_i] = max{ dp[i-1][mask_j] + score_horizontal(mask_i) + score_vertical(mask_i, mask_j) }
    #
    # Complexité :
    # Pour chaque ligne:
    #   Nombre de masques ≈ comb(C, |s_i|) ≤ comb(16, |s_i|)
    # En moyenne raisonnable.
    # Pour chaque transition, on fait produit des deux masques ≈ (comb(C, |s_i|))^2.
    # R max 128.
    # Cela est faisable en Python avec quelques optimisations.
    #
    # Optimisation possible: pré-calcul des masques par ligne, pré-calcul des scores horizontaux, et accès rapide.
    
    from itertools import combinations

    # Fonction pour calculer score horizontal (sur une ligne donnée mask):
    # score horizontal = somme des points dus aux paires adjacentes dans la ligne
    # Chaque point est compté de chaque côté, donc on compte pour chaque cellule les adjacents de droite uniquement pour éviter double compte.
    def calc_score_horizontal(s, positions):
        score = 0
        # positions correspond aux colonnes où on place les lettres de s (en ordre)
        # on vérifie les adjacents horizontaux pour pairs consécutifs
        for i in range(len(s)-1):
            # Si caractères identiques et colonnes adjacentes (positions[i]+1 == positions[i+1])
            if s[i] == s[i+1] and positions[i]+1 == positions[i+1]:
                score += 2  # adjacents horizontaux contribuent 1 point à chacun des 2 cases -> total 2
        return score

    # Fonction score vertical : lettres identiques sur la même colonne entre deux lignes
    # score = somme, pour chaque colonne, si les deux cases ont même lettre, +2 (car chaque adjacent compte 1 pour chacun)
    # On évite double compte en ajoutant +2 par paire détectée là
    def calc_score_vertical(s1, pos1, s2, pos2):
        score = 0
        # pos1 et pos2 sont listes croissantes de colonnes où lettres sont placées dans ligne 1 et 2
        # s1 et s2 sont les chaînes correspondantes
        # On parcourt deux listes en même temps pour trouver colonnes communes
        i1 = 0
        i2 = 0
        while i1 < len(pos1) and i2 < len(pos2):
            if pos1[i1] == pos2[i2]:
                if s1[i1] == s2[i2]:
                    score += 2
                i1 += 1
                i2 += 1
            elif pos1[i1] < pos2[i2]:
                i1 += 1
            else:
                i2 += 1
        return score

    # Converts mask (int) to list of columns selected, in order
    def mask_to_positions(mask):
        positions = []
        for c in range(C):
            if mask & (1<<c):
                positions.append(c)
        return positions

    # Génération de tous les masques valides pour une ligne donnée avec |s| lettres :
    # Retourne une liste de masques (int) avec exactement len(s) bits à 1 dans l'ordre.
    def generate_masks(length):
        # length = nombre de bits à prendre dans C bits
        return [sum((1<<c) for c in comb) for comb in combinations(range(C), length)]

    # Initialisation DP
    dp_prev = dict() # mask -> meilleur score
    masks_lines = [] # pour chaque ligne, liste des masques valides
    # Pour récupérer positions et lettres plus facilement
    positions_lines = [] # pour chaque ligne, liste des positions correspondant aux masques

    # Pré-calcul des masques valides et positions
    for i in range(R):
        length = len(strings[i])
        masks = generate_masks(length)
        masks_lines.append(masks)
        # Pour chaque mask, on crée aussi la liste de positions des lettres placées
        pos_list = [mask_to_positions(m) for m in masks]
        positions_lines.append(pos_list)

    # Pré-calcul score horizontaux pour chaque masque de chaque ligne
    score_horizontals = []
    for i in range(R):
        s = strings[i]
        scores_line = []
        for pos in positions_lines[i]:
            scores_line.append(calc_score_horizontal(s, pos))
        score_horizontals.append(scores_line)

    # On initialise la première ligne :
    for idx, mask in enumerate(masks_lines[0]):
        dp_prev[mask] = score_horizontals[0][idx]

    # Pour passer de la ligne i-1 à i :
    # pour chaque mask_i et mask_j on calcule score vertical
    # optimisation : on pré-calcul score vertical entre masque i et masque j pour accélérer
    # Mais cela utiliserait beaucoup de mémoire R*(nombre_masques^2)
    # On fait calcul à la volée avec cache limité

    # Pour accéder aux lettres :
    # ligne i: strings[i], positions_lines[i][pos_mask]

    # DP ligne par ligne
    for i in range(1, R):
        dp_curr = dict()
        # Pour accélérer recherche
        masks_i = masks_lines[i]
        masks_j = masks_lines[i-1]
        s_i = strings[i]
        s_j = strings[i-1]
        pos_i_list = positions_lines[i]
        pos_j_list = positions_lines[i-1]

        # Map mask_j to its dp_prev value
        dp_prev_items = list(dp_prev.items())

        for idx_i, mask_i in enumerate(masks_i):
            pos_i = pos_i_list[idx_i]
            base_score = score_horizontals[i][idx_i]
            best = -1
            for mask_j, val_j in dp_prev_items:
                idx_j = masks_j.index(mask_j)  # coût potentiellement élevé mais masques limités
                pos_j = pos_j_list[idx_j]
                # score vertical entre ligne i et i-1
                s_ver = calc_score_vertical(s_j, pos_j, s_i, pos_i)
                total_score = val_j + base_score + s_ver
                if total_score > best:
                    best = total_score
            dp_curr[mask_i] = best
        dp_prev = dp_curr

    # Le maximum final
    return max(dp_prev.values())


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    R, C = map(int, input().split())
    strings = [input().strip() for _ in range(R)]
    result = solve_connect(R, C, strings)
    print(result)