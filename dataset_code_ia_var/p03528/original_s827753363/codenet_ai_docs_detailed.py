import sys

def input():
    """
    Reads a line from standard input, strips the trailing newline, 
    and returns the string.
    """
    return sys.stdin.readline().strip()

# Total number of rows required in the matrix (N) and parameter K.
N = 1407  # Number of rows in the matrix. Calculated as K + K*(K-1)
K = 38    # The main parameter (also acts as the number of columns).

# Initialize a 2D list (matrix) of size N x K with zeros.
num_all = [[0] * K for _ in range(N)]

# Fill the first row with numbers 1 to K.
for i in range(K):
    num_all[0][i] = i + 1  # 1-based indexing, so add 1

# Fill the first column for the next K*(K-1) rows.
num = 1  # Row index tracker; will go from 1 upwards
for i in range(K):
    for j in range(K - 1):
        num_all[num][0] = i + 1  # Every block of (K - 1) rows gets first column value (i+1)
        num += 1  # Move to next row

# Fill the submatrix (excluding the first row and first column) with incrementing numbers.
num = K + 1  # Numbering for the cells starts after K (from the filled rows and columns)
for i in range(1, K):
    for j in range(1, K):
        num_all[i][j] = num
        num += 1

# Fill the remaining entries in the matrix following a combinatorial construction:
for n in range(2, K + 1):  # For construction steps from 2 to K inclusive
    for j in range(K - 1):  # For each block within the step
        for i in range(K - 1):  # For each entry in the block
            # Calculate the number to be inserted
            num = K + 1 + j * (K - 1) + i
            # Calculate the correct row to insert into
            loc = K + (n - 2) * (K - 1) + ((i + j * (n - 2)) % (K - 1))
            # Insert into the correct position (row 'loc', column 'j+1')
            num_all[loc][j + 1] = num

def list_print(A):
    """
    Prints the elements of list A in a single line, separated by spaces.
    
    Args:
        A (list): The list of elements to be printed.
    """
    length = len(A)
    for i in range(length - 1):
        print(A[i], end="")
        print(" ", end="")
    print(A[-1])

# Output the dimensions first: N and K
list_print([N, K])

# Output each row of the constructed matrix
for i in range(N):
    list_print(num_all[i])