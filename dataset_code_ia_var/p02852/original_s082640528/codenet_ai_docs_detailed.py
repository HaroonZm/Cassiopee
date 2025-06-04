import sys

def input():
    """
    Reads a line from standard input and strips trailing whitespace.

    :return: The input line as a stripped string.
    """
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    """
    Creates a 2D list (a x b) initialized with value c.

    :param a: Number of rows.
    :param b: Number of columns.
    :param c: Initial value for each element.
    :return: 2D list of dimensions a x b filled with value c.
    """
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    """
    Creates a 3D list (a x b x c) initialized with value d.

    :param a: First dimension size.
    :param b: Second dimension size.
    :param c: Third dimension size.
    :param d: Initial value for each element.
    :return: 3D list of dimensions a x b x c filled with value d.
    """
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def list4d(a, b, c, d, e):
    """
    Creates a 4D list (a x b x c x d) initialized with value e.

    :param a: First dimension size.
    :param b: Second dimension size.
    :param c: Third dimension size.
    :param d: Fourth dimension size.
    :param e: Initial value for each element.
    :return: 4D list filled with value e.
    """
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    """
    Returns the ceiling value of x divided by y.

    :param x: Numerator.
    :param y: Denominator. Default is 1.
    :return: The smallest integer not less than x / y.
    """
    return int(-(-x // y))

def INT():
    """
    Reads one line from input and returns it as an integer.

    :return: Input value as integer.
    """
    return int(input())

def MAP():
    """
    Reads one line from input and returns it as a map of integers.

    :return: A tuple of integers from the input line.
    """
    return map(int, input().split())

def LIST(N=None):
    """
    Reads a list of integers from input.

    :param N: If None, reads one line and splits into a list of integers.
              Otherwise, reads N lines and returns a list of integers.
    :return: List of integers.
    """
    if N is None:
        return list(MAP())
    else:
        return [INT() for _ in range(N)]

def Yes():
    """
    Prints 'Yes' to standard output.
    """
    print('Yes')

def No():
    """
    Prints 'No' to standard output.
    """
    print('No')

def YES():
    """
    Prints 'YES' to standard output.
    """
    print('YES')

def NO():
    """
    Prints 'NO' to standard output.
    """
    print('NO')

# Increase the recursion limit to handle deep recursions if necessary
sys.setrecursionlimit(10 ** 9)

# Large INF value used for initializations
INF = 10 ** 18

# Modulo value commonly used in competitive programming
MOD = 10 ** 9 + 7

class SegTree:
    """
    Segment Tree implementation supporting point updates and range queries.
    Useful for efficient min, max, sum (etc.) queries in a range.

    Public Methods:
        - update(i, x): update value at index i to x
        - query(l, r): query value in [l, r)
        - get(i): get value at index i
        - all(): get value for range [0, n)
    """

    def __init__(self, n, func, intv, A=[]):
        """
        Initializes segment tree with n elements, a function for combining elements, and an identity value.

        :param n: Number of elements (0-indexed).
        :param func: Binary function to combine two node values (e.g., min, max, sum, gcd).
        :param intv: The identity value for the function.
        :param A: Optional initial values as list. If given, populates the segment tree using A.
        """
        self.n = n                  # Number of elements
        self.func = func            # Segment function
        self.intv = intv            # Identity value
        
        # Find the smallest power of two >= n
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        # Create the segment tree array (indexed from 1)
        self.tree = [self.intv] * (n2 << 1)

        # If initial values are provided, populate the leaves, then build the tree upwards
        if A:
            # Set leaf values
            for i in range(n):
                self.tree[n2 + i] = A[i]
            # Fill internal nodes
            for i in range(n2 - 1, 0, -1):
                self.tree[i] = self.func(self.tree[i << 1], self.tree[(i << 1) | 1])

    def update(self, i, x):
        """
        Updates the value at index i to x.

        :param i: Index to update (0-indexed).
        :param x: New value to assign at index i.
        """
        i += self.n2
        self.tree[i] = x
        # Propagate changes up the tree
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[i << 1], self.tree[(i << 1) | 1])

    def query(self, a, b):
        """
        Queries in the range [a, b) and returns the combined value.

        :param a: Left index of range (inclusive, 0-indexed).
        :param b: Right index of range (exclusive, 0-indexed).
        :return: Combined value in the range [a, b).
        """
        l = a + self.n2
        r = b + self.n2
        res = self.intv
        # Left and right intervals handled separately
        while l < r:
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return res

    def get(self, i):
        """
        Returns the current value at index i.

        :param i: Index to retrieve (0-indexed).
        :return: Value at index i.
        """
        return self.tree[i + self.n2]

    def all(self):
        """
        Returns the combined value over the whole range [0, n).

        :return: Combined value of the tree's root.
        """
        return self.tree[1]

# Read input for problem parameters N (string length), M (maximum jump length)
N, M = MAP()
S = input()  # String representing the board (0=open, 1=blocked)

# Initialize dynamic programming table with INF as default value
dp = SegTree(N + 1, min, INF)  # Use segment tree for range minimum query
dp.update(N, 0)  # Goal is at position N, cost is 0

# Fill dp table backwards (from N-1 to 0)
for i in range(N - 1, -1, -1):
    # Skip blocked cells ('1's)
    if S[i] == '1':
        continue
    # Query next M reachable dp values for the minimum step count
    mn = dp.query(i + 1, min(N + 1, i + M + 1))
    if mn != INF:
        # Update dp[i] if it's possible to reach the end from here
        dp.update(i, mn + 1)

# If start position is still INF, cannot reach the goal
if dp.get(0) == INF:
    print(-1)
    exit()

# Reconstruct path by greedy choice (making largest possible moves that decrease step count)
cnt = dp.get(0)  # Current optimal number of moves needed from start
cur = 0          # Current position
prev = -1
ans = []
for i in range(1, N + 1):
    # Only consider reachable positions
    if dp.get(i) == INF:
        continue
    # If dp value drops, add a move from prev to i
    if dp.get(i) != cnt:
        prev = cur
        cur = i
        ans.append(cur - prev)
        cnt = dp.get(i)

# Output the answer as space-separated move lengths
print(*ans)