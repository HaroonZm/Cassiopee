import sys

# Overriding the built-in input function to read a line from standard input and strip whitespaces.
def input():
    """Reads a line from standard input and removes leading/trailing whitespace."""
    return sys.stdin.readline().strip()

# Utility function to generate a 2D list initialized with a default value.
def list2d(a, b, c):
    """
    Creates an a x b 2D list where each element is initialized to c.

    Args:
        a (int): Number of rows.
        b (int): Number of columns.
        c:      Initial value for each element.

    Returns:
        list: The resulting 2D list.
    """
    return [[c] * b for _ in range(a)]

# Utility function to generate a 3D list initialized with a default value.
def list3d(a, b, c, d):
    """
    Creates an a x b x c 3D list where each element is initialized to d.

    Args:
        a (int): First dimension size.
        b (int): Second dimension size.
        c (int): Third dimension size.
        d:      Initial value for each element.

    Returns:
        list: The resulting 3D list.
    """
    return [[[d] * c for _ in range(b)] for _ in range(a)]

# Utility function to generate a 4D list initialized with a default value.
def list4d(a, b, c, d, e):
    """
    Creates an a x b x c x d 4D list where each element is initialized to e.

    Args:
        a (int): First dimension size.
        b (int): Second dimension size.
        c (int): Third dimension size.
        d (int): Fourth dimension size.
        e:      Initial value for each element.

    Returns:
        list: The resulting 4D list.
    """
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

# Custom ceiling integer division.
def ceil(x, y=1):
    """
    Performs ceiling division of x by y.

    Args:
        x (int): Numerator.
        y (int, optional): Denominator (default 1).

    Returns:
        int: The ceiling of x divided by y.
    """
    return int(-(-x // y))

# Read a single integer from input.
def INT():
    """
    Reads and returns an integer from standard input.

    Returns:
        int: The integer read.
    """
    return int(input())

# Read multiple integers from input as separate values.
def MAP():
    """
    Reads a line of input, splits it by spaces, and converts each to an integer.

    Returns:
        iterator: An iterator of integers.
    """
    return map(int, input().split())

# Read a list of integers from input.
def LIST(N=None):
    """
    Reads and returns a list of integers from input.

    Args:
        N (int, optional): If specified, reads N lines (each an integer). Otherwise, reads one line and splits.

    Returns:
        list: List of integers.
    """
    return list(MAP()) if N is None else [INT() for _ in range(N)]

# Convenience functions for outputting common contest answers.
def Yes():
    """Prints 'Yes' (typically for contest output)."""
    print('Yes')

def No():
    """Prints 'No' (typically for contest output)."""
    print('No')

def YES():
    """Prints 'YES' (typically for contest output)."""
    print('YES')

def NO():
    """Prints 'NO' (typically for contest output)."""
    print('NO')

# Increase system recursion limit for deep recursions (e.g., DFS on large trees).
sys.setrecursionlimit(10 ** 9)

# Constants often used in programming problems
INF = float('inf')     # Infinity value
MOD = 10 ** 9 + 7      # Large prime modulus

class BIT2:
    """
    Binary Indexed Tree (Fenwick Tree) supporting range addition and range sum queries (also called dual BIT).

    This structure allows for efficient (log N) range additions and range sum queries:
    - Range add: Add a value to every element in a range [l, r).
    - Range sum: Get the sum of elements in a range [l, r).

    Attributes:
        N (int): Length of the supported array (1-based internally).
        data0 (list): Internal BIT array for the constant term.
        data1 (list): Internal BIT array for the coefficient term (for range updates).
    """

    def __init__(self, N):
        """
        Initializes the range-add/range-sum BIT (dual BIT).

        Args:
            N (int): Size of the array to support (0-based indexing). Internally increased by 1.
        """
        N += 1  # Increase by 1 for 1-based BIT indexing
        self.N = N
        self.data0 = [0] * N  # BIT for constant term
        self.data1 = [0] * N  # BIT for slope/linear coefficient term

    def _add(self, data, k, x):
        """
        Adds value x to element at position k in the provided BIT array.

        Args:
            data (list): The BIT array (data0 or data1).
            k (int): 0-based index in the array (will be converted to 1-based).
            x (int): Value to add.
        """
        k += 1  # Convert to 1-based index for BIT operations
        while k < self.N:
            data[k] += x
            k += k & -k  # Move to next responsible index

    def _get(self, data, k):
        """
        Computes prefix sum for indices [0, k] in the provided BIT array.

        Args:
            data (list): The BIT array (data0 or data1).
            k (int): 0-based index up to which the sum is calculated (inclusive).

        Returns:
            int: The prefix sum data[0] + ... + data[k].
        """
        k += 1  # Convert to 1-based index for BIT operations
        s = 0
        while k:
            s += data[k]
            k -= k & -k  # Move to parent index
        return s

    def add(self, l, r, x):
        """
        Adds value x to every element in the range [l, r) (0-based, inclusive of l, exclusive of r).

        Args:
            l (int): Start index of the range (inclusive).
            r (int): End index of the range (exclusive).
            x (int): Value to add.
        """
        # Update both BITs for range formulations. This is the "dual BIT" method.
        self._add(self.data0, l, -x * (l - 1))
        self._add(self.data0, r, x * (r - 1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)

    def query(self, l, r):
        """
        Computes the sum of values in the range [l, r) (0-based, inclusive of l, exclusive of r).

        Args:
            l (int): Start index of the range (inclusive).
            r (int): End index of the range (exclusive).

        Returns:
            int: The sum of elements in the range [l, r).
        """
        # Compute the sum using the two BITs.
        right_sum = self._get(self.data1, r - 1) * (r - 1) + self._get(self.data0, r - 1)
        left_sum = self._get(self.data1, l - 1) * (l - 1) + self._get(self.data0, l - 1)
        return right_sum - left_sum

# Read problem inputs: array size N and number of queries Q
N, Q = MAP()
# Initialize the range-add/range-sum BIT for N+1 elements to support queries up to N
bit = BIT2(N + 1)

# Process each query
for _ in range(Q):
    cmd, *arg = MAP()
    if cmd == 0:
        # Query type 0: range add operation
        s, t, x = arg
        # Note: add is [s, t+1) so that both s and t are included (matching 0-based semantics).
        bit.add(s, t + 1, x)
    else:
        # Query type 1: range sum operation
        s, t = arg
        # Query sum in [s, t+1), i.e., from s to t inclusive.
        print(bit.query(s, t + 1))