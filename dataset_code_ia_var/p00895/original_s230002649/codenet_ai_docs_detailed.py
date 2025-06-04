def get_input_dimensions():
    """
    Lit une paire de dimensions (hauteur et largeur) depuis l'entrée standard.
    Retourne un tuple d'entiers (h, w).
    """
    h, w = map(int, input().split())
    return h, w

def read_grid(h):
    """
    Lit h lignes de texte depuis l'entrée standard pour former la grille.
    Retourne une liste de chaînes de caractères représentant la grille.
    """
    return [input() for _ in range(h)]

def find_least_frequent_string(grid, height, width):
    """
    Parcourt la grille et compte la fréquence de toutes les chaînes formées en partant de chaque
    case dans chacune des 8 directions, en tournant autour de la grille grâce au modulo.
    Retourne la plus longue chaîne qui apparaît au moins 2 fois, en respectant un critère
    de tri (par longueur décroissante puis ordre lexicographique croissant).
    Si aucune chaîne de longueur > 1 n'est valide, retourne 0.

    Args:
        grid (list of str): La grille de caractères.
        height (int): Nombre de lignes de la grille.
        width (int): Nombre de colonnes de la grille.

    Returns:
        str or int: La chaîne trouvée ou 0 si aucune n'est valide.
    """
    # Directions autour d'une case (8 directions cardinales et diagonales)
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    count = {}

    # Parcours de chaque case de la grille
    for i in range(height):
        for j in range(width):
            for dx, dy in directions:
                # Démarrage avec la lettre courante
                s = grid[i][j]
                count[s] = count.get(s, 0) + 1
                x = (j + dx) % width
                y = (i + dy) % height
                # Construction récursive de la chaîne dans cette direction
                while x != j or y != i:
                    s += grid[y][x]
                    count[s] = count.get(s, 0) + 1
                    x = (x + dx) % width
                    y = (y + dy) % height

    # Recherche la chaîne la plus longue apparaissant au moins 2 fois
    # En cas d'égalité, le tie-breaker est l'ordre lexical
    ans = min(count, key=lambda x: (-len(x) * (count[x] > 1), x))
    # Si la chaîne retenue a une longueur > 1, on la retourne, sinon 0
    return ans if len(ans) > 1 else 0

def main():
    """
    Fonction principale du programme.
    Lit les dimensions et la grille, traite chaque cas jusqu'à ce qu'une paire (0, 0) soit lue,
    puis imprime le résultat pour chaque grille.
    """
    while True:
        h, w = get_input_dimensions()
        if h == 0 and w == 0:
            break
        grid = read_grid(h)
        result = find_least_frequent_string(grid, h, w)
        print(result)

if __name__ == "__main__":
    main()