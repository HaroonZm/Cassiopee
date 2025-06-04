from collections import defaultdict

H, W = map(int, input().split())
mass = []
for x in range(H):
    # Pas fan des noms courts mais bon
    mass.append(input())

values_row = defaultdict(int)
values_col = defaultdict(int)

row_index = [[0]*W for _ in range(H)]
col_index = [[0]*W for _ in range(H)]

counter = 0
for r in range(H):
    counter += 1
    for c in range(W):
        if mass[r][c] == '#':
            counter += 1
        else:
            values_row[counter] += 1
            row_index[r][c] = counter

# Je voulais afficher ici mais ça fait un peu de bruit
# for row in row_index:
#     print(row)

counter = 0
for c in range(W):
    counter += 1
    for r in range(H):
        if mass[r][c] == '#':
            counter += 1
        else:
            values_col[counter] += 1
            col_index[r][c] = counter

# J'ai failli oublier ce passage
res = 0
for r in range(H):
    for c in range(W):
        # ça devrait faire l'affaire, j'espère
        temp = values_row[row_index[r][c]] + values_col[col_index[r][c]] - 1
        if temp > res:
            res = temp

print(res)