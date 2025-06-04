class SegmentTreeLazy:
    """
    Segment Tree with range update and lazy propagation.
    Supports range query and range update with user-defined functions.

    Attributes:
        h (int): Height of the segment tree.
        n (int): Number of leaves (next power of two from the input array length)
        val (list): Segment tree node values.
        laz (list): Lazy propagation values.
        func (callable): Function used for queries (merge two segments).
        op (callable): Function used for applying an update to a segment.
        merge (callable): Function used for merging lazy values.
        ti: Identity element for the value function.
        ei: Identity element for the lazy operation.
    """

    def __init__(self, arr, ti, ei, func, op, merge):
        """
        Initializes the segment tree and its internal structures.
        
        Args:
            arr (list): Initial array of values.
            ti: Identity element for value segment merging.
            ei: Identity element for lazy updates.
            func (callable): Function to merge two segments (e.g., sum or min).
            op (callable): Function to apply lazy update to a value.
            merge (callable): Function to merge two lazy values.
        """
        # Compute the height needed for a complete binary tree
        self.h = (len(arr) - 1).bit_length()
        # Total number of leaves (next power of two of the input length)
        self.n = 2 ** self.h
        self.func = func
        self.op = op
        self.merge = merge
        self.ti = ti
        self.ei = ei
        # Segment tree main values array, initialized to ti
        self.val = [ti for _ in range(2 * self.n)]
        # Copy the data array to the leaves
        for i in range(len(arr)):
            self.val[self.n + i] = arr[i]
        # Build internal node values bottom-up using func
        for i in range(self.n - 1, 0, -1):
            self.val[i] = self.func(self.val[2 * i], self.val[2 * i + 1])
        # Lazy array, all set to ei initially
        self.laz = [ei for _ in range(2 * self.n)]
        
    def reflect(self, k):
        """
        Computes the value of a node after applying any pending lazy updates.
        
        Args:
            k (int): Node index.
        Returns:
            Value after applying lazy update.
        """
        if self.laz[k] == self.ei:
            return self.val[k]
        # If there's a pending update, apply it over the node's value
        return self.op(self.val[k], self.laz[k])

    def propagate(self, k):
        """
        Pushes the lazy value of node k to its children and applies it to itself.
        
        Args:
            k (int): Node index.
        """
        if self.laz[k] == self.ei:
            return
        # Push the lazy value onto the children using merge
        self.laz[2 * k] = self.merge(self.laz[2 * k], self.laz[k])
        self.laz[2 * k + 1] = self.merge(self.laz[2 * k + 1], self.laz[k])
        # Apply the lazy value to the current node
        self.val[k] = self.reflect(k)
        # Clear out the lazy tag for the current node
        self.laz[k] = self.ei

    def thrust(self, k):
        """
        Ensures all pending lazy operations along the path to node k
        are propagated downward before accessing it.
        
        Args:
            k (int): Node index (leaf-based).
        """
        # Push propagations down the tree from root to node k
        for i in range(self.h, 0, -1):
            self.propagate(k >> i)

    def recalc(self, k):
        """
        Updates the value of all ancestors of leaf node k after updates.
        
        Args:
            k (int): Node index (leaf-based).
        """
        while k > 1:
            k >>= 1
            # When recalc-ing, ensure to reflect any lazy updates on both children
            self.val[k] = self.func(
                self.reflect(2 * k), self.reflect(2 * k + 1)
            )

    def update(self, lt, rt, x):
        """
        Applies a range update to [lt, rt) with the operation represented by x.

        Args:
            lt (int): Left bound (inclusive).
            rt (int): Right bound (exclusive).
            x: Operation/lazy value to apply.
        """
        lt += self.n
        rt += self.n
        vl, vr = lt, rt
        # Ensure all lazies are pushed for the target leaves
        self.thrust(lt)
        self.thrust(rt - 1)
        l, r = lt, rt
        # Apply updates and set lazy values as appropriate
        while l < r:
            if l & 1:
                self.laz[l] = self.merge(self.laz[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.laz[r] = self.merge(self.laz[r], x)
            l >>= 1
            r >>= 1
        # Re-calculate values for the segments affected by the update
        self.recalc(vl)
        self.recalc(vr - 1)

    def query(self, lt, rt):
        """
        Queries the range [lt, rt) using the merge (func) function.
        
        Args:
            lt (int): Left bound (inclusive).
            rt (int): Right bound (exclusive).
        Returns:
            Value for the range [lt, rt) after any pending updates.
        """
        lt += self.n
        rt += self.n
        # Push pending updates down to the leaves first
        self.thrust(lt)
        self.thrust(rt - 1)
        vl = vr = self.ti
        l, r = lt, rt
        # Collect results from segments covering the range
        while l < r:
            if l & 1:
                vl = self.func(vl, self.reflect(l))
                l += 1
            if r & 1:
                r -= 1
                vr = self.func(self.reflect(r), vr)
            l >>= 1
            r >>= 1
        # Merge left and right results together
        return self.func(vl, vr)

import sys
input = sys.stdin.buffer.readline

MOD = 998244353

# Read size of array and number of queries
N, Q = map(int, input().split())

# Read array and encode each value as a * MOD + 1 for dual value storage
arr = [a * MOD + 1 for a in map(int, input().split())]

ti = 0      # Identity for data values
ei = MOD    # Identity for lazy operations

def func(a, b):
    """
    Merges two stored segment values.
    
    Args:
        a (int): Encoded value of the first node.
        b (int): Encoded value of the second node.
    Returns:
        int: Encoded merged result.
    """
    a1, a2 = divmod(a, MOD)
    b1, b2 = divmod(b, MOD)
    c1 = (a1 + b1) % MOD
    c2 = (a2 + b2) % MOD
    return c1 * MOD + c2

def op(a, x):
    """
    Applies a range lazy operation to a segment value.
    
    Args:
        a (int): Segment value (encoded).
        x (int): Lazy value (encoded).
    Returns:
        int: Result after operation, encoded.
    """
    a1, a2 = divmod(a, MOD)
    x1, x2 = divmod(x, MOD)
    c1 = (a1 * x1 + a2 * x2) % MOD
    c2 = a2
    return c1 * MOD + c2

def merge(x, y):
    """
    Merges two lazy values for propagation.
    
    Args:
        x (int): First lazy value (encoded).
        y (int): Second lazy value (encoded).
    Returns:
        int: Merged lazy value (encoded).
    """
    x1, x2 = divmod(x, MOD)
    y1, y2 = divmod(y, MOD)
    z1 = (x1 * y1) % MOD
    z2 = (x2 * y1 + y2) % MOD
    return z1 * MOD + z2

# Initialize the segment tree with the encoded array and supporting functions
st = SegmentTreeLazy(arr, ti, ei, func, op, merge)

res = []

# Process each query from the input
for _ in range(Q):
    q, *p = map(int, input().split())
    if q == 0:
        # Range update: multiply by b and add c to elements in [l, r)
        l, r, b, c = p
        st.update(l, r, b * MOD + c)
    else:
        # Range query: compute sum over [l, r)
        l, r = p
        res.append(st.query(l, r) // MOD)

# Output results of all queries, one per line
print('\n'.join(map(str, res)))