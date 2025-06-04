class LazySegmentTree:
    """
    A generic Lazy Segment Tree with range update and range query capabilities.

    Args:
        op (function): A binary operation (such as sum, min, max) to be used for queries.
        e (function): Function that returns the identity element for 'op'.
        mapping (function): Function that maps a lazy value to a segment value.
        composition (function): Function that composes two lazy values.
        ie (function): Function that returns the identity element for the lazy operator.
        init_array (list): Initial values to build the tree from.

    Segment values, identity elements, and lazy updates are all handled generically
    through the input functions.
    """

    def __init__(self, op, e, mapping, composition, ie, init_array):
        """
        Initializes the segment tree structure from the provided initial array.

        Args:
            op (function): See class docstring.
            e (function): See class docstring.
            mapping (function): See class docstring.
            composition (function): See class docstring.
            ie (function): See class docstring.
            init_array (list): See class docstring.
        """
        # Store operations
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.ie = ie

        l = len(init_array)

        def ceil_pow2(n):
            """Returns the smallest power of two >= n."""
            x = 0
            while (1 << x) < n:
                x += 1
            return x

        # Compute the smallest power of two no less than l for the tree size
        self.log = ceil_pow2(l)
        self.size = 1 << self.log  # Total number of leaves in the tree

        # d: stores the actual segment tree values (twice the size for full binary tree representation)
        self.d = [self.e() for _ in range(2 * self.size)]
        # lz: stores the lazy update values for internal nodes
        self.lz = [self.ie() for _ in range(self.size)]

        # Set leaf nodes to initial values
        for i, a in enumerate(init_array):
            self.d[i + self.size] = a

        # Build tree by calculating parents using the provided 'op'
        for i in range(self.size - 1, 0, -1):
            self.__update(i)

    def set(self, p, x):
        """
        Sets the value at position p to x.

        Args:
            p (int): Index to set (0-indexed).
            x: Value to set.
        """
        p += self.size
        # Push updates from the root to the affected leaf to ensure accuracy
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        self.d[p] = x
        # Update all parent nodes to reflect this change
        for i in range(1, self.log + 1):
            self.__update(p >> i)

    def __getitem__(self, p):
        """
        Returns the value at position p after applying all pending updates.

        Args:
            p (int): Index to fetch.

        Returns:
            The value at index p with all updates applied.
        """
        p += self.size
        # Push updates for this path
        for i in range(self.log, 0, -1):
            self.__push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        """
        Returns the result of folding 'op' over the range [l, r).

        Args:
            l (int): Left boundary (inclusive).
            r (int): Right boundary (exclusive).

        Returns:
            The result of op applied across the range.
        """
        if l == r:
            return self.e()

        l += self.size
        r += self.size

        # Push down all outstanding updates for the relevant segments
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push(r >> i)

        sml = self.e()  # left result
        smr = self.e()  # right result

        # Walk up the tree, accumulating answers as necessary
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

    def apply(self, l, r, f):
        """
        Applies the function f (lazy update) to every value in the interval [l, r).

        Args:
            l (int): Left boundary (inclusive).
            r (int): Right boundary (exclusive).
            f: The lazy update to apply.
        """
        if l == r:
            return

        l += self.size
        r += self.size

        # Before applying, tree needs to 'push' all updates on affected segments
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.__push(l >> i)
            if ((r >> i) << i) != r:
                self.__push((r - 1) >> i)

        l2 = l
        r2 = r

        # Apply lazy updates at the correct segments by visiting covers in O(log n)
        while l < r:
            if l & 1:
                self.__all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.__all_apply(r, f)
            l >>= 1
            r >>= 1

        l = l2
        r = r2

        # Update affected parents after propagation
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.__update(l >> i)
            if ((r >> i) << i) != r:
                self.__update((r - 1) >> i)

    def __update(self, k):
        """
        Updates the value of node k based on its children using 'op'.

        Args:
            k (int): The node index to update.
        """
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __all_apply(self, k, f):
        """
        Applies the lazy function 'f' to node k's value and lazily marks children.

        Args:
            k (int): The node index.
            f: Lazy update function.
        """
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def __push(self, k):
        """
        Pushes down any pending lazy updates at node k to its children.

        Args:
            k (int): The node index.
        """
        self.__all_apply(2 * k, self.lz[k])
        self.__all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.ie()

def atcoder_practice_k():
    """
    The driver function for the segment tree, tailored for AtCoder Practice Problem K.

    Performs a sequence of range affine updates and range sum queries.
    """
    import sys
    input = sys.stdin.buffer.readline

    # Read input
    N, Q = map(int, input().split())
    # Pack each element as a 64-bit integer: (value << 32) + count
    # count is always 1 for initial elements
    A = list(map(lambda x: (int(x) << 32) + 1, input().split()))
    MOD = 998244353  # The modulus to be used for all operations

    def e():
        """
        Returns the identity element for the range sum operation.

        Returns:
            int: the packed 0 value.
        """
        return 0

    def op(s, t):
        """
        Combines two segment nodes for the sum operation.

        Args:
            s (int): Packed (sum, count) of the left segment.
            t (int): Packed (sum, count) of the right segment.

        Returns:
            int: Packed (combined_sum, combined_count).
        """
        sv, sn = s >> 32, s % (1 << 32)
        tv, tn = t >> 32, t % (1 << 32)
        return (((sv + tv) % MOD) << 32) + sn + tn

    def mapping(f, a):
        """
        Applies an affine transformation to the segment node 'a'.

        Args:
            f (int): Packed (b, c) representing 'b * x + c'.
            a (int): Packed (sum, count) of the current segment.

        Returns:
            int: The updated packed node value.
        """
        fb, fc = f >> 32, f % (1 << 32)
        av, an = a >> 32, a % (1 << 32)
        return (((fb * av + fc * an) % MOD) << 32) + an

    def composition(f, g):
        """
        Composes two affine functions as lazy updates.

        Args:
            f (int): New affine to apply (b, c), so it's b*x+c.
            g (int): Existing affine lazy value (b', c').

        Returns:
            int: Packed affine representing application order f∘g.
        """
        fb, fc = f >> 32, f % (1 << 32)
        gb, gc = g >> 32, g % (1 << 32)
        return ((fb * gb % MOD) << 32) + ((gc * fb + fc) % MOD)

    def ie():
        """
        Returns the identity element for the affine function: (1, 0) (i.e., identity transformation).

        Returns:
            int: Packed identity affine.
        """
        return 1 << 32  # (1, 0): 1 in upper 32 bits, 0 in lower 32 bits

    # Build the segment tree
    st = LazySegmentTree(op, e, mapping, composition, ie, A)

    for _ in range(Q):
        k, *q = map(int, input().split())
        if k == 0:
            # Range affine update: apply l<=x<r: x := b*x+c mod MOD
            l, r, b, c = q
            st.apply(l, r, (b << 32) + c)
        else:
            # Range sum query: print sum of range [l, r)
            l, r = q
            a = st.prod(l, r)
            print(a >> 32)

if __name__ == "__main__":
    atcoder_practice_k()