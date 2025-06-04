def compute_dominoes(h: int, w: int) -> int:
    """
    Calcule le nombre maximal de dominos 1x2 pouvant être placés sur une grille h x w,
    selon les règles suivantes :
    - Si la surface totale (h*w) est supérieure ou égale à la somme (h+w), alors on retourne
      le plafond de (h*w / 2) (nombre maximal de dominos).
    - Sinon, on retourne 1 (au moins un domino peut être placé).

    Args:
        h (int): Nombre de lignes de la grille.
        w (int): Nombre de colonnes de la grille.

    Returns:
        int: Nombre maximal de dominos pouvant être placés.
    """
    # Surface totale de la grille
    surface = h * w
    # Somme des côtés
    perimetre = h + w

    # Si la surface est suffisamment grande, calculer le plafond de surface / 2
    if surface >= perimetre:
        # Calcul du plafond sans utiliser math.ceil : -(-a // b)
        nb_dominos = -(-surface // 2)
        return nb_dominos
    else:
        # Sinon, il n'est possible de placer qu'un seul domino
        return 1

if __name__ == "__main__":
    # Lecture des dimensions de la grille en une ligne séparée par un espace
    h, w = map(int, input().split())
    # Affichage du résultat calculé par la fonction compute_dominoes
    print(compute_dominoes(h, w))