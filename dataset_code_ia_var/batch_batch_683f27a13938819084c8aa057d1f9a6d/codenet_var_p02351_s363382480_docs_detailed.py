class BIT:
    """
    Implementation of a Binary Indexed Tree (Fenwick Tree) for point updates and prefix sum queries.
    """
    def __init__(self, n):
        """
        Initializes the Binary Indexed Tree.

        Args:
            n (int): The maximum number of elements in the tree.
        """
        self.size = n  # Store the size of the tree
        self.tree = [0] * (n + 1)  # Initialize the array with zeros (1-based indexing)

    def Sum(self, i):
        """
        Computes the prefix sum of elements from index 1 to i.

        Args:
            i (int): The end index of the prefix sum (1-based).

        Returns:
            int: The sum of elements from 1 to i.
        """
        s = 0  # Initialize sum
        # Traverse up the tree, adding values from relevant nodes
        while i > 0:
            s += self.tree[i]
            # Move to parent by removing the last set bit
            i -= i & -i
        return s

    def add(self, i, x):
        """
        Adds value x to the element at index i.

        Args:
            i (int): The index to update (1-based).
            x (int): The value to add.
        """
        # Traverse up the tree, updating all relevant nodes
        while i <= self.size:
            self.tree[i] += x
            # Move to next responsible node by adding the last set bit
            i += i & -i

class RangeUpdate:
    """
    Support range addition and range sum queries using two Binary Indexed Trees (BIT).
    """
    def __init__(self, n):
        """
        Initializes the data structure for a sequence of size n.

        Args:
            n (int): The number of elements in the range update structure.
        """
        # p and q are two BITs that will help to support range addition and sum efficiently
        self.p = BIT(n + 1)
        self.q = BIT(n + 1)

    def add(self, s, t, x):
        """
        Adds value x to all elements in the inclusive range [s, t].

        Args:
            s (int): Start of the range (1-based).
            t (int): End of the range (1-based).
            x (int): Value to be added.
        """
        t += 1  # Make the end point exclusive for easier calculations
        # Update internal BITs to simulate the range update
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def Sum(self, s, t):
        """
        Returns the sum of all elements in the inclusive range [s, t].

        Args:
            s (int): Start of range for sum (1-based).
            t (int): End of range for sum (1-based).

        Returns:
            int: The sum of elements from s to t, inclusive.
        """
        t += 1  # Make end exclusive
        # Compute the range sum using prefix sums from BITs
        return self.p.Sum(t) + self.q.Sum(t) * t - self.p.Sum(s) - self.q.Sum(s) * s

# Main interactive section
n, q = map(int, input().split())  # Read size of array and number of queries
tree = RangeUpdate(n)  # Initialize the range update/query data structure

# Process all queries
for _ in range(q):
    a, *b = map(int, input().split())  # Each operation starts with a and its arguments
    if a == 0:
        # Range add operation: add value b[2] to all elements from b[0] to b[1], inclusive
        tree.add(b[0], b[1], b[2])
    else:
        # Range sum query: print the sum of elements from b[0] to b[1], inclusive
        print(tree.Sum(b[0], b[1]))