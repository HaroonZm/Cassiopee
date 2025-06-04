def inpl():
    """
    Reads a line from input, splits it into separate values, converts each value to an integer,
    and returns the resulting list of integers.
    Returns:
        List[int]: A list of integers from the input line.
    """
    return list(map(int, input().split()))

# Read grid dimensions: Height (H) and Width (W) from input
H, W = inpl()

# Initialize the answer variable to 0. This will hold the maximum Manhattan distance found.
ans = 0

# Read the grid C, which is composed of H strings (each representing a row of the grid)
C = [input() for _ in range(H)]

# Repeat the process twice: once for rows, and then after transposing, for columns
for i in range(2):
    # L[h]: Index of the first occurrence of 'B' in row h, or -1 if not found
    L = [0]*H
    # R[h]: Index of the last occurrence of 'B' in row h, or -1 if not found
    R = [0]*H
    # Lk: List of row indices where 'B' was found (using first occurrence)
    Lk = []
    # Rk: List of row indices where 'B' was found (using last occurrence)
    Rk = []
    
    # Search each row for the first and last occurrence of 'B'
    for h in range(H):
        L[h] = C[h].find("B")  # First occurrence of 'B' in row h
        R[h] = C[h].rfind("B") # Last occurrence of 'B' in row h
        if L[h] >= 0:
            Lk.append(h)       # If 'B' was found (first occurrence), add row index to Lk
        if R[h] >= 0:
            Rk.append(h)       # If 'B' was found (last occurrence), add row index to Rk
    
    # Compute the maximum Manhattan distance between every pair of 'B' positions
    for lh in Lk:
        for rh in Rk:
            # Manhattan distance between two positions:
            #   abs(column of L[lh] and column of R[rh]) + abs(row difference)
            ans = max(ans, abs(L[lh] - R[rh]) + abs(lh - rh))
    
    # After first run (i == 0), transpose the grid to repeat the process over columns:
    if i == 0:
        # Transpose the grid so that rows and columns are swapped
        # zip(*C) combines items from each row into new rows (columns)
        C = ["".join(c) for c in zip(*C)]
        # After transposing, update H and W accordingly
        H, W = W, H

# Print the maximum Manhattan distance found between any two 'B's in the grid
print(ans)