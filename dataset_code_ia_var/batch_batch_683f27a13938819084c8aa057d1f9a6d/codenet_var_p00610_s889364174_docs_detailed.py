"""
AOJ 1024 Cleaning Robot 2.0
Ce programme simule le comportement d'un robot de nettoyage sur une grille carrée. À chaque configuration d'entrée,
le programme détermine la disposition finale sur la grille à partir d'un encodage initial, puis affiche le résultat.
"""

# Mouvement pour 4 directions : haut, droite, bas, gauche
mv = ((-1, 0), (0, 1), (1, 0), (0, -1))

# Dictionnaire de conversion d'état de cellule vers son affichage
d2c = {0: '.', 1: 'E'}

def decode_first_row(k, n):
    """
    Décode l'entier k pour obtenir la configuration de la première ligne de la grille.
    
    Args:
        k (int): Valeur de l'encodage.
        n (int): Taille de la grille (nombre de colonnes).
        
    Returns:
        list: Liste indiquant l'état (0 ou 1) de chaque cellule de la première ligne.
    """
    n1 = n - 1
    row = []
    for c in range(n):
        # Extrait le bit correspondant à la position courante
        bit = (k >> ((n1 - c) >> 1)) & 1
        row.append(bit)
    return row

def compute_next_row(arr, r, n):
    """
    Calcule la ligne suivante en fonction de la ligne précédente selon
    la règle de voisinage suivante : Pour chaque cellule, si exactement
    deux voisins de même type alors inversion de la valeur, sinon conservation.
    
    Args:
        arr (list): Grille partiellement remplie jusqu'à la ligne courante.
        r (int): Numéro de la ligne précédente.
        n (int): Taille de la grille.
    
    Returns:
        list: Nouvelle ligne calculée.
    """
    next_row = []
    for c in range(n):
        cell_value = arr[r][c]
        same_type_neighbors = 0
        # Pour les 4 directions (haut, droite, bas, gauche)
        for i in range(4):
            nr = r + mv[i][0]
            nc = c + mv[i][1]
            # On vérifie que le voisin est dans la grille et appartient au même type
            if 0 <= nr < len(arr) and 0 <= nc < n and arr[nr][nc] == cell_value:
                same_type_neighbors += 1
        # Application de la règle : inversion si 2 voisins similaires, sinon conservation
        next_row.append(1 - cell_value if same_type_neighbors == 2 else cell_value)
    return next_row

def print_grid(arr, n):
    """
    Affiche la grille résultat avec la correspondance des symboles.
    
    Args:
        arr (list): Grille finale avec états (0 ou 1).
        n (int): Taille de la grille.
    """
    for r in range(n):
        print(''.join([d2c[arr[r][c]] for c in range(n)]))
    print()  # Ligne vide après chaque grille

def process_simulation():
    """
    Boucle principale. Gère la lecture des entrées, les vérifications de contraintes,
    l'appel des autres fonctions, et la gestion des sorties.
    """
    while True:
        # Lecture des dimensions et du code d'encodage de la première ligne
        n, k = map(int, input().split())
        if n == 0:
            break  # Fin de l'entrée
        k -= 1   # Encodage de la première ligne est base 1 -> on passe à base 0
        n1 = n - 1
        
        # Vérification des contraintes, sinon on sort
        if (n & 1) or k >= (1 << (n >> 1)):
            print("No\n")
            continue
        
        # Initialisation de la grille avec des valeurs non assignées (-1)
        arr = [[-1 for _ in range(n)] for _ in range(n)]
        # Génération de la première ligne depuis l'encodage k
        arr[0] = decode_first_row(k, n)
        
        # Génération de chaque ligne suivante selon la règle
        for r in range(n1):
            arr[r+1] = compute_next_row(arr, r, n)
        
        # Affichage du résultat
        print_grid(arr, n)

# Lancement du programme principal
process_simulation()