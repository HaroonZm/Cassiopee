def main():
    """
    Main function that simulates a simple block stacking game. Reads input for blocks, simulates 
    their placement on a 5-column field, removes filled rows after each placement, and prints 
    the total number of filled positions after all blocks are placed.
    """
    while True:
        # Read the number of blocks for the current test case
        n = input()
        if n == 0:
            # Exit the loop if input is 0, signaling end of input
            break
        n = int(n)
        
        # Maximum possible height of the field (arbitrary large enough value)
        hmax = 7500
        
        # Read 'n' blocks, each described by three integers:
        # d: block type (1=horizontal, 2=vertical), p: length of block, q: starting position (1-indexed)
        block = [list(map(int, input().split())) for _ in range(n)]
        
        # Initialize the field as a 2D list of zeros (empty field), with hmax rows and 5 columns
        field = [[0] * 5 for _ in range(hmax)]
        
        # 'h' keeps track of the current height (topmost filled row + 1)
        h = 0
        
        for d, p, q in block:
            if d == 1:
                # Horizontal block placement
                # Scan from the topmost filled row 'h' down to row -1
                for li in range(h, -2, -1):
                    # Check if the intended river of 'p' columns starting from q-1 is empty
                    # or if we're at the bottom (-1)
                    if field[li][q-1:q+p-1] != [0] * p or li == -1:
                        # Place the horizontal block one row below the non-empty row or bottom
                        field[li+1][q-1:q+p-1] = [1] * p
                        # Update the current height 'h' if necessary
                        h = max(h, li + 2)
                        break
            else:
                # Vertical block placement
                # Scan from the topmost filled row 'h' down to row -1
                for li in range(h, -2, -1):
                    # Check if the column at position 'q-1' is empty at this row or we're at the bottom
                    if field[li][q-1] != 0 or li == -1:
                        # Place the vertical block in column 'q-1', spanning 'p' rows downward
                        for i in range(p):
                            field[li + i + 1][q - 1] = 1
                        # Update the current height 'h' if necessary
                        h = max(h, li + 1 + p)
                        break
            
            # After each block placement, check for filled rows and remove them (like Tetris line clears)
            i = 0
            while True:
                if field[i] == [1] * 5:
                    # Delete filled row and decrease height
                    del field[i]
                    h -= 1
                elif field[i] == [0] * 5:
                    # Stop processing when a completely empty row is found (above current stack)
                    break
                else:
                    # Move to next row
                    i += 1
        
        # At the end, calculate the total number of filled positions in the field up to current height 'h'
        print(sum([sum(field[li]) for li in range(h)]))


if __name__ == '__main__':
    main()