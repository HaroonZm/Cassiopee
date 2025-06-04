import sys  # Importe le module sys, qui fournit accès à des variables et fonctions utilisées ou maintenues par l’interpréteur Python.

# Redéfinit la fonction input() pour qu'elle lise une ligne depuis l'entrée standard (habituellement utile pour la lecture rapide de grandes entrées, comme lors de concours de programmation).
input = sys.stdin.readline

# Modifie la limite maximale de récursion du programme à 10**9 (un milliard), ce qui peut être nécessaire si le programme utilise de la récursion profonde.
sys.setrecursionlimit(10**9)

# Lit une ligne depuis l'entrée, la découpe par défaut sur les espaces, convertit chaque morceau en entier, puis assigne les deux valeurs respectivement à h (hauteur) et w (largeur).
h, w = map(int, input().split())

# Lit h lignes du plateau depuis l'entrée.
# Pour chaque valeur comprise entre 0 et h-1 (les lignes), lit une chaîne depuis l'entrée,
# ce qui construit une liste de chaînes s de longueur h. Chaque élément de s correspond à une ligne du plateau.
s = [input() for _ in range(h)]

# Crée une table memo (pour "mémoization") qui va mémoriser l'état de visite des cases du plateau.
# Il s'agit d'une liste de listes de taille h x w, initialisée à 0 (ce qui signifie que la case n'a pas encore été visitée).
memo = [[0] * w for _ in range(h)]

# Crée une liste représentant les 4 directions cardinales, chaque paire (dx, dy) correspondant à un déplacement :
# (0, 1) : déplacement d'une case vers la droite
# (0, -1) : déplacement d'une case vers la gauche
# (1, 0) : déplacement d'une case vers le bas
# (-1, 0) : déplacement d'une case vers le haut
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Déclaration de la fonction de recherche en profondeur (dfs = Depth-First Search)
# Cette fonction explore récursivement les cases adjacentes du plateau en respectant certaines règles.
# Paramètres :
#   i     : numéro de la ligne de la case actuelle
#   j     : numéro de la colonne de la case actuelle
#   color : le caractère censé être différent de la case visée pour autoriser le déplacement (utilisé pour alterner entre '.' et '#')
def dfs(i, j, color):
    # Vérifie si la position (i, j) se situe en dehors des bornes du plateau (hors de la grille)
    # Le plateau a des lignes indexées de 0 à h-1 et des colonnes de 0 à w-1
    if not (0 <= i <= h-1 and 0 <= j <= w-1):
        # Si la case est hors du plateau, on retourne (0, 0) puisque rien n'est trouvé
        return 0, 0
    
    # Si memo[i][j] vaut 1, cela signifie que la case (i, j) a déjà été visitée et fait déjà partie d'un composant traité
    if memo[i][j] == 1:
        return 0, 0

    # Si la couleur de la case en cours est égale à la couleur interdite 'color', on ne traite pas cette case (pour éviter de revisiter la même couleur dans une même composante).
    if s[i][j] == color:
        return 0, 0

    # Marque la case courante (i, j) comme visitée en l'indiquant dans la table 'memo'
    memo[i][j] = 1

    # Initialisation des compteurs white et black, qui compteront le nombre respectif de cases blanches ('.') et noires ('#') connectées dans cette composante
    white, black = 0, 0

    # Si la case courante est blanche ('.'), incrémente le compteur de cases blanches
    if s[i][j] == ".":
        white += 1
    else:
        # Sinon, incrémente le compteur de cases noires ('#')
        black += 1

    # Pour chaque direction possible (droite, gauche, bas, haut)
    for dx, dy in dir:
        # Appelle récursivement dfs sur la case adjacente dans cette direction
        # Le paramètre color prend la valeur de la couleur de la case courante, pour éviter la propagation sur des cases de la même couleur
        cur_w, cur_b = dfs(i + dx, j + dy, s[i][j])

        # Ajoute les valeurs (nombre de cases blanches et noires trouvées dans la direction explorée)
        white += cur_w
        black += cur_b

    # Retourne le total trouvé pour cette composante connectée : nombre de blancs et de noirs
    return white, black

# Initialise le résultat final (variable ans) à 0.
# Cette variable accumulera les produits du nombre de cases blanches et noires pour chaque composante,
# ce qui correspond au nombre total de paires blanches/noires adjacentes dans le plateau.
ans = 0

# Parcourt toutes les cases du plateau à l'aide de deux boucles imbriquées,
# la première (i) parcourt chaque ligne (de 0 à h-1), la seconde (j) chaque colonne (de 0 à w-1)
for i in range(h):
    for j in range(w):
        # Si la case courante est blanche (contient '.')
        if s[i][j] == ".":
            # On démarre une exploration dfs pour cette case en interdisant la couleur noire ('#')
            white, black = dfs(i, j, "#")
        else:
            # Si la case courante est noire ('#'), on démarre dfs en interdisant le blanc ('.')
            white, black = dfs(i, j, ".")

        # À la fin de chaque composante, ajoute à ans le produit white * black.
        # Cela compte le nombre d'arrêtes bicolores pour cette composante (chaque composante connectée qui alterne blanc/noir).
        ans += white * black

# Affiche finalement le résultat total, qui est le nombre de paires adjacentes entre une case blanche et une case noire pour l'ensemble du plateau.
print(ans)