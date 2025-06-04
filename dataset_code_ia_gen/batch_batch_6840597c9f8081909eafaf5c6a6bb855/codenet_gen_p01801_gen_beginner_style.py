H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

def to_key(b):
    return tuple(''.join(row) for row in b)

memo = {}

def can_win(b):
    key = to_key(b)
    if key in memo:
        return memo[key]
    # Find all cells that can be chosen (empty '.')
    for i in range(H):
        for j in range(W):
            if b[i][j] == '.':
                # Copy board to simulate move
                nb = [row[:] for row in b]
                # Mark walls upwards
                for ni in range(i, -1, -1):
                    if nb[ni][j] == '#':
                        break
                    nb[ni][j] = '#'
                # Mark walls downwards
                for ni in range(i, H):
                    if nb[ni][j] == '#':
                        break
                    nb[ni][j] = '#'
                # Mark walls leftwards
                for nj in range(j, -1, -1):
                    if nb[i][nj] == '#':
                        break
                    nb[i][nj] = '#'
                # Mark walls rightwards
                for nj in range(j, W):
                    if nb[i][nj] == '#':
                        break
                    nb[i][nj] = '#'
                # If opponent cannot win after this move, current player wins
                if not can_win(nb):
                    memo[key] = True
                    return True
    # If no moves leads to a win, current player loses
    memo[key] = False
    return False

if can_win(board):
    print("First")
else:
    print("Second")