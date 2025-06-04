mod = 998244353

class lazy_segtree(object):
    """
    Lazy Segment Tree supporting range affine transformations and range sum queries.
    Internal representation uses 1-based heap indexing for segment data and lazy operations.
    """

    def __init__(self, n_or_vec):
        """
        Initializes the lazy segment tree.
        Args:
            n_or_vec: int (size of array) or list/tuple (values to initialize, must be iterable of pairs (a, size))
        Each element in the segment tree stores a tuple (sum, count).
        """
        if isinstance(n_or_vec, int):
            # If given integer, create an array of the identity element
            self.n = n_or_vec
            v = [self.e()] * n_or_vec
        elif isinstance(n_or_vec, list) or isinstance(n_or_vec, tuple):
            # If given an array, use its size and values directly
            self.n = len(n_or_vec)
            v = n_or_vec
        # Height of the segment tree
        self.log = (self.n - 1).bit_length()
        # Total size (next power of two)
        self.size = 1 << self.log
        # Segment tree array (value, count) for all nodes
        self.d = [self.e()] * (2 * self.size)
        # Lazy propagation array (affine parameters (a, b))
        self.lz = [self.identity()] * self.size
        # Initialize the leaves
        for i, vi in enumerate(v):
            self.d[self.size + i] = vi
        # Build the upper levels of the tree
        for i in reversed(range(1, self.size)):
            self.update(i)

    def update(self, k):
        """
        Updates the value of the non-leaf node k using its children.
        Args:
            k: index of the node to update
        """
        self.d[k] = self.op(self.d[2*k], self.d[2*k+1])

    def all_apply(self, k, f):
        """
        Applies an affine transformation to node k.
        If k is an internal node, composes with its current lazy value for future pushes.
        Args:
            k: index of the node to apply to
            f: affine transformation (a, b)
        """
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        """
        Pushes the lazy operation at node k to its children and clears its own lazy value.
        Args:
            k: index of the node to push
        """
        self.all_apply(2*k, self.lz[k])
        self.all_apply(2*k+1, self.lz[k])
        self.lz[k] = self.identity()

    def set_x(self, p, x):
        """
        Sets the value at position p to x, updates ancestors appropriately.
        Args:
            p: index in array (0-based)
            x: tuple (sum, count)
        """
        p += self.size
        # Push all lazy values on the path to the leaf
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        self.d[p] = x
        # Update all ancestors
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        """
        Gets the value at position p (after applying any pending lazy operations).
        Args:
            p: index in array (0-based)
        Returns:
            Tuple (sum, count) for index p
        """
        p += self.size
        # Bring lazy values down for this position
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        return self.d[p]

    def show(self):
        """
        Prints the current state of the array (with all lazy updates applied)
        """
        print("show array")
        for i in range(self.n):
            print(self.get(i), end=" ")
        print("\n")

    def prod(self, l, r):
        """
        Computes the range-segment operation [l, r).
        Args:
            l: left (inclusive)
            r: right (exclusive)
        Returns:
            Tuple (sum, count) over the interval
        """
        if l == r:
            return self.e()
        l += self.size
        r += self.size
        # Push all relevant lazy values
        for i in reversed(range(1, self.log + 1)):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml = self.e()
        smr = self.e()
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        """
        Returns the result of the operation over the entire array.
        Returns:
            Tuple (sum, count) for the whole array
        """
        return self.d[1]

    def apply(self, p, f):
        """
        Applies affine transformation f to element at position p.
        Args:
            p: index in array (0-based)
            f: affine transformation (a, b)
        """
        p += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        """
        Applies affine transformation f to range [l, r).
        Args:
            l: left index (inclusive)
            r: right index (exclusive)
            f: affine transformation (a, b)
        """
        if l == r:
            return
        l += self.size
        r += self.size
        # Push all relevant lazy values for both l and r edges
        for i in reversed(range(1, self.log + 1)):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)

        l2, r2 = l, r
        # Apply to all affected nodes directly covering the range
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

        # Update all relevant ancestors to reflect changes
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r - 1) >> i)

    def max_right(self, l, g, target):
        """
        Finds the maximum r in [l, n] such that g(op(data[l:r]), target) holds.
        g must be monotonic (True -> True -> ... -> False -> False).
        Args:
            l: starting index
            g: predicate function, called as g(acc, target)
            target: external target data for predicate
        Returns:
            r: largest index where predicate holds
        """
        if l == self.n:
            return self.n
        l += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push(l >> i)
        sm = self.e()
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.d[l]), target):
                while l < self.size:
                    self.push(l)
                    l = (2 * l)
                    if g(self.op(sm, self.d[l]), target):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if l & -l == l:
                break
        return self.n

    def min_left(self, r, g, target):
        """
        Finds the minimum l in [0, r] such that g(op(data[l:r]), target) holds.
        g must be monotonic (False -> False -> True -> True).
        Args:
            r: exclusive end index
            g: predicate function, called as g(acc, target)
            target: external target data for predicate
        Returns:
            l: smallest index where predicate holds
        """
        if r == 0:
            return 0
        r += self.size
        for i in reversed(range(1, self.log + 1)):
            self.push((r - 1) >> i)
        sm = self.e()
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not g(self.op(self.d[r], sm), target):
                while r < self.size:
                    self.push(r)
                    r = (2 * r + 1)
                    if g(self.op(self.d[r], sm), target):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if r & -r == r:
                break
        return 0

    def op(self, L, R):
        """
        Range operation function: returns sum and count over two aggregates.
        Args:
            L: left child tuple (sum, count)
            R: right child tuple (sum, count)
        Returns:
            Tuple (sum, count) after merging
        """
        La, Lsize = L
        Ra, Rsize = R
        return (La + Ra) % mod, Lsize + Rsize

    def e(self):
        """
        Identity element for the operation (sum, count).
        Returns:
            (0, 0)
        """
        return (0, 0)

    def identity(self):
        """
        Identity affine function for lazy updates: (a=1, b=0)
        Returns:
            (1, 0)
        """
        return (1, 0)

    def mapping(self, L, R):
        """
        Applies affine transformation L=(a, b) to node value R=(sum, count).
        Args:
            L: affine parameters (a, b)
            R: tuple (sum, count) for a segment
        Returns:
            Transformed (sum, count)
        """
        La, Lb = L
        Ra, Rsize = R
        return (La * Ra + Lb * Rsize) % mod, Rsize

    def composition(self, L, R):
        """
        Composes two affine transformations: L(a1, b1) over R(a2, b2).
        The resulting transformation is: (a1*a2, b2*a1+b1)
        Args:
            L: outer affine (a1, b1)
            R: inner affine (a2, b2)
        Returns:
            New affine (a, b)
        """
        La, Lb = L
        Ra, Rb = R
        return (La * Ra) % mod, (Rb * La + Lb) % mod

if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 7)

    # Read number of array elements and queries
    N, Q = map(int, input().split())
    # Read initial array, store as (value, 1) pairs for each index
    A = [(a, 1) for a in map(int, input().split())]

    # Initialize the segment tree with initial values
    lazyseg = lazy_segtree(A)

    # Process queries
    for _ in range(Q):
        t, *arg = map(int, input().split())
        if t == 0:
            # Type 0 update: range affine (c, d) to [l, r)
            l, r, c, d = arg
            lazyseg.range_apply(l, r, (c, d))
        else:
            # Type 1 query: print sum in [l, r)
            l, r = arg
            print(lazyseg.prod(l, r)[0])