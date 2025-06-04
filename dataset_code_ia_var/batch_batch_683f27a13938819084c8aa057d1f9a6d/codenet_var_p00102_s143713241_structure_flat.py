while True:
    n = int(raw_input())
    if n == 0:
        break
    a = []
    for i in range(n):
        row = map(int, raw_input().split())
        row_sum = sum(row)
        row.append(row_sum)
        a.append(row)
    last_row = []
    for k in range(n + 1):
        col_sum = 0
        for j in range(n):
            col_sum += a[j][k]
        last_row.append(col_sum)
    a.append(last_row)
    s = ""
    for i in range(n + 1):
        for j in range(n + 1):
            s += "{0:5d}".format(a[i][j])
        s += "\n"
    print s,