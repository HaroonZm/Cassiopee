def compute_max_dominoes(h: int, w: int) -> int:
    """
    Calcule le nombre maximal de dominos 2x1 pouvant être placés sur une grille de taille h x w sans chevauchement.
    
    Les dominos couvrent chacun deux cases adjacentes de la grille. Le but est de couvrir le maximum de cases 
    en utilisant des dominos entiers.

    Args:
        h (int): nombre de lignes de la grille.
        w (int): nombre de colonnes de la grille.

    Returns:
        int: nombre maximal de dominos qui peuvent être placés sur la grille.
    """
    # Si la grille n'a qu'une ligne ou qu'une colonne, traiter le cas spécial :
    # pour une grille 1x1 ou 1xn ou nx1, on ne peut placer qu'un seul domino si la taille totale >= 2, sinon zéro.
    # Si la grille a au moins 2 lignes ET 2 colonnes, placer le nombre maximum de dominos possible (surface // 2).
    # La division entière renvoie combien de dominos complets peuvent être placés.
    if h > 1 and w > 1:
        return (h * w) // 2
    else:
        # Pour les tableaux 1xN ou Nx1, on ne peut placer qu'un domino si la surface est supérieure ou égale à 2.
        # sum(divmod(h*w, 2)) donne (h*w)//2 + (h*w)%2, càd 1 si surface=1, sinon quantité de dominos.
        surface = h * w
        return sum(divmod(surface, 2))

def main():
    """
    Fonction principale: lit l'entrée utilisateur, calcule et affiche le nombre maximal de dominos.
    """
    # Lecture des dimensions de la grille : deux entiers séparés par un espace.
    h, w = map(int, input().split())
    # Calcul et affichage du nombre maximal de dominos pouvant être placés.
    print(compute_max_dominoes(h, w))

# Appel de la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()