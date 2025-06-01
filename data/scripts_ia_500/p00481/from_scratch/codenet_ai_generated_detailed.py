from collections import deque

# Nous allons résoudre ce problème en utilisant une approche en plusieurs étapes successives de plus court chemin (BFS).
# L'idée est la suivante :
# 1. Identifier les positions de la source (S) et des fromageries numérotées de 1 à N.
# 2. Partir de la position actuelle (initialement 'S') et utiliser BFS pour trouver le chemin le plus court vers la fromagerie du fromage suivant à manger.
# 3. Mettre à jour la position actuelle à la fromagerie visitée et répéter jusqu'à avoir mangé tous les fromages de 1 à N.
# 4. Somme des distances minimales obtenues à chaque étape est la réponse finale.

# Cette méthode est efficace même pour de grandes dimensions (H, W maximale de 1000),
# car chaque BFS est limité par le labyrinthe et on fait au maximum N (≤ 9) BFS.

# Lecture des entrées
H, W, N = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Positions des points d'intérêt : S, puis forgeries 1..N
positions = dict()

for i in range(H):
    for j in range(W):
        c = grid[i][j]
        if c == 'S':
            positions[0] = (i, j)  # position de départ
        elif c in '123456789':
            positions[int(c)] = (i, j)  # position des fromageries

# Déplacements possibles (4 directions)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start, goal):
    """Effectue une BFS depuis start jusqu'à goal dans la grille,
       retourne la distance minimale (en nombre de déplacements) entre les deux."""
    visited = [[False]*W for _ in range(H)]
    queue = deque()
    
    si, sj = start
    gi, gj = goal
    
    queue.append((si, sj, 0))
    visited[si][sj] = True
    
    while queue:
        i, j, dist = queue.popleft()
        if (i, j) == (gi, gj):
            return dist
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < H and 0 <= nj < W:
                if not visited[ni][nj]:
                    if grid[ni][nj] != 'X':  # obstacle interdit
                        visited[ni][nj] = True
                        queue.append((ni, nj, dist+1))
    # Le problème garantit la solution, donc on ne doit pas arriver ici.
    return -1

# Calculer la distance totale en visitant les fromageries dans l'ordre 1,2,...,N
total_time = 0
current_pos = positions[0]

for cheese_num in range(1, N+1):
    target_pos = positions[cheese_num]
    dist = bfs(current_pos, target_pos)
    total_time += dist
    current_pos = target_pos  # Mise à jour de la position actuelle après avoir mangé ce fromage
    # La condition sur la force du rat est implicitement respectée puisque le rat mange dans l'ordre croissant
    # et son endurance augmente de 1 après chaque fromage.

print(total_time)