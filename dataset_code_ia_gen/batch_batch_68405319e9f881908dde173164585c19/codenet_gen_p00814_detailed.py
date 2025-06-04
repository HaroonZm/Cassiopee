# Solution complète pour le problème "Life Line"

# Approche générale :
# 1. Lecture de la configuration du plateau triangulaire.
# 2. Simulation du placement d'une pierre pour le joueur C sur chaque sommet vide.
# 3. Identification des groupes de pierres (mêmes numéros, connexes).
# 4. Vérification des groupes sans sommets vides adjacents pour suppression.
# 5. Calcul du score (pierres adverses supprimées - pierres du joueur supprimées).
# 6. Choix du placement donnant le score maximal.
# 7. Répétition pour chaque cas jusqu'à la détection de la fin d'entrée (0 0).

# Détails clés :
# - Le plateau est un triangle avec N lignes, chaque ligne i contient i sommets.
# - Chaque sommet peut être adjacents à plusieurs sommets, suivant l'agencement triangulaire.
# - On modélise le plateau en listant les voisins de chaque sommet.
# - On utilise BFS/DFS pour trouver les groupes.
# - La suppression ne se fait que si aucun sommet du groupe n'est adjacent à un sommet vide.

import sys
sys.setrecursionlimit(10000)

def read_board(N):
    board = []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        # Vérification du bon format (i+1 sommets)
        if len(line) != i + 1:
            raise ValueError("Format d'entrée incorrect")
        board.append(line)
    return board

def get_neighbors(N):
    # Calcule et retourne une liste de voisins pour chaque sommet
    # Chaque sommet identifié par (i,j), 0 <= j <= i < N
    # La structure est un dictionnaire: (i,j) -> [(ni,nj), ...]
    neighbors = {}
    for i in range(N):
        for j in range(i+1):
            adj = []
            # 6 directions possibles dans la grille triangulaire (maximum)
            # 1) sommet à gauche (i, j-1) si j>0
            if j > 0:
                adj.append((i, j-1))
            # 2) sommet à droite (i, j+1) si j < i
            if j < i:
                adj.append((i, j+1))
            # 3) sommet en haut à gauche (i-1, j-1) si i>0 et j>0
            if i > 0 and j > 0:
                adj.append((i-1, j-1))
            # 4) sommet en haut à droite (i-1, j) si i>0
            if i > 0 and j <= i-1:
                adj.append((i-1, j))
            # 5) sommet en bas à gauche (i+1, j) si i < N-1
            if i < N-1 and j <= i:
                adj.append((i+1, j))
            # 6) sommet en bas à droite (i+1, j+1) si i < N-1 et j < i+1
            if i < N-1 and j+1 <= i+1:
                adj.append((i+1, j+1))
            neighbors[(i,j)] = adj
    return neighbors

def find_groups(board, neighbors):
    # Renvoie une liste de groupes
    # Chaque groupe est une liste de positions (i,j) ayant le même numéro et étant connectés
    N = len(board)
    visited = [[False]*(i+1) for i in range(N)]
    groups = []
    for i in range(N):
        for j in range(i+1):
            if board[i][j] != 0 and not visited[i][j]:
                stone_number = board[i][j]
                stack = [(i,j)]
                group_positions = []
                visited[i][j] = True
                while stack:
                    ci,cj = stack.pop()
                    group_positions.append((ci,cj))
                    for ni,nj in neighbors[(ci,cj)]:
                        if 0 <= ni < N and 0 <= nj <= ni:
                            if board[ni][nj] == stone_number and not visited[ni][nj]:
                                visited[ni][nj] = True
                                stack.append((ni,nj))
                groups.append( (stone_number, group_positions) )
    return groups

def has_empty_adjacent(group_positions, board, neighbors):
    # Détermine si un groupe possède au moins un sommet adjacent vide (0)
    for (i,j) in group_positions:
        for (ni,nj) in neighbors[(i,j)]:
            if 0 <= ni < len(board) and 0 <= nj <= ni:
                if board[ni][nj] == 0:
                    return True
    return False

def simulate_turn(board, neighbors, player):
    # Pour chaque sommet vide, simule la pose de la pierre du joueur, calcule le score, renvoie la valeur max
    N = len(board)
    max_score = -10**9  # assez petit pour minimum
    placed_any = False

    for i in range(N):
        for j in range(i+1):
            if board[i][j] == 0:
                # Copie du plateau
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                placed_any = True

                # Calcule les groupes
                groups = find_groups(new_board, neighbors)

                # Cherche les groupes à supprimer (sans sommet adjacent vide)
                remove_groups = []
                for stone_num,pos_list in groups:
                    if not has_empty_adjacent(pos_list, new_board, neighbors):
                        remove_groups.append((stone_num, pos_list))

                # Calcul du score
                gain = 0
                lose = 0
                # Supprimer les pierres
                for stone_num, pos_list in remove_groups:
                    count = len(pos_list)
                    if stone_num == player:
                        lose += count
                    else:
                        gain += count
                    for (pi,pj) in pos_list:
                        new_board[pi][pj] = 0  # supprime les pierres
                score = gain - lose
                if score > max_score:
                    max_score = score

    # Si aucun placement possible (très improbable car au moins un sommet vide)
    # On retourne 0 par défaut (pas de score)
    if not placed_any:
        return 0
    return max_score

def main():
    neighbors_cache = {}
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        if line.strip() == '0 0':
            break
        N,C = map(int,line.strip().split())
        board = read_board(N)
        if N not in neighbors_cache:
            neighbors_cache[N] = get_neighbors(N)
        neighbors = neighbors_cache[N]
        res = simulate_turn(board, neighbors, C)
        print(res)

if __name__ == "__main__":
    main()