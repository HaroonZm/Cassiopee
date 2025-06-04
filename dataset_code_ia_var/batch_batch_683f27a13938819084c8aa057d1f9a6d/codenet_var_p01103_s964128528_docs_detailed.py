from itertools import product

def read_dimensions():
    """
    Reads two integers from input representing the number of rows (d) and columns (w).
    
    Returns:
        tuple: A tuple (d, w) of integers.
    """
    d, w = map(int, input().split())
    return d, w

def read_grid(d):
    """
    Reads a d x w grid of integers from input.
    
    Args:
        d (int): Number of rows in the grid.
    
    Returns:
        list: A list of lists representing the grid.
    """
    grid = []
    for _ in range(d):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

def compute_max_fill(d, w, grid):
    """
    Computes the maximum possible sum by filling a rectangular region in the grid
    such that the fill value (minimum value on the border) is strictly greater 
    than the maximum inner value, and the total fill sum is maximized.
    
    Args:
        d (int): Number of rows.
        w (int): Number of columns.
        grid (list): 2D list representing the grid.
    
    Returns:
        int: The maximal possible fill sum.
    """
    max_fill = 0  # To store the maximal possible sum

    # Iterate over all possible starting cells of inner rectangle (strictly inside the grid)
    for si, sj in product(range(1, d - 1), range(1, w - 1)):
        # Iterate over all possible ending cells (exclusive, bottom right)
        for ti, tj in product(range(si + 1, d), range(sj + 1, w)):
            inner_max = 0  # Maximum value inside the rectangle

            # Calculate the maximum value inside the rectangle (excluding border)
            for i, j in product(range(si, ti), range(sj, tj)):
                inner_max = max(inner_max, grid[i][j])

            border_min = 100  # Minimum value on the border (initialized to a large value)

            # Check minimum on the top and bottom horizontal border
            for i, j in product([si - 1, ti], range(sj - 1, tj + 1)):
                border_min = min(border_min, grid[i][j])

            # Check minimum on the left and right vertical border
            for i, j in product(range(si - 1, ti + 1), [sj - 1, tj]):
                border_min = min(border_min, grid[i][j])

            # The border value should be greater than all inner values to be fillable
            if inner_max >= border_min:
                continue

            fill_sum = 0  # Sum that can be filled in this region

            # Compute the fill sum for all inner cells
            for i, j in product(range(si, ti), range(sj, tj)):
                fill_sum += border_min - grid[i][j]

            # Update the answer if this region yields a larger fill sum
            max_fill = max(max_fill, fill_sum)

    return max_fill

def main():
    """
    Main execution loop to repeatedly read input and compute the result.
    Continues until a case with d == 0 is encountered.
    """
    while True:
        # Read grid dimensions
        d, w = read_dimensions()
        # Terminate the loop if d == 0
        if d == 0:
            exit()

        # Read the d x w grid
        grid = read_grid(d)
        # Compute the maximum fill sum and print the result
        result = compute_max_fill(d, w, grid)
        print(result)

if __name__ == "__main__":
    main()