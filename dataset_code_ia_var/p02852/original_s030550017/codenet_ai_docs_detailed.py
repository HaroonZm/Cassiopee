class SegmentTree:
    """
    SegmentTree is a data structure that supports efficient range queries and point updates.
    Each operation (point update and range query) runs in O(log N) time.
    
    Methods:
        __init__(n, op, e): Initialize the segment tree with the number of elements,
                            a binary operation, and the identity element for the operation.
        built(array): Build the segment tree from a given initial array.
        update(i, val): Update the value at index i to the new value 'val'.
        get_val(l, r): Compute the result of the binary operation over the interval [l, r).
    """

    def __init__(self, n, op, e):
        """
        Initialize the SegmentTree.
        
        Args:
            n (int): Number of elements (the initial array size).
            op (callable): A binary associative function (e.g., min, max, sum, etc.).
            e (Any): The identity element for the binary operation.

        Example:
            # For range minimum query:
            SegmentTree(n, min, 10**18)
            # For range sum query:
            SegmentTree(n, lambda a, b: a + b, 0)
        """
        self.n = n                       # Number of elements in the input array
        self.op = op                     # Binary operation to use for queries
        self.e = e                       # Identity element for the operation
        # Compute the actual size of the tree (next power of 2)
        self.size = 2 ** ((n - 1).bit_length())
        # Initialize the tree with identity elements
        self.node = [self.e] * (2 * self.size)

    def built(self, array):
        """
        Build the segment tree using an initial array.
        
        Args:
            array (list): The list of initial values to build the tree from.
        """
        # Set the leaves of the tree to the initial values
        for i in range(self.n):
            self.node[self.size + i] = array[i]
        # Build the upper levels of the tree using the binary operation
        for i in range(self.size - 1, 0, -1):
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def update(self, i, val):
        """
        Update the value at index i to 'val'.
        
        Args:
            i (int): The index to update (0-based).
            val (Any): The new value to update at index i.
        """
        # Set the leaf to the new value
        i += self.size
        self.node[i] = val
        # Update all ancestors of the leaf
        while i > 1:
            i >>= 1
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def get_val(self, l, r):
        """
        Query the result of applying the binary operation over the interval [l, r).
        
        Args:
            l (int): Left index (inclusive, 0-based).
            r (int): Right index (exclusive, 0-based).
        
        Returns:
            The result of combining the elements in [l, r) using the binary operation.
        """
        l += self.size
        r += self.size
        res_l, res_r = self.e, self.e
        # Traverse the tree from leaves towards the root, aggregating results
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.node[r], res_r)
            l >>= 1
            r >>= 1
        return self.op(res_l, res_r)

# --- Main Program Logic ---

# Read the input: n - length of string, m - max jump size
n, m = map(int, input().split())
s = input()                         # Input string
INF = 10 ** 18                     # A large constant representing infinity

# Initialize the segment tree for min range queries with indices [0, n]
st = SegmentTree(n + 1, min, INF)
# Set the last position (goal) to 0 (no steps needed to finish from goal)
st.update(n, 0)

# Compute the minimum steps needed to reach the end from each position, in reverse order
for i in range(n - 1, -1, -1):
    if s[i] == "1":
        # Cannot stand on or move from this position
        continue
    # Calculate the minimum number of steps needed from positions ahead (up to m steps)
    tmp = st.get_val(i + 1, min(i + 1 + m, n + 1)) + 1
    st.update(i, tmp)

# If the start position is unreachable, output -1
if st.get_val(0, 1) >= INF:
    print(-1)
    exit()

# Reconstruct the actual jump sequence to reach the goal
ans = []
ind = 0      # Current index (start at the beginning)
for i in range(1, n + 1):
    # If moving from 'ind' to 'i' is optimal (cost decreases by 1), record the jump
    if st.get_val(ind, ind + 1) - 1 == st.get_val(i, i + 1):
        ans.append(i - ind)  # Jump length
        ind = i              # Move to the new position

# Output the jump sequence
print(*ans)