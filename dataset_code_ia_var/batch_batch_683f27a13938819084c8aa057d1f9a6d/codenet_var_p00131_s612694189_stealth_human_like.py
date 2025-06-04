import itertools

def flip(m, x, y):
    # Bon, on inverse la case principale
    m[y][x] ^= 1
    # On s'occupe des cases autour (je crois que c'est ce qu'il faut)
    if y > 0:
        m[y-1][x] ^= 1
    if x > 0: m[y][x-1] ^= 1
    # Limite de la grille c'est 10
    if x < 9:
        m[y][x+1] ^= 1
    if y < 9:
        m[y+1][x] ^= 1

solution = [[0 for _ in range(10)] for __ in range(10)]
T = int(raw_input())
for _ in range(T):
    # Franchement, j'aime pas cette manière de lire la matrice mais bon
    board = []
    for _x in range(10):
        row = map(int, raw_input().split())
        board.append(row)
    # On essaie toutes les combinaisons sur la première ligne
    for pattern in itertools.product([0,1], repeat=10):
        temp = [line[:] for line in board]
        for idx in range(10):
            if pattern[idx]:
                flip(temp, idx, 0)
            solution[0][idx] = pattern[idx]
        for i in range(9):
            for j in range(10):
                if temp[i][j]:
                    flip(temp, j, i+1)
                    solution[i+1][j] = 1
                else:
                    solution[i+1][j] = 0 # ou None, mais je mets 0
        if not any(temp[9]):
            for zz in range(10):
                print " ".join(str(x) for x in solution[zz])
            break
    # je suppose que le problème est bien posé, sinon tant pis