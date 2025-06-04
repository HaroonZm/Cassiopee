import sys
import math
import os
import bisect

# If the environment variable PYDEV is "True", redirect stdin to "sample-input.txt" for local testing
PYDEV = os.environ.get('PYDEV')
if PYDEV == "True":
    sys.stdin = open("sample-input.txt", "rt")

def grid_length(n, grid):
    """
    Calculate the length of the longest consecutive sequence of '1's in the given n x n grid.
    The search is performed in all rows, columns, and both main diagonals.

    Parameters
    ----------
    n : int
        The size of the grid (number of rows and columns).
    grid : List[str]
        A list of n strings, each representing a row of the grid. Each character is either '1' or '0'.

    Returns
    -------
    int
        The length of the longest consecutive sequence of '1's found in any row, column, or diagonal.
    """
    L = 0  # Keeps track of the longest sequence found

    # Check all rows for consecutive '1's
    for row in grid:
        # Split the row by '0's, so each substring contains only consecutive '1's
        # Take the length of the largest such substring
        L = max(L, max([len(segment) for segment in row.split('0')]))

    # Check all columns for consecutive '1's
    for c in range(n):
        # Construct the column as a string by concatenating the character at position c in each row
        col = ''.join([grid[r][c] for r in range(n)])
        # Split the column by '0's and find the maximum consecutive '1's
        L = max(L, max([len(segment) for segment in col.split('0')]))

    # Check all diagonals (both directions) for consecutive '1's
    # Diagonals with positive slope (\): iterate over all possible starting points
    for offset in range(-n, 2 * n):
        # For each diagonal, build the string from top-left to bottom-right
        diag1 = ''.join([grid[offset + c][c] for c in range(n) if 0 <= offset + c < n])
        if diag1:
            L = max(L, max([len(segment) for segment in diag1.split('0')]))

        # For each anti-diagonal, build the string from bottom-left to top-right
        diag2 = ''.join([grid[offset - c][c] for c in range(n) if 0 <= offset - c < n])
        if diag2:
            L = max(L, max([len(segment) for segment in diag2.split('0')]))

    return L

def main():
    """
    Main function to repeatedly read the problem input, process it, and output the results.
    Continues until an input line with a single '0' is encountered.
    """
    while True:
        n_line = input()
        n = int(n_line)
        if n == 0:
            break
        # Read n lines to build the grid
        grid = [input().strip() for _ in range(n)]
        # Print the maximum length of consecutive '1's in the grid
        print(grid_length(n, grid))

if __name__ == "__main__":
    main()