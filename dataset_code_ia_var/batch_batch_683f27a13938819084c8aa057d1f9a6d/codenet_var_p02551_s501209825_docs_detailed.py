class LazySegmentTree:
    """
    Lazy Segment Tree (遅延評価セグメント木) implementation supporting range queries and range updates.
    This structure is generic, allowing customization of the segment operations, mapping, and composition functions.
    """

    __slots__ = ["op_X", "e_X", "mapping", "compose", "id_M", "N", "log", "N0", "data", "lazy"]

    def __init__(self, op_X, e_X, mapping, compose, id_M, N, array=None):
        """
        Initializes the Lazy Segment Tree.

        Parameters:
            op_X (function): Binary operation for the segment data type.
            e_X (object): Identity element for the operation op_X.
            mapping (function): Function that applies a lazy operation to the node data.
            compose (function): Function that composes two lazy operations together.
            id_M (object): Identity element for the lazy operation type.
            N (int): Number of elements in the array.
            array (list, optional): Initial values for the segment tree (size N). If None, initializes with e_X.
        """
        # Store all provided functions and constants
        self.op_X = op_X          # The segment operation
        self.e_X = e_X            # The identity value for the operation
        self.mapping = mapping    # The operation applied to a node
        self.compose = compose    # How to combine two operations
        self.id_M = id_M          # The identity operation for lazy updates

        self.N = N                # Length of the underlying array
        self.log = (N - 1).bit_length()  # Number of layers (tree depth)
        self.N0 = 1 << self.log          # Total number of leaves (tree size rounded up to a power of two)

        # Initialize storage for tree data and lazy operations
        self.data = [e_X] * (2 * self.N0)   # The segment tree data (0-based, with leaves starting at self.N0)
        self.lazy = [id_M] * self.N0        # Stores the pending operations for lazy updates

        if array is not None:
            assert N == len(array), "Initial array length must match N"
            self.data[self.N0:self.N0 + self.N] = array  # Set initial values
            # Build the tree from leaves upward
            for i in range(self.N0 - 1, 0, -1):
                self.update(i)

    def point_set(self, p, x):
        """
        Sets the value at index p to x.

        Parameters:
            p (int): Index in [0, N).
            x (object): Value to set.
        """
        p += self.N0
        # Push down all pending updates affecting this index
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        # Update all ancestor nodes
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def point_get(self, p):
        """
        Gets the value at index p, with all pending operations applied.

        Parameters:
            p (int): Index in [0, N).
        Returns:
            The value at index p.
        """
        p += self.N0
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        """
        Computes the generalized segment operation over the half-open interval [l, r).

        Parameters:
            l (int): Left index (inclusive).
            r (int): Right index (exclusive).
        Returns:
            The result of op_X over the interval [l, r).
        """
        if l == r:
            return self.e_X
        l += self.N0
        r += self.N0
        # Push down all pending updates covering [l, r)
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)

        sml = smr = self.e_X
        while l < r:
            if l & 1:
                sml = self.op_X(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op_X(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op_X(sml, smr)

    def all_prod(self):
        """
        Applies the segment operation to all elements in the array.

        Returns:
            The result of op_X applied over the entire array.
        """
        return self.data[1]

    def apply(self, *args):
        """
        Applies an operation to either a single point or an interval.
        Overloaded for:
            - apply(p, f): applies operation f to index p.
            - apply(l, r, f): applies operation f to interval [l, r).

        Parameters:
            p (int): Index to apply operation (single point version).
            l (int): Left index (inclusive) for range.
            r (int): Right index (exclusive) for range.
            f (object): The operation to apply.
        """
        if len(args) == 2:
            # Point apply
            p, f = args
            p += self.N0
            for i in range(self.log, 0, -1):
                self.push(p >> i)
            self.data[p] = self.mapping(f, self.data[p])
            for i in range(1, self.log + 1):
                self.update(p >> i)
        else:
            # Range apply
            l, r, f = args
            if l == r:
                return
            l += self.N0
            r += self.N0
            for i in range(self.log, 0, -1):
                if (l >> i) << i != l:
                    self.push(l >> i)
                if (r >> i) << i != r:
                    self.push((r - 1) >> i)
            l2, r2 = l, r
            while l < r:
                if l & 1:
                    self.all_apply(l, f)
                    l += 1
                if r & 1:
                    r -= 1
                    self.all_apply(r, f)
                l >>= 1
                r >>= 1
            l, r = l2, r2
            for i in range(1, self.log + 1):
                if (l >> i) << i != l:
                    self.update(l >> i)
                if (r >> i) << i != r:
                    self.update((r - 1) >> i)

    def max_right(self, l, g):
        """
        Finds the maximum right index r >= l such that g(op_X(A[l],...,A[r-1])) == True.

        Parameters:
            l (int): Starting index.
            g (function): Monotonic predicate function on the segment operation result.

        Returns:
            int: Maximum r (l <= r <= N) such that g(op_X(A[l],...,A[r-1])) is True.
        """
        if l == self.N:
            return self.N
        l += self.N0
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e_X
        while True:
            # Move to the rightmost index in the left subtree where the predicate g remains True
            while l & 1 == 0:
                l >>= 1
            if not g(self.op_X(sm, self.data[l])):
                while l < self.N0:
                    self.push(l)
                    l <<= 1
                    if g(self.op_X(sm, self.data[l])):
                        sm = self.op_X(sm, self.data[l])
                        l += 1
                return l - self.N0
            sm = self.op_X(sm, self.data[l])
            l += 1
            if l & -l == l:
                break
        return self.N

    def min_left(self, r, g):
        """
        Finds the minimum left index l <= r such that g(op_X(A[l], ..., A[r-1])) == True.

        Parameters:
            r (int): Ending index.
            g (function): Monotonic predicate function on the segment operation result.

        Returns:
            int: Minimum l (0 <= l <= r) such that g(op_X(A[l],...,A[r-1])) is True.
        """
        if r == 0:
            return 0
        r += self.N0
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e_X
        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1
            if not g(self.op_X(self.data[r], sm)):
                while r < self.N0:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op_X(self.data[r], sm)):
                        sm = self.op_X(self.data[r], sm)
                        r -= 1
                return r + 1 - self.N0
            sm = self.op_X(self.data[r], sm)
            if r & -r == r:
                break
        return 0

    def update(self, k):
        """
        Updates the node at index k with its children after changes.

        Parameters:
            k (int): Index of the node to update.
        """
        self.data[k] = self.op_X(self.data[2 * k], self.data[2 * k + 1])

    def all_apply(self, k, f):
        """
        Applies operation f to the entire segment at node k and its children if necessary.

        Parameters:
            k (int): Node index.
            f (object): The lazy operation to apply.
        """
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.N0:
            self.lazy[k] = self.compose(f, self.lazy[k])

    def push(self, k):
        """
        Pushes down the lazy operation at node k to its children nodes.

        Parameters:
            k (int): Node index.
        """
        if self.lazy[k] is self.id_M:
            return
        self.data[2 * k] = self.mapping(self.lazy[k], self.data[2 * k])
        self.data[2 * k + 1] = self.mapping(self.lazy[k], self.data[2 * k + 1])
        if 2 * k < self.N0:
            self.lazy[2 * k] = self.compose(self.lazy[k], self.lazy[2 * k])
            self.lazy[2 * k + 1] = self.compose(self.lazy[k], self.lazy[2 * k + 1])
        self.lazy[k] = self.id_M

###############################################################################
# Problem-specific logic and customized segment tree operations begin here
###############################################################################

# Read input functions
import sys
readline = sys.stdin.readline
read = sys.stdin.read

# Problem input: board size n, number of queries q, then q lines for queries
n, q = map(int, readline().split())
lr = [list(map(int, readline().split())) for _ in range(q)]

# Define the segment tree operators and identity values for this problem (min query/set)
op_X = min                     # Segment-wise operation: minimum
e_X = n - 1                    # Minimum identity (max possible value within range)
mapping = min                  # Mapping and composition for range set operations
compose = min
id_M = n - 1                   # Identity for lazy operation is 'no change'

# Initialize LazySegmentTree for each direction (horizontal/vertical blocking)
# The last cell (index n-1) is set to 0, others to n-1 (unblocked)
sh = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n - 1] * (n - 1) + [0])
sw = LazySegmentTree(op_X, e_X, mapping, compose, id_M, n, array=[n - 1] * (n - 1) + [0])

# Initial answer: all interior cells excluding the border can be filled => (n-2)^2
ans = (n - 2) ** 2

# Process all queries
for t, x in lr:
    x -= 1  # Adjust to 0-based indexing
    if t == 1:
        # Query type 1: Block a column at x, limit rows by row index sw.point_get(x)
        idx = sw.point_get(x)
        # Block all columns in [1, idx) with value x (row index restriction)
        sh.apply(1, idx, x)
        ans -= (idx - 1)
    else:
        # Query type 2: Block a row at x, limit columns by column index sh.point_get(x)
        idx = sh.point_get(x)
        # Block all rows in [1, idx) with value x (column index restriction)
        sw.apply(1, idx, x)
        ans -= (idx - 1)

# Output the answer (number of accessible interior cells after all queries)
print(ans)