from sys import stdin

def read_input():
    return list(map(int, stdin.readline().split()))

n_rows, n_cols, n_query = read_input()
grille = []
i = 0
while i < n_rows:
    grille.append(stdin.readline().strip())
    i += 1

nod = []
edgex = []
edgey = []
nod.append([0] * (n_cols + 1))
edgex.append([0 for _ in range(n_cols)])
edgey.append([0] * (n_cols + 1))

for p in range(1, n_rows + 1):
    N_row = [0]
    ex = [0]
    ey = [0]
    j = 1
    while j <= n_cols:
        incr = 1 if grille[p-1][j-1] == '1' else 0
        N_row.append(N_row[-1] + nod[p-1][j] - nod[p-1][j-1] + incr)
        if j < n_cols:
            if grille[p-1][j-1] == '1' and grille[p-1][j] == '1':
                ex.append(ex[-1] + edgex[p-1][j] - edgex[p-1][j-1] + 1)
            else:
                ex.append(ex[-1] + edgex[p-1][j] - edgex[p-1][j-1])
        if p < n_rows:
            eyVal = 0
            if grille[p-1][j-1] == "1" and grille[p][j-1] == "1":
                eyVal = 1
            ey.append(ey[-1] + edgey[p-1][j] - edgey[p-1][j-1] + eyVal)
        j += 1
    nod.append(N_row)
    edgex.append(ex)
    if p < n_rows:
        edgey.append(ey)

q=0
while q<n_query:
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    num = nod[x2][y2] - nod[x1-1][y2] - nod[x2][y1-1] + nod[x1-1][y1-1]
    ey_count = edgey[x2-1][y2] - edgey[x1-1][y2] - edgey[x2-1][y1-1] + edgey[x1-1][y1-1]
    ex_count = edgex[x2][y2-1] - edgex[x1-1][y2-1] - edgex[x2][y1-1] + edgex[x1-1][y1-1]
    total = ex_count + ey_count
    # Résultat par soustraction
    result = num - total
    print(result)
    q += 1