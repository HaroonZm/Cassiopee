while True:
    n = int(input())
    if n == 0:
        # End of input
        break
    matrix = []
    for _ in range(n):
        # Read each row of the matrix as a list of integers
        row = list(map(int, input().split()))
        matrix.append(row)

    # Initialize a list to store the sum of each column
    col_sums = [0] * n
    # Initialize a list to store the sum of each row
    row_sums = [0] * n

    # Calculate the sums
    for i in range(n):
        row_sum = sum(matrix[i])
        row_sums[i] = row_sum
        for j in range(n):
            col_sums[j] += matrix[i][j]

    # Calculate the total sum of all elements
    total_sum = sum(row_sums)

    # Print the matrix with row sums
    for i in range(n):
        # For each element in the row, print right aligned with width 5
        for j in range(n):
            print(f"{matrix[i][j]:5d}", end='')
        # Print the sum of the current row at the end, also right aligned with width 5
        print(f"{row_sums[i]:5d}")

    # Print the sums of each column at the bottom, right aligned with width 5
    for j in range(n):
        print(f"{col_sums[j]:5d}", end='')
    # Print the total sum at the bottom right corner, right aligned with width 5
    print(f"{total_sum:5d}")