class LazySegmentTree:
    """
    Lazy Segment Tree implementation supporting range updates and range queries with lazy propagation.

    This class supports an arbitrary monoid and operator with user-provided functions, and assumes the number of elements is a power of two (internally pads if not).

    Attributes:
        n (int): Size rounded up to the nearest power of two.
        original_size (int): Original size of the input data.
        log (int): Height of the segment tree (number of bits needed for n).
        data (list): The segment tree nodes, storing the accumulated monoids.
        lazy (list): The array for pending operations for lazy propagation.
        me: The identity element of the monoid.
        oe: The identity element of the operator.
        fmm: Binary function to combine two monoids.
        fmo: Function to apply an operator to a monoid.
        foo: Binary function to combine two operators.
    """
    __slots__ = [
        "n", "original_size", "log", "data", "lazy",
        "me", "oe", "fmm", "fmo", "foo"
    ]

    def __init__(self, monoid_data, monoid_identity, operator_identity, func_monoid_monoid, func_monoid_operator, func_operator_operator):
        """
        Initializes a LazySegmentTree.

        Args:
            monoid_data (list): Initial list of monoid elements (one for each leaf).
            monoid_identity: The identity element for the monoid.
            operator_identity: The identity element for the operator.
            func_monoid_monoid (callable): Binary function for combining two monoids.
            func_monoid_operator (callable): Function for applying an operator to a monoid.
            func_operator_operator (callable): Binary function for combining two operators.
        """
        self.me = monoid_identity
        self.oe = operator_identity
        self.fmm = func_monoid_monoid
        self.fmo = func_monoid_operator
        self.foo = func_operator_operator

        self.original_size = len(monoid_data)
        self.log = (self.original_size - 1).bit_length()
        self.n = 1 << self.log  # Smallest power of two >= original_size
        # Initialize tree: the leaves [self.n:2*self.n) hold the data, pad to fill all leaves
        self.data = (
            [self.me] * self.n +
            list(monoid_data) +
            [self.me] * (self.n - self.original_size)
        )
        # Build tree bottom-up
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.fmm(self.data[2 * i], self.data[2 * i + 1])

        # Lazy array: store pending operations for each node
        self.lazy = [self.oe] * (self.n * 2)

    def replace(self, index, value):
        """
        Sets the value at the given index to `value`, propagating and recalculating as needed.

        Args:
            index (int): The 0-based index in the original array to update.
            value: The new value (a monoid).
        """
        index += self.n  # Move to leaf position in segment tree
        # Propagate pending operations from ancestors to this node
        for shift in range(self.log, 0, -1):
            i = index >> shift
            # Propagate operation from parent to children
            self.lazy[2 * i] = self.foo(self.lazy[2 * i], self.lazy[i])
            self.lazy[2 * i + 1] = self.foo(self.lazy[2 * i + 1], self.lazy[i])
            # Apply parent operation to parent data
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe
        # Update the leaf
        self.data[index] = value
        self.lazy[index] = self.oe
        # Update all ancestors
        i = index
        while i > 1:
            i //= 2
            self.data[i] = self.fmm(
                self.fmo(self.data[2 * i], self.lazy[2 * i]),
                self.fmo(self.data[2 * i + 1], self.lazy[2 * i + 1])
            )
            self.lazy[i] = self.oe

    def effect(self, l, r, operator):
        """
        Applies the operator to the range [l, r) (0-indexed, exclusive of r).

        Args:
            l (int): Left bound (inclusive).
            r (int): Right bound (exclusive).
            operator: The operator to apply to the range.
        """
        l += self.n
        r += self.n
        # Prepare unique indices that may have pending operations needing propagation
        indices = []
        L = l // 2
        R = r // 2
        lc = 0 if l % 2 else (L & -L).bit_length()
        rc = 0 if r % 2 else (R & -R).bit_length()
        for i in range(self.log):
            if rc <= i:
                indices.append(R)
            if L < R and lc <= i:
                indices.append(L)
            L //= 2
            R //= 2

        # Propagate all pending operations before updating the range
        for i in reversed(indices):
            self.lazy[2 * i] = self.foo(self.lazy[2 * i], self.lazy[i])
            self.lazy[2 * i + 1] = self.foo(self.lazy[2 * i + 1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # Apply the operator to all nodes covering the target range
        ll, rr = l, r
        while ll < rr:
            if ll % 2:
                self.lazy[ll] = self.foo(self.lazy[ll], operator)
                ll += 1
            if rr % 2:
                rr -= 1
                self.lazy[rr] = self.foo(self.lazy[rr], operator)
            ll //= 2
            rr //= 2

        # Recalculate the affected ancestors
        for i in indices:
            self.data[i] = self.fmm(
                self.fmo(self.data[2 * i], self.lazy[2 * i]),
                self.fmo(self.data[2 * i + 1], self.lazy[2 * i + 1])
            )
            self.lazy[i] = self.oe

    def folded(self, l, r):
        """
        Returns the folded (aggregated) value for the range [l, r) (0-indexed, exclusive of r),
        applying any pending operator propagation as needed.

        Args:
            l (int): Left bound (inclusive).
            r (int): Right bound (exclusive).

        Returns:
            The folded value (monoid) for the given range, after applying all necessary updates.
        """
        l += self.n
        r += self.n
        # Prepare unique indices that may have pending operations needing propagation
        indices = []
        L = l // 2
        R = r // 2
        lc = 0 if l % 2 else (L & -L).bit_length()
        rc = 0 if r % 2 else (R & -R).bit_length()
        for i in range(self.log):
            if rc <= i:
                indices.append(R)
            if L < R and lc <= i:
                indices.append(L)
            L //= 2
            R //= 2

        # Propagate updates on the path
        for i in reversed(indices):
            self.lazy[2 * i] = self.foo(self.lazy[2 * i], self.lazy[i])
            self.lazy[2 * i + 1] = self.foo(self.lazy[2 * i + 1], self.lazy[i])
            self.data[i] = self.fmo(self.data[i], self.lazy[i])
            self.lazy[i] = self.oe

        # Aggregate values in the range [l, r)
        left_folded = self.me
        right_folded = self.me
        ll, rr = l, r
        while ll < rr:
            if ll % 2:
                left_folded = self.fmm(
                    left_folded,
                    self.fmo(self.data[ll], self.lazy[ll])
                )
                ll += 1
            if rr % 2:
                rr -= 1
                right_folded = self.fmm(
                    self.fmo(self.data[rr], self.lazy[rr]),
                    right_folded
                )
            ll //= 2
            rr //= 2
        return self.fmm(left_folded, right_folded)

def atc2():
    """
    Driver function for a specific problem (ATC2 inversion count with bit flips).

    Monoid: Tuple (number of 0's, number of 1's, inversion count)
    Operator: 1 (flip) or 0 (do nothing)

    Query types:
        1 L R - flip [L-1, R)
        2 L R - print inversion count in [L-1, R)
    """
    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().split())
    # Initial array: treat each bit as (zeros, ones, inversions)
    monoid_data = [
        (0, 1, 0) if A == b'1' else (1, 0, 0)
        for A in input().split()
    ]

    def fmm(m1, m2):
        """
        Combine two monoid values.

        Args:
            m1, m2 (tuple): (zeros, ones, inversions)
        Returns:
            tuple: Combined (zeros, ones, inversions)
        """
        return (
            m1[0] + m2[0],  # zeros
            m1[1] + m2[1],  # ones
            m1[2] + m2[2] + m1[1] * m2[0]  # inversions + new inversions
        )

    def fmo(m, o):
        """
        Apply the operator to a monoid value.

        Args:
            m (tuple): (zeros, ones, inversions)
            o (int): 0 (no change) or 1 (flip)
        Returns:
            tuple: Updated (zeros, ones, inversions)
        """
        if o:
            # Flip zeros<->ones, and adjust the inversion count
            return (m[1], m[0], m[0] * m[1] - m[2])
        else:
            return m

    def foo(o1, o2):
        """
        Combine two operators.

        Args:
            o1 (int): first operator
            o2 (int): second operator
        Returns:
            int: combined operator
        """
        return o1 ^ o2  # Flip is its own inverse

    lst = LazySegmentTree(
        monoid_data,
        (0, 0, 0),  # monoid identity
        0,          # operator identity
        fmm, fmo, foo
    )
    ans = []
    for _ in range(Q):
        T, L, R = map(int, input().split())
        if T == 1:
            lst.effect(L - 1, R, 1)  # range flip [L-1, R)
        else:
            ans.append(lst.folded(L - 1, R)[2])  # report inversion count in [L-1, R)
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    atc2()