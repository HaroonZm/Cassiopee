import sys

# Large enough height to accommodate all blocks (max 1000 blocks, each up to length 5)
# We choose 2000 to be safe.
HEIGHT = 2000
WIDTH = 5

def drop_block(board, d, p, q):
    """
    Simulate dropping a block on the board.
    d: direction (1=horizontal, 2=vertical)
    p: length (1 to 5)
    q: position (1 to 5) - left end for horizontal, column for vertical
    board: 2D list representing board state (HEIGHT rows x WIDTH columns)
    """

    q -= 1  # zero-based index

    # Find the landing height of the block
    # Landing height (row) is the lowest row where the block can be placed (bottom row is 0)
    # We start from the bottom and go upward

    if d == 1:
        # horizontal block p-length starting at column q
        # Ensure the block fits horizontally
        if q + p > WIDTH:
            # invalid input technically, but per problem constraints it should not happen
            return

        # For each column of the block, find height of the stacked blocks
        max_height = 0
        for col in range(q, q + p):
            # find topmost filled cell in this column
            col_height = 0
            for row in range(HEIGHT):
                if board[row][col]:
                    col_height = row + 1  # block occupies this or below, so candidate height is next row
            if col_height > max_height:
                max_height = col_height

        # max_height is where the bottom of the block will rest
        # Place the block at max_height row over columns q..q+p-1
        for col in range(q, q + p):
            board[max_height][col] = True

        # After placing, clear any complete lines and settle blocks downwards
        clear_lines(board)

    else:
        # vertical block length p at column q
        # Find the row where depositing vertical block with p height is possible:
        # we need a space of p cells vertically, finding the lowest row where block bottom cell can be placed
        # We drop the block down until any block is immediately below the bottom cell, or bottom row is reached.
        # Check for each possible position the landing row

        # Starting from 0 (ground), we try upward until existing block blocks it.
        landing_row = 0
        while True:
            # check if block fits if placed with bottom cell at landing_row
            # check from landing_row to landing_row + p -1 cells at column q, if any cell occupied
            can_place = True
            if landing_row + p > HEIGHT:
                # out of bounds, cannot place here (should not happen due to large HEIGHT)
                can_place = False
            else:
                for r in range(landing_row, landing_row + p):
                    if board[r][q]:
                        can_place = False
                        break
            if not can_place:
                # cannot place here, must place one row above
                landing_row -= 1
                break
            landing_row += 1

        if landing_row < 0:
            landing_row = 0

        # place block vertical at landing_row to landing_row + p -1
        for r in range(landing_row, landing_row + p):
            board[r][q] = True

        clear_lines(board)


def clear_lines(board):
    """
    Check for full rows and clear them.
    Rows above lines cleared will fall down accordingly.
    """

    # We traverse from bottom (row=0) upwards
    write_row = 0  # position to copy rows downward
    for read_row in range(HEIGHT):
        if all(board[read_row]):
            # Row fully occupied - clear by not copying it down
            continue
        if read_row != write_row:
            # copy row down
            board[write_row] = board[read_row][:]
        write_row += 1

    # Clear remaining rows above
    for r in range(write_row, HEIGHT):
        board[r] = [False] * WIDTH


def count_blocks(board):
    """
    Count how many cells are True (blocks present) on the board.
    """
    count = 0
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if board[r][c]:
                count += 1
    return count

def main():
    input = sys.stdin.readline

    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if line == '':
                return
        n = int(line.strip())
        if n == 0:
            break

        # Initialize empty board
        # bottom row = 0 index
        board = [[False] * WIDTH for _ in range(HEIGHT)]

        for _ in range(n):
            while True:
                line = input()
                if line.strip() != '':
                    break
            d,p,q = map(int,line.strip().split())
            drop_block(board, d, p, q)

        result = count_blocks(board)
        print(result)

if __name__ == "__main__":
    main()