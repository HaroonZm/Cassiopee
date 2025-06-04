K = 38
#K = int(input())
N = K ** 2 - K + 1

print(N, K)

_res = []
for i in range((K - 1) ** 2):
    row = []
    for j in range(K - 1):
        row.append(-1)
    _res.append(row)

rest = []
for i in range(K - 1):
    row = []
    for j in range(K - 1):
        row.append(-1)
    rest.append(row)

id = K
start = 0
while N > id:
    j = 0
    while j < K - 1:
        x = (K - 1) * j + (start + j * ((id - 1) // (K - 1))) % (K - 1)
        y = (id - 1) // (K - 1) - 1
        _res[x][y] = id
        j += 1
    id += 1
    start = (start + 1) % (K - 1)

rest = []
i = 0
while i < K - 1:
    row = []
    j = 0
    while j < K - 1:
        row.append(_res[j][i])
        j += 1
    rest.append(row)
    i += 1

ans = []
row = []
j = 0
while j < K:
    row.append(j)
    j += 1
ans.append(row)

i = 0
while i < K - 1:
    j = 0
    while j < K - 1:
        tmp = []
        tmp.append(i)
        k = 0
        while k < K - 1:
            tmp.append(_res[(K - 1) * i + j][k])
            k += 1
        ans.append(tmp)
        j += 1
    i += 1

i = 0
while i < K - 1:
    tmp = []
    tmp.append(K - 1)
    j = 0
    while j < K - 1:
        tmp.append(rest[i][j])
        j += 1
    ans.append(tmp)
    i += 1

i = 0
while i < N:
    row = []
    j = 0
    while j < K:
        row.append(ans[i][j] + 1)
        j += 1
    ans[i] = row
    i += 1

i = 0
while i < N:
    j = 0
    while j < K:
        print(ans[i][j], end=' ' if j < K - 1 else '\n')
        j += 1
    i += 1

# ---- Optionnel, désactivé par défaut ----
# ids = []
# i = 0
# while i < N:
#     ids.append([])
#     i += 1
#
# i = 0
# while i < N:
#     ans[i].sort()
#     if ans[i][0] < 0 or ans[i][-1] > N - 1:
#         print("WA1")
#         exit()
#     j = 1
#     while j < K:
#         if ans[i][j] == ans[i][j-1]:
#             print("WA2")
#             exit()
#         j += 1
#     j = 0
#     while j < K:
#         ids[ans[i][j]].append(i)
#         j += 1
#     i += 1
#
# i = 0
# while i < N:
#     if len(ids[i]) != K:
#         print("WA3")
#         exit()
#     i += 1
#
# p = set()
# i = 0
# while i < N:
#     j = 0
#     while j < len(ids[i]):
#         k = 0
#         while k < j:
#             a = ids[i][j]
#             b = ids[i][k]
#             if (a, b) in p:
#                 print("WA4")
#                 print(ans[a])
#                 print(ans[b])
#                 exit()
#             p.add((a, b))
#             k += 1
#         j += 1
#     i += 1