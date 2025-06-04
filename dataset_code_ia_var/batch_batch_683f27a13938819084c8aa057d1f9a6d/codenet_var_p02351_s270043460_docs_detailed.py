class BinaryIndexedTree(object):
    """
    Implementation of a Binary Indexed Tree (Fenwick Tree) to perform prefix sum queries and single-point updates efficiently.
    """

    def __init__(self, n: int) -> None:
        """
        Initialize a Binary Indexed Tree with n elements.

        Args:
            n (int): The size of the array (number of elements to be managed by the BIT).
        """
        self.size = n
        # BIT representation uses 1-based indexing, so array is of size n+1
        self.bit = [0] * (self.size + 1)

    def add(self, i: int, v: int) -> None:
        """
        Performs an additive update: Adds value v to the element at index i.

        Args:
            i (int): The 1-based index of the element to be updated.
            v (int): The value to add to the element.
        """
        while i <= self.size:
            self.bit[i] += v
            # Move to the next responsible node by updating index with the lowest set bit
            i += (i & -i)

    def sum(self, i: int) -> int:
        """
        Computes the prefix sum from index 1 to i.

        Args:
            i (int): The 1-based index up to which the sum is computed.

        Returns:
            int: The sum of elements from index 1 to i.
        """
        s = 0
        while i > 0:
            s += self.bit[i]
            # Move to the parent node responsible for prefix sum
            i -= (i & -i)
        return s

class RangeQuery(object):
    """
    Supports range-add and range-sum queries on an array using two Binary Indexed Trees.
    Suitable for scenarios where both range updates and range queries are required.
    """

    def __init__(self, n: int) -> None:
        """
        Initialize the RangeQuery structure for an array of size n.

        Args:
            n (int): The number of elements in the array.
        """
        self.size = n
        # Use two BITs for efficient range operations; size+1 for 1-based indexing
        self.bit1 = BinaryIndexedTree(n + 1)
        self.bit2 = BinaryIndexedTree(n + 1)

    def add(self, i: int, j: int, v: int) -> None:
        """
        Increments all elements in the range [i, j] (1-based) by value v.

        Implements range update via the concept of difference arrays using BIT.

        Args:
            i (int): The starting 1-based index of the update range.
            j (int): The ending 1-based index of the update range.
            v (int): The value to add to all elements in the range.
        """
        # Update BIT1 to maintain a compensation term for prefix sum calculation
        self.bit1.add(i, v * -i)
        self.bit1.add(j + 1, v * (j + 1))
        # Update BIT2 to maintain the range increment amounts
        self.bit2.add(i, v)
        self.bit2.add(j + 1, -v)

    def sum(self, i: int, j: int) -> int:
        """
        Computes the sum of the elements in the range [i, j] (1-based inclusive).

        Args:
            i (int): The starting 1-based index of the query range.
            j (int): The ending 1-based index of the query range.

        Returns:
            int: The sum of values in the range [i, j].
        """
        # Calculate prefix sum up to (j+1), then subtract the prefix sum up to i to get [i, j]
        s = self.bit1.sum(j + 1) + (j + 1) * self.bit2.sum(j + 1)
        s -= self.bit1.sum(i) + i * self.bit2.sum(i)
        return s

if __name__ == "__main__":
    # Read the number of elements (n) and number of queries (q)
    n, q = map(int, input().split())
    rq = RangeQuery(n)

    for _ in range(q):
        inp = list(map(int, input().split()))
        com = inp[0]
        v = inp[1:]
        if com == 0:
            # Perform a range addition from v[0] to v[1] with value v[2]
            rq.add(v[0], v[1], v[2])
        else:
            # Perform a range sum query from v[0] to v[1] and print the result
            print(rq.sum(v[0], v[1]))