import sys
sys.setrecursionlimit(10**6)
H, W = map(int, input().split())
S = [[c for c in input()] for _ in range(H)]
B = [[False] * W for _ in range(H)]

R = [['6', '3', '1', '4'], ['1', '3', '6', '4']]
C = [['6', '2', '1', '5'], ['1', '2', '6', '5']]
G = [['6', '3', '1', '4'], ['2', '-1', '2', '-1'],
     ['1', '3', '6', '4'], ['5', '-1', '5', '-1']]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    if y < 0 or H <= y or x < 0 or W <= x:
        return
    if S[y][x] == '#':
        return
    if B[y][x] == True:
        return

    m4y = y % 4
    m4x = x % 4

    if S[y][x] != G[m4y][m4x]:
        return

    # R
    # if y % 2 == 0:
    #    if not(y % 4 != 0 or y % 4 == 0 and S[y][x] == R[0][x % 4]):
    #        return
    #    if not(y % 4 != 2 or y % 4 == 2 and S[y][x] == R[1][x % 4]):
    #        return
    # C
    # if y % 2 == 1:
    #    if not(y % 4 != 1 or y % 4 == 1 and S[y][x] == '2'):
    #        return
    #    if not(y % 4 != 3 or y % 4 == 3 and S[y][x] == '5'):
    #        return

    B[y][x] = True

    for i in range(4):
        dfs(y+dy[i], x+dx[i])

dfs(0, 0)
#print(*B, sep='\n')
print('YES' if B[H-1][W-1] else 'NO')