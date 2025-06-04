def get_input():
    """
    Generator function that reads input from standard input line by line.
    Continues reading until EOF (End Of File) is encountered, at which point the loop breaks.
    Yields each line as a string.
    """
    while True:
        try:
            # Read one line from input and yield it
            yield ''.join(input())
        except EOFError:
            # Stop iteration when EOF is encountered
            break

def nuri(table, m, x, y):
    """
    Recursively labels all connected 'True' cells in 'table' starting from position (x, y).
    Uses depth-first search to traverse in 4 directions.
    
    Args:
        table (list of list of bool): 2D grid indicating available positions to fill.
        m (list of list of int): 2D grid with region markings (0 if unmarked, region number otherwise).
        x (int): Row index of the current position.
        y (int): Column index of the current position.
    """
    # Check upward neighbor
    if table[x-1][y] and m[x-1][y] == 0:
        m[x-1][y] = m[x][y]
        nuri(table, m, x-1, y)
    # Check downward neighbor
    if table[x+1][y] and m[x+1][y] == 0:
        m[x+1][y] = m[x][y]
        nuri(table, m, x+1, y)
    # Check left neighbor
    if table[x][y-1] and m[x][y-1] == 0:
        m[x][y-1] = m[x][y]
        nuri(table, m, x, y-1)
    # Check right neighbor
    if table[x][y+1] and m[x][y+1] == 0:
        m[x][y+1] = m[x][y]
        nuri(table, m, x, y+1)
    return

# Read all input lines into a list; 
# each element in N is a line (row) of the input grid as a string
N = list(get_input())

# Process the input in blocks of 13 lines,
# as each block seems to represent a single test case
for l in range(0, len(N), 13):
    # Initialize a 14x14 grid (with 1-cell border) filled with False
    table = [[False for i in range(14)] for j in range(14)]
    # Fill the core 12x12 table with True for positions with '1' in the input
    for i in range(12):
        for j in range(12):
            if int(N[l + i][j]) == 1:
                # Shift indices by 1 to leave a border around the table
                table[i + 1][j + 1] = True

    # Create a marking grid of the same size, initialized to 0
    m = [[0 for i in range(14)] for j in range(14)]
    cnt = 0  # Counter for number of distinct regions

    # Traverse the core grid positions 
    for i in range(1, 13):
        for j in range(1, 13):
            # If cell (i, j) is unmarked and set as True, start a DFS to label the region
            if table[i][j] and m[i][j] == 0:
                cnt += 1
                m[i][j] = cnt
                nuri(table, m, i, j)

    # Print the number of connected components in current grid
    print(cnt)