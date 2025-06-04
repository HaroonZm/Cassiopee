def read_input():
    """
    Lit les dimensions d'une grille (H, W) et les lignes représentant la grille elle-même depuis l'entrée standard.

    Returns:
        tuple: Un tuple contenant :
            - H (int) : Le nombre de lignes de la grille.
            - W (int) : Le nombre de colonnes de la grille.
            - MAP (List[List[str]]) : Une liste représentant la grille sous forme de listes de caractères.
    """
    # Lecture de la taille (H, W) de la grille.
    H, W = map(int, input().split())
    # Lecture des H lignes d'entrée et conversion en listes de caractères.
    MAP = [list(input()) for _ in range(H)]
    return H, W, MAP

def collect_b_positions(H, W, MAP):
    """
    Collecte toutes les positions de la lettre 'B' dans la grille.

    Args:
        H (int): Nombre de lignes de la grille.
        W (int): Nombre de colonnes de la grille.
        MAP (List[List[str]]): La grille.

    Returns:
        List[List[int]]: Une liste des positions où 'B' est présent. 
                         Chaque position est une liste [ligne, colonne].
    """
    BLIST = []
    # Parcourt toutes les cases de la grille.
    for i in range(H):
        for j in range(W):
            # Si on trouve un 'B', on enregistre sa position.
            if MAP[i][j] == "B":
                BLIST.append([i, j])
    return BLIST

def max_manhattan_distance(BLIST):
    """
    Calcule la plus grande distance de Manhattan entre deux positions de la liste BLIST.

    Args:
        BLIST (List[List[int]]): Liste des positions de 'B' dans la grille.

    Returns:
        int: La distance de Manhattan maximale possible entre deux cases 'B'.
    """
    if not BLIST:
        return 0

    # Calcul de la distance maximale dans deux orientations possibles :
    # 1. Selon la somme des indices (x+y).
    BLIST.sort(key=lambda x: x[0] + x[1])
    # La distance entre le premier et le dernier selon cet ordre.
    ans1 = abs(BLIST[0][0] - BLIST[-1][0]) + abs(BLIST[0][1] - BLIST[-1][1])

    # 2. Selon la différence des indices (x-y).
    BLIST.sort(key=lambda x: x[0] - x[1])
    # La distance entre le premier et le dernier selon ce nouvel ordre.
    ans2 = abs(BLIST[0][0] - BLIST[-1][0]) + abs(BLIST[0][1] - BLIST[-1][1])

    # On conserve la distance maximale trouvée.
    return max(ans1, ans2)

def main():
    """
    Programme principal.
    Lit la grille, collecte les positions des 'B', puis calcule et affiche la distance de Manhattan maximale.
    """
    H, W, MAP = read_input()
    BLIST = collect_b_positions(H, W, MAP)
    ANS = max_manhattan_distance(BLIST)
    print(ANS)

if __name__ == "__main__":
    main()