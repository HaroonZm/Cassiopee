from sys import stdin
from itertools import accumulate

file_input = stdin

N = int(file_input.readline())
G = []
for _ in range(N):
    G.append(tuple(map(int, file_input.readline().split())))

ar = []
for line in G:
    a = [0]
    a.extend(accumulate(line))
    ar.append(tuple(a))

ac_cols = []
for line in zip(*G):
    a = [0]
    a.extend(accumulate(line))
    ac_cols.append(tuple(a))
ac_1 = ac_cols[0]
ac = []
for j in range(N):
    temp = []
    for i in range(N+1):
        temp.append(ac_cols[j][i])
    ac.append(tuple(temp))
ac = tuple(zip(*ac))

ans = 0
for i in range(N):
    G_i = G[i]
    ar_i = ar[i]
    ac_i = ac[i]
    ac_1i = ac_1[i]
    ar_ii = ar_i[i]
    j = i
    while j < N:
        G_j = G[j]
        ar_ij = ar_i[j+1]
        ac_j = ac[j+1]
        ac_1j = ac_1[j+1]
        if ar_ij - ar_ii > ans:
            ans = ar_ij - ar_ii
        if i == j:
            j += 1
            continue
        col_max = ac_1j - ac_1i
        k = 1
        while k < N+1:
            ac_jk = ac_j[k]
            ac_ik = ac_i[k]
            G_ik = G_i[k-1]
            G_jk = G_j[k-1]
            col = ac_jk - ac_ik
            if col_max > 0:
                c_ans = col_max + col
                if c_ans > ans:
                    ans = c_ans
            else:
                if col > ans:
                    ans = col
            t_col_max = col_max + G_ik + G_jk
            if t_col_max > col:
                col_max = t_col_max
            else:
                col_max = col
            k += 1
        j += 1
print(ans)