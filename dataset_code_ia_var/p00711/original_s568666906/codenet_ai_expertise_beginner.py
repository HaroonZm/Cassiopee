def solve(dat):
    # On calcule la hauteur et la largeur
    H = len(dat)
    W = len(dat[0])
    
    # On cherche la position de départ '@'
    for i in range(H):
        for j in range(W):
            if dat[i][j] == "@":
                start_i = i
                start_j = j

    # On crée une grille pour marquer les cases visitées
    visited = []
    for i in range(H):
        visited.append([0] * W)
    
    # Les mouvements : haut, bas, gauche, droite
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    
    # On met la case de départ
    to_visit = [(start_i, start_j)]
    
    while len(to_visit) > 0:
        i, j = to_visit.pop()
        visited[i][j] = 1
        for k in range(4):
            ni = i + d_row[k]
            nj = j + d_col[k]
            if 0 <= ni < H and 0 <= nj < W:
                if dat[ni][nj] == "." and visited[ni][nj] == 0:
                    to_visit.append((ni, nj))
    
    # On compte les cases visitées
    count = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j]:
                count += 1
    return count

while True:
    line = raw_input()
    W_H = line.split()
    W = int(W_H[0])
    H = int(W_H[1])
    if W == 0 and H == 0:
        break
    dat = []
    for i in range(H):
        dat.append(raw_input())
    print solve(dat)