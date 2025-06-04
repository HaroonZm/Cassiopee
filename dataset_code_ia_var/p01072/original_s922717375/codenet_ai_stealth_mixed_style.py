w, h, t = [int(x) for x in input().split()]
num = int(input())
H = []
for _ in range(num):
    d = input().split()
    H += [[int(d[0]),int(d[1]),int(d[2])]]
field = []
for _ in range(h):
    r = input().split()
    row = []
    for c in r:
        if int(c) == 1:
            row.append(True)
        else:
            row.append(False)
    field.append(row)

result = [[0]*w for _ in range(h)]
def update_field(h_data, fld, res):
    for k in range(len(h_data)):
        x, y, t = h_data[k]
        if fld[y][x]:
            res[y][x] += 1
update_field(H, field, result)

S = 0
i = 0
while i < len(result):
    S = S + sum(result[i])
    i += 1
print(S)