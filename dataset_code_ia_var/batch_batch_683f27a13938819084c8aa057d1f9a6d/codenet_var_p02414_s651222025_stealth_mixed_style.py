A, B = list(), []
n, m, l = [int(x) for x in input().split()]
for _ in range(n):
    y = input().split()
    row = []
    for v in y:
        row.append(int(v))
    A += [row]
for _ in range(m):
    B.append([*map(int, input().split())])
def mul(a, b, rows, cols, width):
    res = []
    for i in range(rows):
        c = []
        j = 0
        while j < cols:
            s = 0
            for k in range(width):
                s = s + a[i][k] * b[k][j]
            c.append(s)
            j += 1
        res.append(c)
    return res
result = mul(A, B, n, l, m)
for line in result:
    print(*map(str, line))