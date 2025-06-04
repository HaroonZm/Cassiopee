import queue as Q

def read_input():
    """
    Reads the input for the problem. 
    The first line should contain two integers representing the number of rows and columns.
    The next lines contain the grid information, where each cell is either '.' or a digit.
    Returns:
        tuple: (a - list of two integers, b - grid of strings)
    """
    a = list(map(int, input().split()))  # Read dimensions of the grid [rows, columns]
    b = []  # Initialize grid
    for _ in range(a[0]):  # Read each row of the grid
        b.append(list(input()))  # Store each character in a separate cell
    return a, b

def initialize_grids(a, b):
    """
    Initializes the auxiliary grids and markers required for processing.
    Args:
        a (list): List containing the number of rows and columns.
        b (list): Initial grid of strings.
    Returns:
        tuple: (b - converted to integer grid with dots, c - integer grid for counts)
    """
    c = [[] for _ in range(a[0])]  # Initialize the count grid
    for i in range(a[0]):  # Iterate through each cell
        row_c = []
        for j in range(a[1]):
            if b[i][j] != '.':  # If cell is not a dot, convert to integer
                b[i][j] = int(b[i][j])
            row_c.append(0)  # Initialize count to 0
        c[i] = row_c
    return b, c

def count_dot_neighbors(a, b, c, arounds):
    """
    Fills the 'c' grid with the count of neighboring '.' cells for each cell (excluding the edge cells).
    Args:
        a (list): [number of rows, number of columns]
        b (list): Current grid with integers and '.'
        c (list): Grid to fill with the counts
        arounds (list): List of (dx, dy) pairs for 8 neighboring cells
    """
    for i in range(1, a[0]-1):  # Avoid the first and last row
        for j in range(1, a[1]-1):  # Avoid the first and last column
            for dx, dy in arounds:  # Check each neighbor
                ni, nj = i + dx, j + dy
                if b[ni][nj] == '.':  # If neighbor is a dot
                    c[i][j] += 1  # Increment the count in c[i][j]

def mark_initial_dots(a, b, c, qs):
    """
    Marks the initial cells that will turn into '.' because their hint value is less than or equal to the dot neighbor count.
    Args:
        a (list): [number of rows, number of columns]
        b (list): Grid with integer values and '.'
        c (list): Grid with counts of dot-neighbors for each cell
        qs (list): List of two Queue objects for double buffering
    Returns:
        int: 1 if any cells are marked, 0 otherwise
    """
    has_change = 0
    for i in range(a[0]):
        for j in range(a[1]):
            if b[i][j] != '.' and b[i][j] <= c[i][j]:
                b[i][j] = '.'
                qs[0].put((i,j))  # Enqueue position
                has_change = 1
    return has_change

def process_waves(a, b, c, qs, arounds):
    """
    Simulates the wave propagation of revealing cells based on the mine counts, incrementing the step counter each wave.
    Args:
        a (list): [number of rows, number of columns]
        b (list): Grid of current cell states
        c (list): Count grid of neighboring dots
        qs (list): List of two Queues for processing
        arounds (list): List of (dx,dy) neighbor offsets
    Returns:
        int: The total number of waves required to finish the process
    """
    wave_count = 0  # Initialize number of wave steps taken
    q = 0  # Index of the current queue being processed (double buffer)
    while not qs[q].empty():  # While there are more cells to process
        while not qs[q].empty():
            p = qs[q].get()  # Get the cell position (i, j)
            i, j = p
            for dx, dy in arounds:  # For each neighbor
                ni, nj = i + dx, j + dy
                # Update count of dot-neighbors for the neighbor cell
                c[ni][nj] += 1
                # If neighbor is a number and has exactly enough dots around it to be revealed
                if b[ni][nj] != '.' and b[ni][nj] == c[ni][nj]:
                    b[ni][nj] = '.'  # Reveal the cell (turn into '.')
                    qs[q^1].put((ni,nj))  # Prepare for the next wave
        q ^= 1  # Switch to the other queue for the next wave of processing
        wave_count += 1  # Increment number of wave operations
    return wave_count

def main():
    """
    Main routine to execute the Minesweeper cell reveal simulation.
    Reads the input, initializes grids, performs the cell revelation process,
    and prints the number of wave steps required.
    """
    # Step 1: Read input and create the initial grid
    a, b = read_input()

    # Step 2: Prepare double-buffered queues for propagation
    qs = [Q.Queue(), Q.Queue()]  # Two queues for BFS-like layer by layer

    # Step 3: Directions to the 8 adjacent neighbors (including diagonals)
    arounds = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # Step 4: Initialize the count grid and convert b's values to int where appropriate
    b, c = initialize_grids(a, b)

    # Step 5: Count the number of neighboring '.' for each cell (excluding the border)
    count_dot_neighbors(a, b, c, arounds)

    # Step 6: Enqueue initial cells that can be revealed
    init_change = mark_initial_dots(a, b, c, qs)
    if not init_change:
        # If nothing to process, print 0 and exit
        return

    # Step 7: Process waves; each iteration is a step in propagation
    ans = process_waves(a, b, c, qs, arounds)

    # Step 8: Output the number of wave steps required
    print(ans)

if __name__ == "__main__":
    main()