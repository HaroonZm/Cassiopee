import sys
sys.setrecursionlimit(1000000)  # J'espère que c'est suffisant !
H, W = map(int, input().split())
S = []
for _ in range(H):
    # On pourrait écrire directement S = [list(input()) for _ in range(H)]
    # mais ça marche comme ça aussi
    line = input()
    # Pas obligé d'utiliser une liste de caractères, mais bon
    S.append([ch for ch in line])

B = []  # Pour garder les cases déjà visitées
for _ in range(H):
    B.append([False] * W)

# J'ai pas trop compris à quoi servent toutes ces listes mais on suit l'énoncé
R = [['6', '3', '1', '4'], ['1', '3', '6', '4']]
C = [['6', '2', '1', '5'], ['1', '2', '6', '5']]
G = [
    ['6', '3', '1', '4'],
    ['2', '-1', '2', '-1'],
    ['1', '3', '6', '4'],
    ['5', '-1', '5', '-1']
]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    # Franchement, j'ai toujours un doute sur l'ordre des conditions
    if y < 0 or y >= H or x < 0 or x >= W:
        return
    if S[y][x] == '#':
        return
    if B[y][x]:
        return

    m4y = y % 4
    m4x = x % 4
    if S[y][x] != G[m4y][m4x]:
        return

    # Ces conditions commentées servent plus à rien ?
    # Enfin bref, je les laisse au cas où
    # if y % 2 == 0:
    #     if not(y % 4 != 0 or (y % 4 == 0 and S[y][x] == R[0][x % 4])):
    #         return
    #     if not(y % 4 != 2 or (y % 4 == 2 and S[y][x] == R[1][x % 4])):
    #         return
    # if y % 2 == 1:
    #     if not(y % 4 != 1 or (y % 4 == 1 and S[y][x] == '2')):
    #         return
    #     if not(y % 4 != 3 or (y % 4 == 3 and S[y][x] == '5')):
    #         return

    B[y][x] = True

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        dfs(ny, nx)

dfs(0, 0)
# print(B)  # Afficher pour debug mais c'est un peu moche
if B[H-1][W-1]:
    print("YES")
else:
    print("NO")