class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree) implementation for efficient prefix sum queries and updates.
    Supports point addition and prefix sum queries in logarithmic time.
    """

    def __init__(self, n):
        """
        Initializes the Binary Indexed Tree with 'n' elements.

        Args:
            n (int): The number of elements. The internal array will be of size n + 1 (1-based indexing).
        """
        self.n = n
        # The tree is represented as a list of zeroes initially
        self.dat = [0] * (n + 1)

    def sum(self, i):
        """
        Computes the prefix sum from index 1 up to index i (inclusive).

        Args:
            i (int): The inclusive index up to which the prefix sum is calculated.

        Returns:
            int: The prefix sum from dat[1] to dat[i].
        """
        s = 0
        while i:
            s += self.dat[i]
            # Move index to parent node
            i -= i & -i
        return s

    def add(self, i, x):
        """
        Adds value 'x' to element at index 'i'.

        Args:
            i (int): The index (1-based) to add 'x' to.
            x (int): The value to be added.
        """
        while i <= self.n:
            self.dat[i] += x
            # Move index to the next responsible node
            i += i & -i


# Read number of elements and number of queries from input
N, Q = [int(_) for _ in input().split()]
# Read all queries; each query consists of a list of strings
Query = [input().split() for _ in range(Q)]

# Instantiate two Binary Indexed Trees (for range add / range sum)
BIT0 = BinaryIndexedTree(N + 1)
BIT1 = BinaryIndexedTree(N + 1)

# Process each query
for query in Query:
    c, *array = query
    array = list(map(int, array))  # Convert arguments to integers

    if c == '1':
        # Query: Compute and print the sum of elements in the range [a, b)
        a, b = array
        a -= 1   # Adjust 'a' for 0-based to 1-based transition

        # The result is calculated with the help of two BITs to handle range updates
        res = 0
        res += b * BIT1.sum(b) + BIT0.sum(b)
        res -= a * BIT1.sum(a) + BIT0.sum(a)
        print(res)

    else:
        # Query: Add 'x' to all elements in the range [a, b]
        a, b, x = array
        b += 1  # Open interval for easier BIT range processing

        # Update BITs to simulate range add operation using two trees
        BIT1.add(a, x)
        BIT0.add(a, -(a - 1) * x)
        BIT1.add(b, -x)
        BIT0.add(b, (b - 1) * x)