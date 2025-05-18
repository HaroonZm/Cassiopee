from itertools import permutations
from copy import deepcopy
board = [["."] * 8 for _ in range(8)]
N = int(input())

def check(r, c, board):
    # 4つのループで8方向のblockを移動不可にする
    for i in range(8):
        if board[i][c] == "Q": return False
        if board[r][i] == "Q": return False
    for i in range(-8,8):
        if 0 <= i + c < 8 and 0 <= i + r < 8:
            if board[i+r][i+c] == "Q": return False
        if 0 <= c+(-i) < 8 and 0 <= i + r < 8:
            if board[i+r][-i+c] == "Q": return False
    return True

rc = [list(map(int, input().split())) for _ in range(N)]

def main():
    for p in permutations(range(8)):
        tmp = deepcopy(board)
        for i, v in enumerate(p):
            tmp[i][v] = "Q"
        if not all(tmp[rc[i][0]][rc[i][1]] == "Q" for i in range(N)): continue
        judge = True
        for i, v in enumerate(p):
            tmp[i][v] = "."
            if check(i, v, tmp):
                pass
            else:
                judge = False
                break
            tmp[i][v] = "Q"
        if judge: return tmp
       
tmp = main()
for t in tmp:
    print(''.join("Q" if i == "Q" else "." for i in t))