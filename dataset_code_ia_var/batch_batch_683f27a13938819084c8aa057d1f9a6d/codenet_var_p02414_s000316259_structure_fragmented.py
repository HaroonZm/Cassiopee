def read_ints():
    return list(map(int, input().split()))

def get_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(read_ints())
    return matrix

def transpose(matrix):
    return list(zip(*matrix))

def mult_row_col(row, col):
    return sum(a * b for a, b in zip(row, col))

def multiply_row_by_matrix(row, matrix_T):
    return [mult_row_col(row, col) for col in matrix_T]

def multiply_matrices(matA, matB_T):
    result = []
    for row in matA:
        result.append(multiply_row_by_matrix(row, matB_T))
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    nml = read_ints()
    n, m, l = nml[0], nml[1], nml[2]
    matA = get_matrix(n)
    matB = get_matrix(m)
    matB_T = transpose(matB)
    res = multiply_matrices(matA, matB_T)
    print_matrix(res)

main()