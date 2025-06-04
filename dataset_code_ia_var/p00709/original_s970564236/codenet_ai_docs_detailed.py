def solve():
    """
    Main function to process multiple test cases of the carpet covering problem from standard input.

    For each test case:
    - Reads the grid dimensions and its content.
    - Identifies every possible maximal square ("carpet") made of 1s, encodes it as a bitmask.
    - Iteratively tries to cover the 1 positions by optimal usage of maximal carpets.
    - If after greedy covering some 1s remain, uses brute-force combinations to finish.
    - Prints the minimum number of carpets necessary to cover all 1s in the grid.

    Input terminates on a line where W == 0.

    Note: Assumes standard input provides the formatted problem data.
    """
    from itertools import combinations
    from sys import stdin
    file_input = stdin  # Standard input for reading

    while True:
        # Read grid width (W) and height (H)
        W, H = map(int, file_input.readline().split())

        # If W == 0, input ends
        if W == 0:
            break

        carpets = []  # List to store bitmask representations of all maximal carpets found
        state = 0     # Bitmask for all cells covered so far (initially empty)

        # Largest Square DP algorithm to find all maximal carpets (squares of 1s)
        prev = [0] * (W + 1)  # Previous row's DP values (left-padded for index convenience)
        for i in range(1, H + 1):
            f_line = file_input.readline().split()  # Read current line of the grid
            cur = [0] * (W + 1)                    # DP for current row (1-based indexing)

            # Go through each cell (1-based column index for DP)
            for j, tpl in enumerate(zip(f_line, prev, prev[1:]), start=1):
                p, p1, p2 = tpl  # p: current cell ("1" or "0"), p1: prev_row[j], p2: prev_row[j-1]
                if p == '1':
                    # This cell can be part of a square ending here
                    # The side length is 1 + min(top, left, topleft)
                    side = min(p1, p2, cur[j - 1]) + 1
                    cur[j] = side

                    # Build the bitmask of the found maximal square (carpet)
                    # Make a bitmask for a square of "side" width/height with its bottom-right at (i, j)
                    line_bit = (1 << side) - 1           # Bitmask for a row of size 'side'
                    line_bit <<= (j - side)              # Shift to correct column start
                    c_b = line_bit
                    # For the remaining rows of the square, stack equivalent rows above
                    for k in range(side - 1):
                        c_b <<= W                        # Shift up one "row" (in bitmask)
                        c_b += line_bit
                    c_b <<= (W * (i - side))             # Shift carpet mask to proper (row, col) in grid
                    carpets.append(c_b)                  # Store carpet mask
                else:
                    # For "0" cell, mark as covered in initial state (already covered/no need for carpet)
                    b = 1 << (j - 1)
                    b <<= (W * (i - 1))
                    state += b
            prev = cur  # Current row DP becomes previous for next

        flag = -1  # Variable to detect state stability after an iteration
        ans = 0    # Number of carpets used

        # Repeatedly remove carpets subsumed by others and apply unique possible coverings
        while flag != state:
            flag = state  # Snapshot of state before this iteration

            # 1. Remove carpets that are entirely contained in other carpets
            c_check = dict(zip(carpets, [False] * len(carpets)))  # Mark for removal if subsumed
            for c1, c2 in combinations(carpets, 2):
                if c_check[c1] or c_check[c2]:
                    continue
                overlap = c1 & c2
                if overlap == c2:
                    c_check[c2] = True  # c2 is contained in c1, mark c2 for removal
                elif overlap == c1:
                    c_check[c1] = True  # c1 is contained in c2, mark c1 for removal
            # Only keep carpets that are not subsumed
            carpets = []
            for k, v in c_check.items():
                if not v:
                    carpets.append(k)

            # 2. Find unit squares that can be covered only by one carpet; cover them greedily
            for i in range(W * H):
                b = 1 << i  # Bit for the i-th cell
                if b & state:
                    continue  # Already covered, skip
                t_carpets = []
                for c in carpets:
                    if b & c:
                        t_carpets.append(c)
                if len(t_carpets) == 1:
                    # Only one carpet can cover this cell, must use it
                    c = t_carpets[0]
                    state |= c        # Mark all cells in that carpet as covered
                    ans += 1          # Count this carpet as used
                    carpets.remove(c) # Remove this carpet from further consideration

            # 3. Update carpets to remove already covered bits
            carpets = list(set(c ^ (c & state) for c in carpets))

        # The target state is all bits (cells) set (i.e., all should be covered)
        goal = (1 << (W * H)) - 1

        if state == goal:
            # All 1s are covered, print answer and process next test case
            print(ans)
            continue

        # If greedy approach couldn't finish, try combinations of remaining carpets to cover all
        # Try using 1 more carpet, then 2, up to the number of carpets left
        for i in range(1, len(carpets) + 1):
            for t_carpets in combinations(carpets, i):
                t_state = state
                for c in t_carpets:
                    t_state |= c  # Add each selected carpet's coverage
                if t_state == goal:
                    print(ans + i)
                    break
                else:
                    continue
                break  # Break if solution found at this level
            else:
                continue
            break  # Outer break on first solution

# Call the main solve function
solve()