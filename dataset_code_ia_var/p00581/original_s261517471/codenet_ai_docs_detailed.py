def main():
    """
    Reads a grid of characters and computes a special count according to specified rules.
    
    The grid consists of characters 'J', 'O', and 'I'. The algorithm processes the grid from
    the bottom-right to the top-left, counting, for each cell containing 'J', the 
    product of:
        - the count of 'O's to its right on the same row (up to that point)
        - the count of 'I's in the same column below (up to that point).
    The final result is the sum of these products for all 'J's in the grid.

    Input:
        The first line contains two integers h and w: the height and width of the grid.
        The next h lines each contain a string of length w, consisting of only 'J', 'O', and 'I'.

    Output:
        Prints the computed total as an integer.
    """

    # Read grid dimensions
    h, w = map(int, input().split())
    # Read the grid as a list of lists, one list per row
    s = [list(input()) for _ in range(h)]

    # `ans` will hold the total count as per the algorithm
    ans = 0
    # `ci` is a list where ci[j] is the count of 'I's found so far in column j (from the bottom upwards)
    ci = [0 for _ in range(w)]

    # Iterate over each row starting from the bottom (h-1) to the top (0)
    for i in range(h - 1, -1, -1):
        # `co` is the count of 'O's encountered in current row from right to left
        co = 0
        # Iterate over each column in current row from rightmost (w-1) to leftmost (0)
        for j in range(w - 1, -1, -1):
            if s[i][j] == 'J':
                # For a 'J', accumulate the product of 
                # 'O's to its right in the same row (co), and 
                # 'I's below it in current column (ci[j])
                ans += co * ci[j]
            elif s[i][j] == 'O':
                # For an 'O', increment the current row's 'O' counter
                co += 1
            elif s[i][j] == 'I':
                # For an 'I', increment the current column's 'I' counter
                ci[j] += 1

    # Output the final aggregated result
    print(ans)

if __name__ == "__main__":
    main()