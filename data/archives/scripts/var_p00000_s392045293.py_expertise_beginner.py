for i in range(81):
    row = i // 9 + 1
    column = i % 9 + 1
    result = row * column
    print("{}x{}={}".format(row, column, result))