# Solution complète en Python avec commentaires détaillés

def max_consecutive_ones(grid, n):
    """
    Calcule le plus grand nombre de 1 consécutifs dans une grille nxn
    dans les directions horizontale, verticale et diagonales (2 directions).
    
    Args:
    - grid: liste de chaînes, chaque chaîne représentant une ligne de la grille
    - n: taille de la grille (n x n)
    
    Retourne:
    - un entier représentant le nombre maximal de 1 consécutifs
    """
    max_len = 0
    
    # Vérification horizontale
    for i in range(n):
        count = 0
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
    
    # Vérification verticale
    for j in range(n):
        count = 0
        for i in range(n):
            if grid[i][j] == '1':
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
    
    # Vérification diagonale descendante (de haut-gauche vers bas-droite)
    # On parcourt toutes les diagonales possibles où la différence i-j est constante
    for diff in range(-n+1, n):
        count = 0
        # i valide entre 0 et n-1, j = i - diff
        for i in range(n):
            j = i - diff
            if 0 <= j < n:
                if grid[i][j] == '1':
                    count += 1
                    max_len = max(max_len, count)
                else:
                    count = 0
        # Réinit à chaque diagonale
    
    # Vérification diagonale montante (de bas-gauche vers haut-droite)
    # Ces diagonales ont somme i+j constante entre 0 et 2n-2
    for s in range(2*n -1):
        count = 0
        # i varie de max(0, s-(n-1)) à min(n-1, s)
        start_i = max(0, s - (n -1))
        end_i = min(n-1, s)
        for i in range(start_i, end_i+1):
            j = s - i
            if grid[i][j] == '1':
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
    
    return max_len

def main():
    """
    Lecture des multiples jeux de données jusqu'à la ligne '0'.
    Pour chaque jeu de données, on calcule la plus grande chaîne de 1 consécutifs
    et on affiche le résultat.
    """
    while True:
        line = input().strip()
        if line == '0':
            break
        n = int(line)
        grid = []
        for _ in range(n):
            row = input().strip()
            grid.append(row)
        
        result = max_consecutive_ones(grid, n)
        print(result)

if __name__ == "__main__":
    main()