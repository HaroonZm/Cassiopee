import sys

sys.setrecursionlimit(10**7)

def main():
    while True:
        # Lecture de la largeur (W) et de la hauteur (H) du matrix
        W, H = map(int, sys.stdin.readline().split())
        if W == 0 and H == 0:
            break  # Fin des données

        matrix = [list(sys.stdin.readline().strip()) for _ in range(H)]

        # Memoization pour stocker le plus grand nombre possible à partir de chaque position
        dp = [[None]*W for _ in range(H)]

        def is_digit(c):
            return '0' <= c <= '9'

        # Recherche du plus grand nombre qui peut débuter en (r, c)
        def dfs(r, c):
            if dp[r][c] is not None:
                return dp[r][c]

            current_char = matrix[r][c]
            # Par hypothèse, on appelle dfs seulement sur un caractère chiffre

            candidates = []

            # Vérifier si on peut aller à droite
            if c+1 < W and is_digit(matrix[r][c+1]):
                candidates.append(dfs(r, c+1))

            # Vérifier si on peut aller en bas
            if r+1 < H and is_digit(matrix[r+1][c]):
                candidates.append(dfs(r+1, c))

            # Si aucun mouvement possible, nombre maximal est juste le chiffre actuel
            if not candidates:
                dp[r][c] = current_char
                return dp[r][c]

            # Sinon, construire le plus grand nombre possible en concaténant ce chiffre au
            # plus grand parmi les suites possibles
            # On choisit la chaîne la plus grande en valeur numérique (en comparant string comme int)
            best_next = max(candidates, key=lambda x: int(x))
            dp[r][c] = current_char + best_next
            return dp[r][c]

        max_number = None
        # On parcourt toute la matrice et on lance dfs sur toutes les positions qui sont des chiffres
        for i in range(H):
            for j in range(W):
                if is_digit(matrix[i][j]):
                    candidate = dfs(i, j)
                    # Suppression des zéros en tête avant comparaison
                    candidate_int = int(candidate)
                    if max_number is None or candidate_int > max_number:
                        max_number = candidate_int

        print(max_number)

if __name__ == '__main__':
    main()