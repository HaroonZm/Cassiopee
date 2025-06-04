while True:
    n = int(input())
    if n == 0:
        break
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # find the shortest in each row
    shortest_in_row = []
    for i in range(n):
        shortest = min(matrix[i])
        shortest_in_row.append(shortest)

    # find the tallest in each column
    tallest_in_col = []
    for j in range(n):
        tallest = matrix[0][j]
        for i in range(1, n):
            if matrix[i][j] > tallest:
                tallest = matrix[i][j]
        tallest_in_col.append(tallest)

    result = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == shortest_in_row[i] and matrix[i][j] == tallest_in_col[j]:
                result = matrix[i][j]

    print(result)