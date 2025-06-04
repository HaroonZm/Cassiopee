def read_input():
    """
    Lit les dimensions de la grille (H, W) ainsi que les valeurs dans la grille (intersections).
    Retourne:
        H (int): Nombre de lignes de la grille.
        W (int): Nombre de colonnes de la grille.
        intersections (list of list of int): Valeurs dans chaque case de la grille.
    """
    H, W = list(map(int, input().split(' ')))
    intersections = [list(map(int, input().split(' '))) for _ in range(H)]
    return H, W, intersections

def calculate_min_score(H, W, intersections):
    """
    Calcule le score minimum dans la grille d'intersections. Pour chaque case (h, w), 
    on somme le produit entre la valeur de toutes les autres cases (hors même ligne et colonne)
    et la distance minimale (ligne ou colonne) à (h, w). 
    On cherche la position (h, w) pour laquelle ce score est minimal.

    Args:
        H (int): Nombre de lignes de la grille.
        W (int): Nombre de colonnes de la grille.
        intersections (list of list of int): Valeurs de la grille.

    Returns:
        min_score (int): Le score minimal trouvé.
    """
    min_score = float('inf')
    # Parcourt chaque position possible de la case (h, w)
    for h in range(H):
        for w in range(W):
            score = 0
            not_min_flag = False  # Permet un court-circuit si le score dépasse le min déjà trouvé
            # Parcourt toutes les autres cases (hors ligne h et colonne w)
            for _h in range(H):
                if _h == h:
                    continue
                for _w in range(W):
                    if _w == w:
                        continue
                    # Ajoute au score : valeur de la case * distance minimale à (h, w)
                    score += intersections[_h][_w] * min(abs(h - _h), abs(w - _w))
                    # Si le score dépasse le minimum actuel, on arrête pour cette position
                    if score > min_score:
                        not_min_flag = True
                        break
                if not_min_flag:
                    break
            # Mise à jour du score minimal si un meilleur score est trouvé
            if score < min_score:
                min_score = score
    return min_score

def main():
    """
    Fonction principale :
    - Lit les entrées
    - Calcule le score minimal
    - Affiche ce score
    """
    H, W, intersections = read_input()
    min_score = calculate_min_score(H, W, intersections)
    print(min_score)

if __name__ == "__main__":
    main()