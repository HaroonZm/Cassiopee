import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Main function that processes a sequence of operations on an abstract N x N table,
    applies transformations, and computes a hash over a subrectangle at the end.

    Operations may include rotating views, swapping rows/columns, copying/pasting,
    and writing values. Table transformations are tracked efficiently using
    direction, position flips, and dynamic row/column mappings.
    """
    # Read the first line's parameters
    N, Q, A, B, C, D, E, F, G = map(int, readline().split())
    
    # Initialize transformation states:
    d = 0       # Current rotation: 0=0deg, 1=90deg, 2=180deg, 3=270deg
    rx = 0      # Horizontal axis flip flag (for x)
    ry = 0      # Vertical axis flip flag (for y)
    
    # X and Y maintain row/column mapping under swaps
    X = list(range(N))  # Mapping for 'rows' from original to current
    Y = list(range(N))  # Mapping for 'columns' from original to current

    def fc(d, x, y):
        """
        Returns (x', y') coordinates corresponding to (x, y) after a d*90° rotation.
        Parameters:
            d (int): rotation counter (0,1,2,3)
            x (int): x coordinate (column)
            y (int): y coordinate (row)
        Returns:
            (int, int): New coordinates after rotation
        """
        if d == 0:   # 0°: no rotation
            return x, y
        if d == 1:   # 90° clockwise
            return y, N - 1 - x
        if d == 2:   # 180°
            return N - 1 - x, N - 1 - y
        # d == 3: 270°
        return N - 1 - y, x

    mp = {}  # Dictionary for explicitly set/pasted table positions (sparse storage)

    for i in range(Q):
        # Parse each command line
        c, *g = readline().strip().split()
        c0, c1 = c[0], c[1]
        if c0 == "R":
            # Rotate or flip view
            if c1 == "L":
                # Rotate left (counter-clockwise 90°)
                d = (d - 1) % 4
            elif c1 == "R":
                # Rotate right (clockwise 90°)
                d = (d + 1) % 4
            elif c1 == "H":
                # Horizontal flip
                if d & 1:
                    rx ^= 1
                else:
                    ry ^= 1
            else: # "V": Vertical flip
                if d & 1:
                    ry ^= 1
                else:
                    rx ^= 1
        elif c0 == "S":
            # Swap (Row/Column swap)
            a, b = map(int, g)
            a -= 1; b -= 1
            if c1 == "R":
                # Row swap depending on orientation
                if d & 1:
                    # Oriented swap (columns become rows)      
                    if rx != ((d & 2) > 0):
                        a = N - 1 - a
                        b = N - 1 - b
                    X[a], X[b] = X[b], X[a]
                else:
                    # Row swap in canonical orientation
                    if ry != ((d & 2) > 0):
                        a = N - 1 - a
                        b = N - 1 - b
                    Y[a], Y[b] = Y[b], Y[a]
            else: # "C": column swap
                if d & 1:
                    # Column swap acts on Y, possibly reversed
                    if ((d & 2) == 0) != ry:
                        a = N - 1 - a
                        b = N - 1 - b
                    Y[a], Y[b] = Y[b], Y[a]
                else:
                    # Standard column swap
                    if ((d & 2) > 0) != rx:
                        a = N - 1 - a
                        b = N - 1 - b
                    X[a], X[b] = X[b], X[a]
        elif c0 == "C":
            # CP (copy-paste): Copy cell (x1,y1) to (x2,y2)
            y1, x1, y2, x2 = map(int, g)
            x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

            # Transform coordinates into canonical space based on transform
            x1, y1 = fc(d, x1, y1)
            x2, y2 = fc(d, x2, y2)
            if rx:
                x1 = N - 1 - x1
                x2 = N - 1 - x2
            if ry:
                y1 = N - 1 - y1
                y2 = N - 1 - y2

            # Row/col mapping after row/col swaps
            key1 = (X[x1], Y[y1])
            key2 = (X[x2], Y[y2])

            # If source not present, generate using formula; else copy value
            if key1 not in mp:
                xa, ya = key1
                mp[key2] = (ya * A + xa * B + A + B) % C
            else:
                mp[key2] = mp[key1]

        else:
            # WR (write): Write value v to (x, y)
            y, x, v = map(int, g)
            x -= 1; y -= 1

            # Transform into canonical coordinates
            x, y = fc(d, x, y)
            if rx:
                x = N - 1 - x
            if ry:
                y = N - 1 - y
            key = (X[x], Y[y])
            mp[key] = v

    # Hash computation:
    MOD = 10**9 + 7      # Large modulus for hash
    h = 314159265        # Initial hash value

    # Hash all values in the subrectangle [D-1:E), [F-1:G)
    for y in range(D-1, E):
        for x in range(F-1, G):
            # Back-transform coordinates for current view
            x0, y0 = fc(d, x, y)
            if rx:
                x0 = N - 1 - x0
            if ry:
                y0 = N - 1 - y0
            x0 = X[x0]
            y0 = Y[y0]
            key = (x0, y0)
            # Determine current cell value: explicit if available, else implicit formula
            if key in mp:
                v = mp[key]
            else:
                v = ((y0 + 1) * A + (x0 + 1) * B) % C
            h = (31 * h + v) % MOD

    # Output final hash
    write("%d\n" % h)

solve()