class Paper:
    """
    A class to model a rectangular paper and simulate folding operations, keeping track
    of the thickness at any point after any number of folds.

    Attributes:
        n (int): Current number of columns in the paper.
        m (int): Current number of rows in the paper.
        table (list of lists): 2D list representing thickness at each point.
    """

    def __init__(self, n, m):
        """
        Initialize the paper with given dimensions. All points start with a thickness of 1.

        Args:
            n (int): Number of columns of the paper (width).
            m (int): Number of rows of the paper (height).
        """
        self.n = n
        self.m = m
        # Create a m x n matrix, each element initialized to 1 (thickness)
        self.table = [[1] * n for _ in range(m)]

    def __str__(self):
        """
        Provide a string representation of the current paper thickness grid.
        
        Returns:
            str: String representation of the thickness table.
        """
        return str(self.table)

    def thickness(self, x, y):
        """
        Get the thickness of the paper at a specific coordinate.

        Args:
            x (int): Column index (0-based).
            y (int): Row index (0-based).

        Returns:
            int: The thickness at position (x, y).
        """
        return self.table[y][x]

    def fold(self, d, c):
        """
        Perform a folding operation on the paper.

        Args:
            d (int): Fold direction (1 for left-right fold, otherwise top-bottom fold).
            c (int): Position (distance from corresponding edge in folding).
        Returns:
            None
        """
        if d == 1:
            return self.foldl(c)  # Fold left/right
        else:
            return self.foldb(c)  # Fold top/bottom

    def foldl(self, c):
        """
        Simulate a left/right fold (vertical fold) at column 'c'.
        Everything left of column 'c' folds over everything right of 'c'.

        Args:
            c (int): The column on which to fold (0-based index from left).

        Returns:
            None
        """
        # The width of the new paper is the maximum of the two overlapping sides
        nn = max(c, self.n - c)
        # Initialize a new table with updated width, preserving row count
        tbl = [[0] * nn for _ in range(self.m)]
        for y in range(self.m):
            # Add thickness for the folded left side
            for x in range(c):
                tbl[y][x] += self.table[y][c - x - 1]
            # Add thickness for the right side (original or overlapped)
            for x in range(self.n - c):
                tbl[y][x] += self.table[y][c + x]
        self.n = nn
        self.table = tbl

    def foldb(self, c):
        """
        Simulate a top/bottom fold (horizontal fold) at row 'c'.
        Everything above row 'c' folds over everything below 'c'.

        Args:
            c (int): The row on which to fold (0-based index from top).

        Returns:
            None
        """
        # The height of the new paper is the maximum of the two overlapping sides
        mm = max(c, self.m - c)
        # Initialize a new table with updated height, preserving column count
        tbl = [[0] * self.n for _ in range(mm)]
        for x in range(self.n):
            # Add thickness for the folded top side
            for y in range(c):
                tbl[y][x] += self.table[c - y - 1][x]
            # Add thickness for the bottom side (original or overlapped)
            for y in range(self.m - c):
                tbl[y][x] += self.table[c + y][x]
        self.m = mm
        self.table = tbl

# Main process: repeatedly accept input, perform folding operations, and output queries
while True:
    # Read a scenario: paper dimensions (n,m), number of folds (t), query count (p)
    n, m, t, p = map(int, input().split())
    if n == m == t == p == 0:
        # Exit condition: all values are zero
        break

    # Instantiate the Paper object
    paper = Paper(n, m)

    # Perform all folding operations
    for i in range(t):
        d, c = map(int, input().split())
        paper.fold(d, c)

    # Answer all thickness queries
    for i in range(p):
        x, y = map(int, input().split())
        print(paper.thickness(x, y))