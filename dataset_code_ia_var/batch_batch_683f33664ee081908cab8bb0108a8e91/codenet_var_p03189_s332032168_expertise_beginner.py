import sys

n_q = input().split()
n = int(n_q[0])
q = int(n_q[1])
MOD = 10 ** 9 + 7
INV2 = (MOD + 1) // 2

lines = []
for _ in range(n + q):
    lines.append(sys.stdin.readline())

a_values = []
for i in range(n):
    a_values.append(int(lines[i]))

mat = []
for i in range(n):
    row = []
    for j in range(n):
        if a_values[i] < a_values[j]:
            row.append(1)
        else:
            row.append(0)
    mat.append(row)

for idx in range(n, n + q):
    x_y = lines[idx].split()
    x = int(x_y[0]) - 1
    y = int(x_y[1]) - 1

    tmp = (mat[x][y] + mat[y][x]) * INV2 % MOD

    # Calculer nouvelle ligne x/y
    new_row = []
    for k in range(n):
        val = (mat[x][k] + mat[y][k]) * INV2 % MOD
        new_row.append(val)
    mat[x] = new_row
    mat[y] = new_row[:]

    # Calculer nouvelle colonne x/y
    for k in range(n):
        val = (mat[k][x] + mat[k][y]) * INV2 % MOD
        mat[k][x] = val
        mat[k][y] = val

    mat[x][x] = 0
    mat[y][y] = 0
    mat[x][y] = tmp
    mat[y][x] = tmp

ans = 0
for i in range(n):
    for j in range(i, n):
        ans = (ans + mat[i][j]) % MOD
ans = (ans * pow(2, q, MOD)) % MOD
print(ans)