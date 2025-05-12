from sys import stdin
N = 8
FREE = -1
NOT_FREE = 1
row = [FREE] * N
col = [FREE] * N
dpos = [FREE] * (2 * N - 1)
dneg = [FREE] * (2 * N - 1)
X = [[False] * N for _ in range(N)]
n = int(stdin.readline())
for _ in range(0, n):
    r, c = map(int, stdin.readline().split())
    X[r][c] = True
def printBoard():
    for i in range(0, N):
        for j in range(0, N):
            if X[i][j] != 0 and row[i] != j: return
    for i in range(0, N):
        for j in range(0, N):
            print("Q" if row[i] == j else ".", end="")
        print("")
def recursive(i):
    if i == N:
        printBoard()
        return
    for j in range(0, N):
        if (NOT_FREE == col[j] or
            NOT_FREE == dpos[i + j] or
            NOT_FREE == dneg[i - j + N - 1]): continue
        row[i] = j
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE
        recursive(i + 1)
        row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE
recursive(0)