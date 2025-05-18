from collections import defaultdict

H, W = map(int, input().split())
mass = list()
for i in range(H):
    mass.append(input())

values_col = defaultdict(int)
values_row = defaultdict(int)

ind_row = [[0 for i in range(W)] for j in range(H)]
ind_col = [[0 for i in range(W)] for j in range(H)]

ind = 0
for i, m_row in enumerate(mass):
    ind += 1
    for j, chr in enumerate(mass[i]):
        if chr == '#':
            ind += 1
        else:
            values_row[ind] += 1
            ind_row[i][j] = ind

# print('ROW')
# for i in range(H):
#     for j in range(W):
#         print(values_row[ind_row[i][j]], end=' ')
#     print()

ind = 0
for j in range(W):
    ind += 1
    for i in range(H):
        chr = mass[i][j]
        if chr == '#':
            ind += 1
        else:
            values_col[ind] += 1
            ind_col[i][j] = ind

# print('COL')
# for i in range(H):
#     for j in range(W):
#         print(values_col[ind_col[i][j]], end=' ')
#     print()

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, values_row[ind_row[i][j]] + values_col[ind_col[i][j]] - 1)
print(ans)