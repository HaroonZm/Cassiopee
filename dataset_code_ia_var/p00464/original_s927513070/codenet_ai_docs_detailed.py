#!/usr/bin/env python
import string
import sys
from itertools import chain, takewhile

def read(
    f, *shape, it=chain.from_iterable(sys.stdin), whitespaces=set(string.whitespace)
):
    """
    Read values from an iterable, typically sys.stdin, according to a shape specification.

    Parameters:
        f (callable): Function to process each individual element (e.g., int, str).
        *shape (int): Dimensions to read. 
            - If no shape, reads a single value.
            - If 1D, reads shape[0] values.
            - If 2D, reads shape[0] rows of shape[1] elements each.
        it (iterator, optional): Iterable of characters to read from. Defaults to sys.stdin flattened.
        whitespaces (set of str, optional): Set of characters considered to be whitespace.

    Returns:
        The data read, processed by `f`, shaped per `shape`.
    """
    def read_word():
        # Read a word by consuming characters up to the next whitespace,
        # then apply the function f.
        return f("".join(takewhile(lambda c: c not in whitespaces, it)).strip())

    if not shape:
        # No shape: read and return a single word.
        return read_word()
    elif len(shape) == 1:
        # 1D shape: return a list of words.
        return [read_word() for _ in range(shape[0])]
    elif len(shape) == 2:
        # 2D shape: return a list of lists (matrix) of words.
        return [[read_word() for _ in range(shape[1])] for _ in range(shape[0])]

def arr(*shape, fill_value=0):
    """
    Create a 1D or 2D array (list of lists) filled with a specified value.

    Parameters:
        *shape (int): Dimensions of the array.
            - 1D: arr(size) returns [fill_value] * size
            - 2D: arr(rows, cols) returns [[fill_value] * cols for _ in range(rows)]
        fill_value (any, optional): Value used to fill the array. Defaults to 0.

    Returns:
        list: The filled array.
    """
    if len(shape) == 1:
        # 1D array
        return [fill_value] * shape[0]
    elif len(shape) == 2:
        # 2D array
        return [[fill_value] * shape[1] for _ in range(shape[0])]

def debug(**kwargs):
    """
    Print variable names and values for debugging to standard error.

    Parameters:
        **kwargs: Named variables to display.
    """
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )

def main():
    """
    Main execution function.
    
    Reads multiple test cases from stdin. Each test case begins with three integers:
    - h: number of rows in the grid
    - w: number of columns in the grid
    - n: number of tokens

    Then reads a h x w grid of integers. Simulates the path of n tokens in the grid
    with specified rules and determines the destination cell where the final token ends up.

    Repeats until a (0, 0, 0) triple is found.
    Prints the (1-based) coordinates of the final cell.
    """
    while True:
        # Read grid dimensions and number of tokens
        h, w, n = map(int, sys.stdin.readline().split())
        # Terminate on special input
        if (h, w, n) == (0, 0, 0):
            return

        # Read the h x w grid
        grid = []
        for _ in range(h):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)

        # Initialize DP table for counting tokens at each cell
        dp = arr(h, w)
        dp[0][0] = n - 1  # All but the last token remain to distribute

        # Simulate the distribution of tokens through the grid
        for i in range(h):
            for j in range(w):
                # If not on last row, move tokens down based on grid state
                if i < h - 1 and grid[i][j] == 0:
                    dp[i + 1][j] += (dp[i][j] + 1) // 2  # Half (round up) go down if cell=0
                if i < h - 1 and grid[i][j] == 1:
                    dp[i + 1][j] += dp[i][j] // 2  # Half (round down) go down if cell=1
                # If not on last col, move tokens right based on grid state
                if j < w - 1 and grid[i][j] == 0:
                    dp[i][j + 1] += dp[i][j] // 2  # Half (round down) go right if cell=0
                if j < w - 1 and grid[i][j] == 1:
                    dp[i][j + 1] += (dp[i][j] + 1) // 2  # Half (round up) go right if cell=1

        # Update the grid values to account for the parity flips caused by the tokens
        for i in range(h):
            for j in range(w):
                grid[i][j] = (grid[i][j] + dp[i][j]) % 2

        # Track the path of the last token
        i = 0
        j = 0
        while i < h and j < w:
            # Token moves down if cell==0, right if cell==1
            if grid[i][j] == 0:
                i += 1
            else:
                j += 1

        # Output final position in 1-based indexing
        print(i + 1, j + 1)

if __name__ == "__main__":
    main()