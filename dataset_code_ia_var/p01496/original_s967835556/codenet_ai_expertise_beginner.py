import sys
from collections import deque
from string import ascii_lowercase, ascii_uppercase, digits

def read_input():
    H, W = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(H):
        grid.append(sys.stdin.readline().strip())
    return H, W, grid

def main():
    # On prépare les constantes et helpers
    DIRS = [
        (1, 5, 2, 3, 0, 4),  # Haut : U
        (3, 1, 0, 5, 4, 2),  # Droite : R
        (4, 0, 2, 3, 5, 1),  # Bas : D
        (2, 1, 5, 0, 4, 3),  # Gauche : L
    ]
    RSEQ = (0, 0, 0, 1, 1, 2, 2, 3) * 3
    LABELS = digits + ascii_uppercase + ascii_lowercase
    NB_L = len(LABELS)
    MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Pour faire tourner un dé (ex: rotate([A,B,C,D,E,F], 0|1|2|3))
    def rotate(curr, move):
        return [curr[i] for i in DIRS[move]]

    # Toutes les positions possibles avec rotations
    def generate_all_rotations(dice):
        pos = dice[:]
        for move in RSEQ:
            yield pos
            pos = [pos[i] for i in DIRS[move]]

    def build_dice_graph():
        faces = list(generate_all_rotations([0,1,2,3,4,5]))
        idx_map = {tuple(f): i for i, f in enumerate(faces)}
        transitions = []
        for f in faces:
            options = []
            for d in range(4):
                n = rotate(f, d)
                options.append(idx_map[tuple(n)])
            transitions.append(options)
        return faces, transitions

    H, W, S = read_input()
    faces, transitions = build_dice_graph()
    visited = [[False]*W for _ in range(H)]
    found = []

    # On explore la grille pour trouver les dés à 3 # et 3 lettres/chiffres
    for y in range(H):
        for x in range(W):
            if S[y][x] == '.' or visited[y][x]:
                continue
            face_values = [0]*6
            queue = deque()
            queue.append((x, y, 0))
            visited[y][x] = True
            while queue:
                cx, cy, orient = queue.popleft()
                vface = faces[orient][0]
                c = S[cy][cx]
                if c == '#':
                    face_values[vface] = NB_L
                else:
                    face_values[vface] = LABELS.index(c)
                for d, (dx, dy) in enumerate(MOVES):
                    nx, ny = cx+dx, cy+dy
                    if 0<=nx<W and 0<=ny<H and S[ny][nx] != '.' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny, transitions[orient][d]))
            if face_values.count(NB_L) != 3:
                continue
            for perm in generate_all_rotations(face_values):
                if perm[3] == perm[4] == perm[5] == NB_L:
                    if perm[0] != perm[1] and perm[1] != perm[2] and perm[2] != perm[0]:
                        found.append(tuple(perm[:3]))
                    break

    # Les positions de la grille finale à remplir
    PPP = [
        [0, 3, 4],
        [0, 2, 3],
        [0, 1, 2],
        [0, 4, 1],
        [3, 2, 5],
        [2, 1, 5],
        [1, 4, 5],
        [4, 3, 5],
    ]

    found.sort()
    N = len(found)

    # On cherche par backtracking si on peut remplir la structure avec ces dés
    def rec(pos, used, used_colors, grid_vals):
        if pos == 8:
            return True
        indices = PPP[pos]
        for idx, d in enumerate(found):
            if used[idx]:
                continue
            used[idx] = True
            for rot in range(3):
                fits = True
                assign_vals = []
                for k in range(3):
                    face = indices[k]
                    face_val = d[(rot+k)%3]
                    if grid_vals[face] == -1:
                        if used_colors[face_val]:
                            fits = False
                            break
                    else:
                        if grid_vals[face] != face_val:
                            fits = False
                            break
                if fits:
                    save = []
                    for k in range(3):
                        face = indices[k]
                        face_val = d[(rot+k)%3]
                        if grid_vals[face] == -1:
                            used_colors[face_val] = True
                            save.append(face)
                        grid_vals[face] = face_val
                    if rec(pos+1, used, used_colors, grid_vals):
                        return True
                    # backtrack
                    for face in save:
                        used_colors[grid_vals[face]] = False
                        grid_vals[face] = -1
                    for k in range(3):
                        face = indices[k]
                        if face not in save:
                            grid_vals[face] = grid_vals[face]
            used[idx] = False
        return False

    if N >= 8 and rec(0, [False]*N, [False]*NB_L, [-1]*6):
        print("Yes")
    else:
        print("No")

main()