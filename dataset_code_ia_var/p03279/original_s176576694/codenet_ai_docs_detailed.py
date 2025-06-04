from bisect import bisect
from collections import defaultdict

class Bit:
    """
    Implementation of a Binary Indexed Tree (Fenwick Tree) for efficient prefix sums and updates.

    Attributes:
        size (int): The number of elements managed by the tree.
        tree (list): The internal array representing the binary indexed tree.
        depth (int): Number of bits required for indexing, used in lower_bound.
    """
    def __init__(self, n):
        """
        Initialize the BIT (Fenwick Tree).

        Args:
            n (int): Number of items to manage (the maximum index).
        """
        self.size = n
        self.tree = [0] * (n + 1)  # 1-based index
        self.depth = n.bit_length()

    def sum(self, i):
        """
        Compute the prefix sum of tree[1..i].

        Args:
            i (int): Index up to which the sum is computed (inclusive).

        Returns:
            int: The sum of elements from index 1 to i.
        """
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        """
        Add a value to the element at index i.

        Args:
            i (int): Index at which to add (1-based index).
            x (int): Value to add.
        """
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def debug_print(self):
        """
        Print the internal status of the BIT with indentation showing tree structure.

        For debugging purposes.
        """
        for i in range(1, self.size + 1):
            j = (i & -i).bit_length()
            print('  ' * j, self.tree[i])

    def lower_bound(self, x):
        """
        Find the lowest index such that the prefix sum is at least x.

        Args:
            x (int): The required prefix sum.

        Returns:
            tuple (int, int): (index, accumulated sum) such that
            sum of elements up to 'index-1' < x <= sum up to 'index'.
        """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_

# --- Main Logic Begins Here ---

# Read input values
n, m = map(int, input().split())  # n: number of x coordinates, m: number of y coordinates
xxx = list(map(int, input().split()))  # List of x coordinates
yyy = list(map(int, input().split()))  # List of y coordinates (must be sorted for bisect)

ab = defaultdict(set)  # Stores sets of 'b' for each possible 'a'
coordinates = set()    # Unique collection of 'b' values (distances)

# Preprocessing: For each x, determine its nearest y interval, and compute the deltas a and b
for x in xxx:
    # Only process x if it's within the range covered by yyy
    if x < yyy[0] or yyy[-1] < x:
        continue
    # Find index such that yyy[i-1] <= x < yyy[i]
    i = bisect(yyy, x)
    a = x - yyy[i - 1]       # Distance from x to left y boundary
    b = yyy[i] - x           # Distance from x to right y boundary
    ab[a].add(b)             # For each 'a', keep unique 'b' values
    coordinates.add(b)       # Store all unique 'b' values

# Set up BIT indexing for 'b' values. Indexing is shifted by 1 to allow for '0' sum positions.
# Map each sorted unique 'b' value to a unique index starting from 2
cor_dict = {b: i for i, b in enumerate(sorted(coordinates), start=2)}
cdg = cor_dict.get          # Quick access to index of given 'b'
bit = Bit(len(coordinates) + 1)  # Initialize BIT. Size +1 since index starts at 1, and we shift by 1.

# Initialize the tree at position 1 (special base case for dynamic programming)
bit.add(1, 1)

# Perform dynamic programming using the BIT structure
# Iterate over sorted 'a' values (ascending)
for a in sorted(ab):
    # For each possible 'b' corresponding to current 'a', map to BIT index
    # Sort in reverse order so that updates do not affect the computation for smaller indexes in the same iteration
    bbb = sorted(map(cdg, ab[a]), reverse=True)
    for b in bbb:
        # Update BIT at index b: sum ways from previous indices
        bit.add(b, bit.sum(b - 1))

# Output the total number of ways modulo 10^9 + 7
print(bit.sum(bit.size) % (10 ** 9 + 7))