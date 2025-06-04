n, m, d = map(int, input().split())
field = []
for i in range(n):
    line = input()
    field.append(line)

ans = 0

# Vérifier les lignes
for row in field:
    parts = row.split("#")
    for part in parts:
        if len(part) >= d:
            ans += len(part) - d + 1

# Vérifier les colonnes
columns = []
for col in range(m):
    col_str = ""
    for row in range(n):
        col_str += field[row][col]
    columns.append(col_str)

for col in columns:
    parts = col.split("#")
    for part in parts:
        if len(part) >= d:
            ans += len(part) - d + 1

print(ans)