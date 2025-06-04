def main():
    """
    Main function to process a grid, count specific patterns, and output the result.

    The grid consists of 'I', 'O', and other characters.
    For each cell that is neither 'I' nor 'O', the code computes the product of:
        - The number of consecutive 'I's downward from this cell
        - The number of consecutive 'O's rightward from this cell
    The sum of these products for all such cells is computed and printed.
    """
    # Read grid dimensions h (number of rows) and w (number of columns)
    h, w = map(int, input().split())

    # Read the grid (each string of length w)
    mp = [input() for _ in range(h)]

    # Initialize 2D lists to store counts of consecutive 'I's and 'O's in required directions
    # i_cnt[y][x]: Number of consecutive 'I' characters downwards from cell (y, x) including itself if 'I'
    # o_cnt[y][x]: Number of consecutive 'O' characters rightwards from cell (y, x) including itself if 'O'
    i_cnt = [[0] * w for _ in range(h)]
    o_cnt = [[0] * w for _ in range(h)]

    # Populate last row 'I's: if the cell in the last row is 'I', set count to 1
    for x in range(w):
        if mp[h - 1][x] == "I":
            i_cnt[h - 1][x] = 1

    # Populate last column 'O's: if the cell in the last column is 'O', set count to 1
    for y in range(h):
        if mp[y][w - 1] == "O":
            o_cnt[y][w - 1] = 1

    # Initialize the answer (sum of products for all valid cells)
    ans = 0

    # Fill the i_cnt and o_cnt matrices from bottom right towards top left
    # Start from second-last row and column, iterate upwards and leftwards
    for y in range(h - 2, -1, -1):       # From h-2 downto 0 (rows)
        for x in range(w - 2, -1, -1):   # From w-2 downto 0 (columns)
            if mp[y][x] == "I":
                # For cell 'I', the number of 'I's downward is one more than below,
                # 'O' count right is the same as that in the right cell
                i_cnt[y][x] = i_cnt[y + 1][x] + 1
                o_cnt[y][x] = o_cnt[y][x + 1]
            elif mp[y][x] == "O":
                # For cell 'O', the 'I' count down is the same as below,
                # the number of 'O's rightward is one more than that in right cell
                i_cnt[y][x] = i_cnt[y + 1][x]
                o_cnt[y][x] = o_cnt[y][x + 1] + 1
            else:
                # For any other cells, get counts from right and below cells
                i_cnt[y][x] = i_cnt[y + 1][x]
                o_cnt[y][x] = o_cnt[y][x + 1]
                # Add the product of counts to the answer
                ans += i_cnt[y][x] * o_cnt[y][x]

    # Print the final answer
    print(ans)

main()