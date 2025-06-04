import sys
input = sys.stdin.readline

class Lazysegtree:
    """
    Segment Tree with Lazy Propagation to support range queries and updates.
    This specific implementation is for tracking inversion counts in a binary array.
    """

    def __init__(self, A, fx, ex, fm, em, fa, initialize=True):
        """
        Initializes the lazy segment tree.

        Args:
            A (list): Initial array where each element is a tuple (zero_count, one_count, inversion_count)
            fx (callable): The function used to merge two segments for queries.
            ex (tuple): The identity element for the segment tree, e.g., (0, 0, 0).
            fm (callable): The function to merge two lazy operations (monoid for operations).
            em (int/tuple): The identity element for lazy propagation (no-op).
            fa (callable): The function that describes how to apply a lazy operation to a node.
            initialize (bool): Whether to initialize segment tree data with input array `A`.
        """
        self.n = len(A)
        self.n0 = 2 ** (self.n - 1).bit_length()  # Smallest power of two >= n
        self.fx = fx if fx is not None else self.default_fx  # Function for range query (merging nodes)
        self.ex = ex    # Identity element for node values
        self.fm = fm    # Function for combining lazy operations
        self.em = em    # Identity element for lazy operation (no-op)
        self.fa = fa if fa is not None else self.default_fa  # Function to apply lazy operation to node
        self.lazy = [em] * (2 * self.n0)  # Lazy propagation array

        if initialize:
            # Fill the tree leaves with A, pad with ex if needed
            self.data = [self.ex] * self.n0 + A + [self.ex] * (self.n0 - self.n)
            # Build the tree bottom-up
            for i in range(self.n0 - 1, 0, -1):
                self.data[i] = self.fx(self.data[i * 2], self.data[i * 2 + 1])
        else:
            # When initialization is skipped, fill the whole tree with ex
            self.data = [self.ex] * (2 * self.n0)

    def default_fx(self, x, y):
        """
        Default merge/query function for the tree nodes.

        Args:
            x (tuple): Node data for left child (zeros, ones, inv_count)
            y (tuple): Node data for right child (zeros, ones, inv_count)

        Returns:
            tuple: The combined (zeros, ones, inv_count) for the parent segment.
        """
        zx, ox, tx = x
        zy, oy, ty = y
        return (zx + zy, ox + oy, tx + ty + ox * zy)

    def default_fa(self, ope, idx):
        """
        Default function to apply a lazy operation to a node.

        Args:
            ope (int): The operation to apply; in this problem, 0 means do nothing, 1 means reverse 0s and 1s.
            idx (int): The index of the node to apply the operation to.

        Returns:
            tuple: Modified data for the node.
        """
        if ope == 0:
            return self.data[idx]
        zero, one, inv = self.data[idx]
        # Swapping 0s and 1s: new inversion count is all possible pairs minus current inversions
        total = zero + one
        total_pairs = total * (total - 1) // 2
        ones_pairs = one * (one - 1) // 2
        zeros_pairs = zero * (zero - 1) // 2
        return (one, zero, total_pairs - ones_pairs - zeros_pairs - inv)

    def _ascend(self, k):
        """
        Updates the segment tree upwards from a node after performing updates.

        Args:
            k (int): Index in the tree to start ascending from (typically a leaf index).
        """
        k >>= 1
        c = k.bit_length()
        for j in range(c):
            idx = k >> j
            self.data[idx] = self.fx(self.data[2 * idx], self.data[2 * idx + 1])

    def _descend(self, k):
        """
        Pushes all pending lazy operations downwards to cover a certain node.

        Args:
            k (int): Index in the tree to propagate lazy operations for.
        """
        k >>= 1
        idx = 1
        c = k.bit_length()
        for j in range(1, c + 1):
            idx = k >> (c - j)
            if self.lazy[idx] == self.em:
                continue
            # Apply the lazy operation to both children
            self.data[2 * idx] = self.fa(self.lazy[idx], 2 * idx)
            self.data[2 * idx + 1] = self.fa(self.lazy[idx], 2 * idx + 1)
            self.lazy[2 * idx] = self.fm(self.lazy[idx], self.lazy[2 * idx])
            self.lazy[2 * idx + 1] = self.fm(self.lazy[idx], self.lazy[2 * idx + 1])
            # Clear the current node's lazy value
            self.lazy[idx] = self.em

    def query(self, l, r):
        """
        Queries the combined value for range [l, r) in the underlying array.

        Args:
            l (int): Start index (inclusive, 0-based).
            r (int): End index (exclusive, 0-based).

        Returns:
            tuple: The merged node value over the range, typically (zero, one, inversion_count).
        """
        L = l + self.n0
        R = r + self.n0
        # Propagate lazy updates so the values in this range are up-to-date.
        self._descend(L // (L & -L))
        self._descend(R // (R & -R) - 1)

        sl = self.ex  # Accumulates left side result
        sr = self.ex  # Accumulates right side result

        while L < R:
            if R & 1:
                R -= 1
                sr = self.fx(self.data[R], sr)
            if L & 1:
                sl = self.fx(sl, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return self.fx(sl, sr)

    def operate(self, l, r, x):
        """
        Applies a lazy update to all elements in range [l, r).

        Args:
            l (int): Start index (inclusive, 0-based).
            r (int): End index (exclusive, 0-based).
            x (int): The operation value to propagate (e.g., 1 for bit flip).
        """
        L = l + self.n0
        R = r + self.n0
        Li = L // (L & -L)
        Ri = R // (R & -R)
        # Ensure all lazy updates along the path to L and R are applied before updating
        self._descend(Li)
        self._descend(Ri - 1)

        # Apply the operation in the range using lazy propagation
        l0, r0 = L, R
        while L < R:
            if R & 1:
                R -= 1
                self.data[R] = self.fa(x, R)
                self.lazy[R] = self.fm(x, self.lazy[R])
            if L & 1:
                self.data[L] = self.fa(x, L)
                self.lazy[L] = self.fm(x, self.lazy[L])
                L += 1
            L >>= 1
            R >>= 1

        # After updates, rebuild parent nodes
        self._ascend(Li)
        self._ascend(Ri - 1)

# Read input size and queries
N, Q = map(int, input().split())
# Read the initial array and interpret as binary, converting to (zero, one, inv) for each element
*A, = map(int, input().split())
A = [(0, 1, 0) if a == 1 else (1, 0, 0) for a in A]

# Set up the segment tree for the problem.
# fx: query merge function, ex: identity, fm: operation merge (XOR for flip), em: no-op, fa: apply function
segtree = Lazysegtree(
    A,
    fx=None,                  # Use default_fx
    ex=(0, 0, 0),
    fm=lambda x, y: x ^ y,
    em=0,
    fa=None,                  # Use default_fa
    initialize=True
)

ans = []
for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        # Apply inversion (bit flip) over [l-1, r)
        segtree.operate(l - 1, r, 1)
    else:
        # Query number of inversions in [l-1, r)
        ans.append(segtree.query(l - 1, r)[2])

# Output all the query answers
for v in ans:
    print(v)