import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
mod = 1000000007

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_grid(h):
    grid = []
    for _ in range(h):
        row = sys.stdin.readline().strip()
        grid.append(list(row))
    return grid

def main():
    # Lire les 4 pièces
    pieces = []
    for _ in range(4):
        h, w = read_int_list()
        grid = read_grid(h)
        temp = []
        for i in range(h):
            row = []
            for j in range(w):
                if grid[i][j] == "#":
                    row.append(1)
                else:
                    row.append(0)
            temp.append(row)
        pieces.append(temp)

    H = 4
    W = 10
    patterns = defaultdict(int)

    def copy_table(tab):
        return [row[:] for row in tab]

    def dfs(board, skip_index, count):
        if count == 3:
            pattern_tup = tuple(tuple(row) for row in board)
            patterns[pattern_tup] = 1
            return
        for piece_index in range(4):
            if piece_index == skip_index:
                continue
            p = pieces[piece_index]
            ph = len(p)
            pw = len(p[0])
            for y in range(H - ph + 1):
                for x in range(W - pw + 1):
                    conflict = False
                    # Placement
                    new_board = copy_table(board)
                    for dy in range(ph):
                        for dx in range(pw):
                            if p[dy][dx] == 1:
                                if new_board[y + dy][x + dx] == 1:
                                    conflict = True
                                new_board[y + dy][x + dx] += p[dy][dx]
                        if conflict:
                            break
                    if not conflict:
                        dfs(new_board, piece_index, count + 1)

    # Générer tous les états possibles avec 3 pièces sur le plateau
    for skip in range(4):
        board = [[0] * W for _ in range(H)]
        dfs(board, skip, 0)

    # Lire les configurations à tester
    n = read_int()
    for _ in range(n):
        test_grid = read_grid(H)
        ttuple = []
        for i in range(H):
            temp_row = []
            for j in range(W):
                if test_grid[i][j] == "#":
                    temp_row.append(0)
                else:
                    temp_row.append(1)
            ttuple.append(tuple(temp_row))
        ttuple = tuple(ttuple)
        if patterns[ttuple]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()