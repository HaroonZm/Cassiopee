def parse_dimensions():
    """
    Lit les dimensions de la grille et la valeur de déplacement 'd' à partir de l'entrée standard.
    
    Returns:
        tuple: Un triplet (h, w, d) où 
            h (int): nombre de lignes de la grille,
            w (int): nombre de colonnes de la grille,
            d (int): valeur maximale de saut (différence d'indice entre deux nombres consécutifs pour le calcul).
    """
    h, w, d = map(int, input().split())
    return h, w, d

def build_index(h, w):
    """
    Construit une table d'index associant chaque entier de la grille à sa position (ligne, colonne).

    Args:
        h (int): Nombre de lignes de la grille.
        w (int): Nombre de colonnes de la grille.

    Returns:
        list: Une liste de tuples où chaque tuple (i, j) représente 
              la position (ligne, colonne) de la valeur correspondante dans la grille.
              L'indice de la valeur dans la liste est la valeur dans la grille.
    """
    # Initialisation de la liste d'index : pour chaque valeur de 1 à h*w, positionnera (ligne, colonne)
    index = [(0, 0) for _ in range(h * w + 1)]
    for i in range(1, h + 1):
        # Lecture de la ligne courante de la grille
        col = list(map(int, input().split()))
        for j in range(1, w + 1):
            # Assignation de la position (i, j) à la valeur col[j-1]
            index[col[j - 1]] = (i, j)
    return index

def compute_memo(h, w, d, index):
    """
    Calcule un tableau mémoïsé 'memo' où chaque case indique la somme des distances
    de type « déplacement en cheval » (par pas de taille d) jusqu'à un certain indice.

    Args:
        h (int): Nombre de lignes.
        w (int): Nombre de colonnes.
        d (int): Saut maximal (nombre d'écart entre deux indices consécutifs pour le calcul).
        index (list): Liste des positions (ligne, colonne) pour chaque valeur de la grille.

    Returns:
        list: Tableau des coûts cumulés pour chaque indice (mémoïsé).
    """
    memo = [0 for _ in range(h * w + 1)]
    # Calculer la somme des distances pour tous les indices, par pas de taille d
    for l in range(1, h * w + 1 - d):
        pos_from = index[l]
        pos_to = index[l + d]
        # Distance de Manhattan entre pos_from et pos_to
        dist = abs(pos_to[0] - pos_from[0]) + abs(pos_to[1] - pos_from[1])
        # On cumule la distance au mémo précédent
        memo[l + d] = memo[l] + dist
    return memo

def process_queries(memo):
    """
    Lit et traite les requêtes, imprime pour chacune la différence de coûts cumulés entre deux indices.

    Args:
        memo (list): Liste des coûts cumulés calculés précédemment.
    """
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        # Calcul de la différence de coût cumulée (distance totale entre l et r par pas de d)
        print(memo[r] - memo[l])

def main():
    """
    Fonction principale orchestrant la lecture de la grille, 
    la préparation de l'indexation et du mémo, puis le traitement des requêtes.
    """
    h, w, d = parse_dimensions()
    index = build_index(h, w)
    memo = compute_memo(h, w, d, index)
    process_queries(memo)

# Point d'entrée du script
if __name__ == "__main__":
    main()