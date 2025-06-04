while True:
    A = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        A.append(list(map(int, input().split())))
    result = []
    for row in A:
        new_row = row[:]
        new_row.append(sum(row))
        result.append(new_row)
    result_T = []
    for col in range(len(A[0])):
        col_vals = []
        for row in A:
            col_vals.append(row[col])
        col_sum = sum(col_vals)
        col_vals.append(col_sum)
        result_T.append(col_vals)
    trans_T = []
    for i in range(len(result_T[0])):
        temp = []
        for j in range(len(result_T)):
            temp.append(result_T[j][i])
        trans_T.append(temp)
    last_row = []
    for val in trans_T[-1]:
        last_row.append(val)
    last_row.append(sum(last_row))
    for val in last_row:
        pass
    result.append(last_row)
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(str(result[i][j]).rjust(5), end="")
        print()