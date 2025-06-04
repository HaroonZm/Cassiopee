# Résolution complète du problème des 8 reines avec contraintes initiales

# La stratégie est d'utiliser un backtracking :
# 1. On initialise le plateau avec les reines déjà placées.
# 2. On garde en mémoire les colonnes, diagonales principales et secondaires déjà occupées par ces reines.
# 3. On place les reines restantes ligne par ligne en respectant les contraintes.
# 4. Lorsqu'on trouve une solution valide, on l'affiche.

# Comme il y a exactement une solution, on peut stopper la recherche dès qu'on la trouve.

# Voici le code :

def solve_8_queens_with_fixed_queens():
    # Lecture du nombre de reines déjà placées
    k = int(input())
    
    # Plateau initialisé avec des '.' (cases vides)
    board = [['.' for _ in range(8)] for _ in range(8)]
    
    # Ensembles pour garder trace des colonnes et diagonales occupées
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    
    # Rangs déjà placés (pour gérer les lignes)
    fixed_rows = set()
    
    # Placer les reines fixes et remplir les contraintes pour ces positions
    for _ in range(k):
        r, c = map(int, input().split())
        board[r][c] = 'Q'
        cols.add(c)
        diag1.add(r - c)
        diag2.add(r + c)
        fixed_rows.add(r)
    
    # Fonction recursive pour placer les reines
    # row : ligne actuelle à traiter
    def backtrack(row):
        # Si on a placé les reines jusqu'à la ligne 8, la solution est complète
        if row == 8:
            return True
        
        # Si cette ligne a déjà une reine fixe, on passe à la suivante
        if row in fixed_rows:
            return backtrack(row + 1)
        
        # On essaye de placer la reine sur chaque colonne possible
        for c in range(8):
            if (c not in cols) and ((row - c) not in diag1) and ((row + c) not in diag2):
                # Placer la reine
                board[row][c] = 'Q'
                cols.add(c)
                diag1.add(row - c)
                diag2.add(row + c)
                
                # Appel récursif pour la ligne suivante
                if backtrack(row + 1):
                    return True
                
                # Si ça ne mène pas à une solution, on retire la reine
                board[row][c] = '.'
                cols.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)
        
        # Aucune position valide sur cette ligne
        return False
    
    # Lancer la recherche à la ligne 0
    backtrack(0)
    
    # Affichage final du plateau
    for row in board:
        print("".join(row))
        

# Appeler la fonction pour exécuter la résolution
solve_8_queens_with_fixed_queens()