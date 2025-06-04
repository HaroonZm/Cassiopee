import sys
input = sys.stdin.readline

class BIT:
    """
    Binary Indexed Tree (Fenwick Tree) supporting range addition and point query operations.

    This implementation allows:
    - Adding a value to all elements in a range [l, r)
    - Querying the value at a single index

    All operations are performed in O(log N) time.

    Attributes:
        n (int): Size of the array.
        bit (List[int]): Internal tree for storing difference values.
    """

    def __init__(self, n):
        """
        Initializes the BIT for an array of size n.

        Args:
            n (int): The number of elements.
        """
        self.n = n
        # The tree uses 1-based indexing, so we allocate n+1 elements
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        """
        Internal function to add 'val' to the prefix ending at index 'i - 1'.

        This function walks downward in the tree structure to propagate 'val' 
        to all relevant nodes, enabling efficient range updates.

        Args:
            i (int): Index in 1-based numbering (exclusive).
            val (int): Value to add.
        """
        while i > 0:  # Traverse indices toward the beginning
            self.bit[i] += val
            i -= i & -i  # Move to the next responsible ancestor

    def add(self, l, r, val):
        """
        Adds the value 'val' to all elements in the half-open interval [l, r).

        Args:
            l (int): Left endpoint of the interval (0-indexed, inclusive).
            r (int): Right endpoint of the interval (0-indexed, exclusive).
            val (int): Value to add to each element in the interval.
        """
        # Convert to 1-based for internal representation
        self._add(r, val)
        self._add(l, -val)

    def get_val(self, i):
        """
        Retrieves the value at index 'i' after all range additions.

        Args:
            i (int): The index to query (0-indexed).

        Returns:
            int: The value at index 'i'.
        """
        i += 1  # Convert to 1-based indexing for internal representation
        res = 0
        # Traverse tree structure, accumulating range update effects
        while i <= self.n:
            res += self.bit[i]
            i += i & -i  # Move to next responsible child in BIT
        return res

# Read input values for n (size of the array) and q (number of queries)
n, q = map(int, input().split())
# Read in all queries. Each query is one line of either:
# - [0 l r x]: Add x to the interval [l-1, r)
# - [1 i]: Output value at position i-1
query = [list(map(int, input().split())) for _ in range(q)]

# Initialize the BIT for n elements
bit = BIT(n)

# Process each query in order
for qcmd in query:
    if qcmd[0] == 0:
        # Range add: add x to [l-1, r)
        _, l, r, x = qcmd
        bit.add(l - 1, r, x)
    else:
        # Point query: print value at position i-1
        _, i = qcmd
        print(bit.get_val(i - 1))