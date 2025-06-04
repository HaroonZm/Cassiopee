# Solution complète en Python avec commentaires détaillés pour le problème "英語の勉強"

from collections import defaultdict

# Directions possibles pour du voisinage 8-directions (horizontal, vertical, diagonale)
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def inside_board(x, y):
    """Vérifie si les coordonnées (x, y) sont bien dans la grille 4x4"""
    return 0 <= x < 4 and 0 <= y < 4

def dfs(board, word, idx, x, y, visited):
    """
    Recherche récursive (profondeur) d'un chemin correspondant au mot `word`,
    à partir de la position (x,y) sur le plateau `board`.
    `idx` est la position actuelle dans `word` que l'on doit vérifier,
    `visited` est un set des positions déjà parcourues.
    Renvoie True si on peut terminer le mot depuis cette position, sinon False.
    """
    if idx == len(word):
        # Mot entièrement trouvé
        return True

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if inside_board(nx, ny) and (nx, ny) not in visited and board[nx][ny] == word[idx]:
            visited.add((nx, ny))
            if dfs(board, word, idx+1, nx, ny, visited):
                return True
            visited.remove((nx, ny))
    return False

def find_all_paths(board, word):
    """
    Trouve toutes les façons différentes (différents chemins) de parcourir le mot `word` sur `board`.
    Renvoie une liste de tuples représentant les chemins (listes de coordonnées).
    """
    paths = []

    def dfs_paths(idx, x, y, visited, path):
        if idx == len(word):
            # Chemin complet trouvé
            paths.append(tuple(path))
            return
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if inside_board(nx, ny) and (nx, ny) not in visited and board[nx][ny] == word[idx]:
                visited.add((nx, ny))
                path.append((nx, ny))
                dfs_paths(idx+1, nx, ny, visited, path)
                path.pop()
                visited.remove((nx, ny))

    # Pour chaque position possible du premier caractère
    for i in range(4):
        for j in range(4):
            if board[i][j] == word[0]:
                visited = set([(i, j)])
                dfs_paths(1, i, j, visited, [(i, j)])

    return paths

def main():
    import sys
    input = sys.stdin.readline

    # Lecture du nombre de mots du dictionnaire
    N = int(input())
    dictionary = {}
    for _ in range(N):
        line = input().split()
        word, score = line[0], int(line[1])
        dictionary[word] = score

    # Lecture de la grille 4x4
    board = [list(input().strip()) for _ in range(4)]

    # Temps limite T
    T = int(input())

    # Pour chaque mot, on trouve toutes les manières différentes (chemins uniques) de le parcourir
    # On veut retrouver pour chaque mot la liste des chemins (chaque chemin une séquence de coordonnées).
    # Puis, on va créer une liste de "items" : (temps, score) par occurrence unique trouvée.
    # Ensuite, on résoud un problème de sac à dos (knapsack) à temps T sur ces items.

    items = []
    for word, score in dictionary.items():
        paths = find_all_paths(board, word)
        length = len(word)  # temps nécessaire = taille du mot (en secondes)
        # Ajouter un item pour chaque chemin unique (pas de redondance)
        # Chaque item est (temps, score)
        for _ in paths:
            items.append((length, score))

    # Problème : max total de points avec temps <= T
    # On résout un knapsack classique où poids = temps, valeur = score.

    dp = [0] * (T+1)
    for cost, value in items:
        # Traitement classique knapsack 0/1
        for time in range(T, cost-1, -1):
            if dp[time - cost] + value > dp[time]:
                dp[time] = dp[time - cost] + value

    print(max(dp))


if __name__ == "__main__":
    main()