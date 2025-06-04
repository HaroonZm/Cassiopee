import sys

# Redéfinir la fonction input pour une lecture plus rapide sur l'entrée standard.
input = sys.stdin.readline

# Augmenter la limite de récursion pour éviter les erreurs lors de DFS profonds.
sys.setrecursionlimit(10**9)

# Lecture des dimensions de la grille.
h, w = map(int, input().split())

# Lecture du contenu de la grille sous forme de liste de chaînes (une par ligne).
s = [input().strip() for _ in range(h)]

# Création d'une matrice de mémoïsation pour marquer les cases déjà visitées.
memo = [[0] * w for _ in range(h)]

# Liste des directions de déplacement : droite, gauche, bas, haut.
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j, color):
    """
    Effectue une recherche en profondeur (DFS) à partir de la case (i, j), alternant entre deux couleurs.
    Ne visite que les cases contiguës d'une composante où deux couleurs alternent à chaque déplacement.
    
    Args:
        i (int): Indice de ligne courant dans la grille.
        j (int): Indice de colonne courant dans la grille.
        color (str): Couleur de la case précédente à comparer ('.' ou '#') pour assurer l'alternance.

    Returns:
        tuple: (white, black)
            white (int): Nombre de cases blanches ('.') dans la composante explorée.
            black (int): Nombre de cases noires ('#') dans la composante explorée.
    """
    # Vérifie si la position (i, j) est en dehors des bornes de la grille.
    if not (0 <= i <= h - 1 and 0 <= j <= w - 1):
        return 0, 0
    # Vérifie si la case a déjà été visitée.
    if memo[i][j] == 1:
        return 0, 0
    # Vérifie si la couleur actuelle n'est pas différente de la précédente (pour maintenir l'alternance).
    if s[i][j] == color:
        return 0, 0

    # Marque la case actuelle comme visitée.
    memo[i][j] = 1

    # Initialise les compteurs de cases blanches et noires.
    white, black = 0, 0

    # Incrémente le compteur selon la couleur de la case.
    if s[i][j] == ".":
        white += 1
    else:
        black += 1

    # Explore récursivement les cases adjacentes dans chaque direction.
    for dx, dy in dir:
        cur_w, cur_b = dfs(i + dx, j + dy, s[i][j])
        white += cur_w
        black += cur_b

    return white, black

# Initialisation du résultat final.
ans = 0

# Parcours de chaque case de la grille.
for i in range(h):
    for j in range(w):
        # Si la case n'a pas été visitée, lance une DFS à partir de celle-ci pour une nouvelle composante alternée.
        if memo[i][j] == 0:
            # Détermine la couleur opposée à celle de la case courante pour respecter l'alternance.
            if s[i][j] == ".":
                white, black = dfs(i, j, "#")
            else:
                white, black = dfs(i, j, ".")

            # Ajoute au résultat : pour chaque composante, le nombre de paires possibles (produit des blancs et noirs).
            ans += white * black

# Affiche le résultat final.
print(ans)