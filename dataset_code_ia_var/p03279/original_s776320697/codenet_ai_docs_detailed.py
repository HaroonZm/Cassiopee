from bisect import bisect
from collections import defaultdict

class Bit:
    """
    Implementation of a Binary Indexed Tree (Fenwick Tree) to efficiently handle prefix sums and updates modulo MOD.
    
    Attributes:
        size (int): The size of the Fenwick Tree.
        tree (List[int]): Internal storage for the Fenwick Tree, 1-based index.
        depth (int): Bit length of size to facilitate efficient traversals.
        mod (int): The modulo value for all operations.
    """
    def __init__(self, n, MOD):
        """
        Initialize the BIT structure.
        
        Args:
            n (int): The maximum size of the tree.
            MOD (int): The modulo applied for every update/sum.
        """
        self.size = n
        self.tree = [0] * (n + 1)  # 1-based indexing
        self.depth = n.bit_length()  # Needed for lower_bound
        self.mod = MOD

    def sum(self, i):
        """
        Compute the prefix sum of elements from 1 to i (inclusive) with modulo.
        
        Args:
            i (int): Index up to which the prefix sum is computed.
        
        Returns:
            int: The prefix sum from 1 to i modulo self.mod.
        """
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s % self.mod

    def add(self, i, x):
        """
        Add value x to element at index i.
        
        Args:
            i (int): The index to which x will be added (1-based).
            x (int): The value to add (modulo self.mod will be used).
        """
        while i <= self.size:
            self.tree[i] = (self.tree[i] + x) % self.mod
            i += i & -i

    def debug_print(self):
        """
        Print the internal state of the tree for debugging.
        Each entry is indented according to its lowest set bit.
        """
        for i in range(1, self.size + 1):
            j = (i & -i).bit_length()
            print('  ' * j, self.tree[i])

    def lower_bound(self, x):
        """
        Finds the smallest index such that the prefix sum >= x.
        
        Args:
            x (int): The threshold sum.
        
        Returns:
            tuple (int, int): Index where prefix sum first exceeds x, and sum up to just before.
        """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_

# Main section: reading and preprocessing inputs
n, m = map(int, input().split())
xxx = list(map(int, input().split()))  # List of n values (e.g., possible x-positions)
yyy = list(map(int, input().split()))  # List of m values (e.g., fixed y-positions)

ab = defaultdict(set)  # Mapping from a-values to a set of b-values
coordinates = set()    # Unique b-values across all entries

# Build table linking each relevant x in xxx to its neighbors in yyy
for x in xxx:
    # Skip x if it is outside the range of yyy
    if x < yyy[0] or yyy[-1] < x:
        continue
    i = bisect(yyy, x)
    a = x - yyy[i - 1]
    b = yyy[i] - x
    ab[a].add(b)        # Map distance a to set of b
    coordinates.add(b)  # Collect all b's (for coordinate compression)

# Compress b coordinates; start at index 2 to allow a zero-index entry in BIT
cor_dict = {b: i for i, b in enumerate(sorted(coordinates), start=2)}
cdg = cor_dict.get     # Shorthand for coordinate mapping

MOD = 10 ** 9 + 7      # Large prime modulo for answers

# Initialize BIT/Fenwick Tree (index 0 left unused; index 1 is intentionally used as "zero" in this logic)
bit = Bit(len(coordinates) + 1, MOD)
bit.add(1, 1)  # Initial state: one way at the first position

# Main DP-like update loop: iterate over sorted a's, for each update BIT for b's
for a in sorted(ab):
    # For each a, process its b's (sorted descending to avoid double counting)
    bbb = sorted(map(cdg, ab[a]), reverse=True)
    for b in bbb:
        # Count number of ways to reach up to (b - 1), and add that to position b
        bit.add(b, bit.sum(b - 1))

# Output the total number of ways for the largest position in BIT
print(bit.sum(bit.size))