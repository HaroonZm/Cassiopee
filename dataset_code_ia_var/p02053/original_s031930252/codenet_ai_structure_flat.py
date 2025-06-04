INF = 10e10
H_W = input().split()
H = int(H_W[0])
W = int(H_W[1])
c_grid = []
B = set()
i = 0
while i < H:
    line = input()
    row = list(line)
    c_grid.append(row)
    j = 0
    while j < W:
        if row[j] == "B":
            B.add((i, j))
        j += 1
    i += 1

a = 0
b = INF
c_val = 0
d = INF
B_list = list(B)
idx = 0
while idx < len(B_list):
    e = B_list[idx]
    sum_e = e[0] + e[1]
    diff_e = e[0] - e[1]
    if sum_e > a:
        a = sum_e
    if sum_e < b:
        b = sum_e
    if diff_e > c_val:
        c_val = diff_e
    if diff_e < d:
        d = diff_e
    idx += 1

result1 = a - b
result2 = c_val - d
if result1 > result2:
    print(result1)
else:
    print(result2)