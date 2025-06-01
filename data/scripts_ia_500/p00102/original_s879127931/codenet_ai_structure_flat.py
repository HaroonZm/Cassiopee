while True:
    n = int(input())
    if n == 0:
        break
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    result = []
    for row in A:
        s = sum(row)
        row2 = row + [s]
        result.append(row2)
    cols = []
    for j in range(len(A[0])):
        col = []
        for i in range(n):
            col.append(A[i][j])
        cols.append(col)
    col_sums = [sum(col) for col in cols]
    last_row = col_sums + [sum(col_sums)]
    result.append(last_row)
    for row in result:
        for val in row:
            print(str(val).rjust(5), end='')
        print()