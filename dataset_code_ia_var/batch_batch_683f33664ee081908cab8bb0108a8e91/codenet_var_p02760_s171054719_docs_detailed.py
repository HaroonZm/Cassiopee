def read_row():
    """
    Reads a line of input, splits it by whitespace, and converts the values to integers to form a list.
    
    Returns:
        list: A list of three integers representing one row of a 3x3 grid.
    """
    return list(map(int, input().split()))

def mark_number_on_grid(number, grid, mark_value):
    """
    Replaces occurrences of a given number with the specified mark_value in the provided grid rows.
    
    Args:
        number (int): The number to search for and mark in the grid.
        grid (list of lists): The game grid (3 rows, each is a list).
        mark_value (int): The value to replace matched numbers with (indicating a mark).
    """
    for row in grid:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = mark_value

def is_bingo(grid, mark_value):
    """
    Checks the grid for a bingo (i.e., a full row, column, or diagonal matches mark_value).

    Args:
        grid (list of lists): The game grid, 3x3 (three lists of three integers).
        mark_value (int): The special value representing a marked cell.

    Returns:
        bool: True if any row, column, or diagonal is fully marked, False otherwise.
    """
    # Check rows
    for i in range(3):
        if all(cell == mark_value for cell in grid[i]):
            return True

    # Check columns
    for j in range(3):
        if all(grid[i][j] == mark_value for i in range(3)):
            return True

    # Check diagonals
    if all(grid[i][i] == mark_value for i in range(3)):
        return True
    if all(grid[i][2 - i] == mark_value for i in range(3)):
        return True

    return False

def main():
    """
    Main function to run the bingo check.
    Reads three rows of grid numbers and a list of called numbers. Marks the grid as numbers are called,
    and then determines if a bingo (row, column, or diagonal filled) has occurred.
    Prints "Yes" if bingo, otherwise "No".
    """
    # Read the three rows of the 3x3 bingo grid from the user
    a = read_row()
    b = read_row()
    c = read_row()

    # Store the grid as a list of rows for easier processing
    grid = [a, b, c]

    # Define the special value to represent a marked cell
    maru = 111

    # Read the number of called numbers
    n = int(input())

    # For each called number, mark them in the grid if present
    for _ in range(n):
        e = int(input())
        mark_number_on_grid(e, grid, maru)

    # Check if the grid has a bingo (row, column, diagonal fully marked)
    if is_bingo(grid, maru):
        print("Yes")
    else:
        print("No")

# Run the main function
if __name__ == "__main__":
    main()