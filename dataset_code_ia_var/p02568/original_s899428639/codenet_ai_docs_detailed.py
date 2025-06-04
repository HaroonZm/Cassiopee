from typing import Callable, List, TypeVar

S = TypeVar("S")
F = TypeVar("F")

class LazySegmentTree:
    """
    Lazy Segment Tree.

    This segment tree supports range queries and range updates, where updates can be composed and applied lazily.
    It's implemented using a complete binary tree, and lazy propagation is used to efficiently process large segments.

    Attributes:
        e (S): The identity element for the data segment operation.
        op (Callable[[S, S], S]): The associative operation to combine data segments.
        id (F): The identity element for the lazy operation.
        mapping (Callable[[F, S], S]): Function to apply a lazy operation to a value in the segment tree.
        composition (Callable[[F, F], F]): Function to compose two lazy operations.
        _n (int): Size of input data.
        _log (int): Logarithm base 2 of the size (used for traversals).
        _size (int): Internal size of the tree array (a power of two covering n).
        tree (List[S]): The segment tree data.
        lazy (List[F]): The lazy operation flags for each node.
    """

    __slots__ = [
        "e",
        "op",
        "id",
        "mapping",
        "composition",
        "_n",
        "_log",
        "_size",
        "tree",
        "lazy",
    ]

    def __init__(
        self,
        a: List[S],
        e: S,
        op: Callable[[S, S], S],
        id_: F,
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
    ) -> None:
        """
        Initialize the LazySegmentTree.

        Args:
            a (List[S]): Initial array of elements.
            e (S): Identity element for 'op'.
            op (Callable[[S, S], S]): Function to merge two segments.
            id_ (F): Identity element for lazy operation.
            mapping (Callable[[F, S], S]): Function to apply lazy operation to a data value.
            composition (Callable[[F, F], F]): Function to compose two lazy operations.
        """
        self.e = e
        self.op = op
        self.id = id_
        self.mapping = mapping
        self.composition = composition

        self._n = len(a)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log

        # Build initial tree, padding with identity as needed
        self.tree = [e] * self._size + a + [e] * (self._size - self._n)
        for i in range(self._size - 1, 0, -1):
            self._update(i)
        # Initialize lazy propagation array
        self.lazy = [id_] * self._size

    def _update(self, k: int) -> None:
        """
        Recompute the data value at tree node k from its children.

        Args:
            k (int): Index of the node to update.
        """
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def _apply_all(self, k: int, f: F) -> None:
        """
        Apply a lazy operation to node k, updating its value and lazy tag.

        Args:
            k (int): Tree node to update.
            f (F): Operation to apply.
        """
        self.tree[k] = self.mapping(f, self.tree[k])
        if k < self._size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _push(self, k: int) -> None:
        """
        Push lazy updates from internal node k to its children.

        Args:
            k (int): Index to push.
        """
        self._apply_all(2 * k, self.lazy[k])
        self._apply_all(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.id

    def set(self, k: int, x: S) -> None:
        """
        Set a[k] = x.

        Args:
            k (int): Index to set.
            x (S): Value to set.
        """
        assert 0 <= k < self._n

        k += self._size
        # Push down any pending lazy updates
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        self.tree[k] = x
        # Update the ancestors
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def get(self, k: int) -> S:
        """
        Get value at position k.

        Args:
            k (int): Index to get.

        Returns:
            S: Value at a[k]
        """
        assert 0 <= k < self._n

        k += self._size
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        return self.tree[k]

    def prod(self, l: int, r: int) -> S:
        """
        Compute the operation of values in range [l, r).

        Args:
            l (int): Inclusive left index.
            r (int): Exclusive right index.

        Returns:
            S: Result of op(a[l], ..., a[r-1]).
        """
        assert 0 <= l <= r <= self._n

        if l == r:
            return self.e

        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push(r >> i)

        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def prod_all(self) -> S:
        """
        Compute the operation over the entire array.

        Returns:
            S: Result of op(a[0], ... a[n-1])
        """
        return self.tree[1]

    def apply(self, k: int, f: F) -> None:
        """
        Apply a lazy operation f to a[k].

        Args:
            k (int): Index to apply operation.
            f (F): Operation to apply.
        """
        assert 0 <= k < self._n

        k += self._size
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        self.tree[k] = self.mapping(f, self.tree[k])
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def apply_range(self, l: int, r: int, f: F) -> None:
        """
        Apply a lazy operation f to all elements in [l, r).

        Args:
            l (int): Inclusive left index.
            r (int): Exclusive right index.
            f (F): Operation to apply.
        """
        assert 0 <= l <= r <= self._n

        if l == r:
            return

        l += self._size
        r += self._size

        # Push down affected nodes before applying
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        l_tmp, r_tmp = l, r
        # Apply to left and right partial blocks
        while l < r:
            if l & 1:
                self._apply_all(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._apply_all(r, f)
            l >>= 1
            r >>= 1
        l, r = l_tmp, r_tmp

        # Update ancestors after performing operation
        for i in range(1, self._log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r - 1) >> i)

    def max_right(self, l: int, g: Callable[[S], bool]) -> int:
        """
        Find the maximum index r >= l such that predicate g(op(a[l], ..., a[r-1])) is true.

        Args:
            l (int): Start index.
            g (Callable[[S], bool]): Monotonic predicate.

        Returns:
            int: Largest r >= l with g(op(a[l], ..., a[r-1])) == True, or n if not found.
        """
        assert 0 <= l <= self._n
        assert g(self.e)

        if l == self._n:
            return self._n

        l += self._size
        for i in range(self._log, 0, -1):
            self._push(l >> i)
        sm = self.e

        while True:
            while not l & 1:
                l >>= 1

            if not g(self.op(sm, self.tree[l])):
                while l < self._size:
                    l *= 2
                    if g(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self._size

            sm = self.op(sm, self.tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self._n

    def min_left(self, r: int, g: Callable[[S], bool]) -> int:
        """
        Find the minimum index l <= r such that predicate g(op(a[l], ..., a[r-1])) is true.

        Args:
            r (int): Right index (exclusive).
            g (Callable[[S], bool]): Monotonic predicate.

        Returns:
            int: Smallest l <= r with g(op(a[l], ..., a[r-1])) == True, or 0 if not found.
        """
        assert 0 <= r <= self._n
        assert g(self.e)

        if not r:
            return 0

        r += self._size
        for i in range(self._log, 0, -1):
            self._push((r - 1) >> i)
        sm = self.e

        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1

            if not g(self.op(self.tree[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if g(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self._size

            sm = self.op(self.tree[r], sm)

            if (r & -r) == r:
                break

        return 0

MOD = 998244353

def range_affine_range_sum():
    """
    Solution for the Range Affine Range Sum problem.

    This function supports two types of queries on an array:
    - For a range [l, r), assign a[i] := b * a[i] + c (mod MOD).
    - For a range [l, r), return sum_{i=l}^{r-1} a[i] (mod MOD).

    Values and linear functions are encoded as packed 64-bit integers using high/low 32 bits.
    Input is read from stdin, and outputs are printed to stdout.
    """
    import sys

    readline = sys.stdin.buffer.readline

    N, Q = map(int, readline().split())
    A = [(i << 32) + 1 for i in map(int, readline().split())]  # Pack value and count

    e = 1  # Packed neutral element: value=0, count=1
    id_ = 1 << 32  # Packed identity: b=1, c=0 for affine, count=1

    def op(s, t):
        """
        Merge two packed segments, summing their values and counts.

        Args:
            s (int): Packed segment.
            t (int): Packed segment.

        Returns:
            int: Packed result.
        """
        sv, sn = s >> 32, s % (1 << 32)
        tv, tn = t >> 32, t % (1 << 32)
        # Sum values mod MOD, sum counts as is
        return (((sv + tv) % MOD) << 32) + sn + tn

    def mapping(f, a):
        """
        Apply packed affine map f=(b,c) to packed segment a=(sum, count).

        Args:
            f (int): Packed affine parameters.
            a (int): Packed sum/count segment.

        Returns:
            int: Packed result.
        """
        fb, fc = f >> 32, f % (1 << 32)
        av, an = a >> 32, a % (1 << 32)
        # new_sum = b * sum + c * count, count unchanged
        return (((fb * av + fc * an) % MOD) << 32) + an

    def composition(f, g):
        """
        Compose two packed affine operations.

        Args:
            f (int): Outer operation (b2, c2).
            g (int): Inner operation (b1, c1).

        Returns:
            int: Packed (b2*b1, c2*b1 + c1)
        """
        fb, fc = f >> 32, f % (1 << 32)
        gb, gc = g >> 32, g % (1 << 32)
        return ((fb * gb % MOD) << 32) + ((gc * fb + fc) % MOD)

    # Initialize segment tree with packing
    tree = LazySegmentTree(A, e, op, id_, mapping, composition)
    res = []
    for _ in range(Q):
        query = readline().split()
        com, l, r = map(int, query[:3])
        if com:
            # Sum query: unpack value from high 32 bits
            res.append(tree.prod(l, r) >> 32)
        else:
            # Affine update query: construct packed b and c
            b, c = map(int, query[3:])
            tree.apply_range(l, r, (b << 32) + c)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    range_affine_range_sum()