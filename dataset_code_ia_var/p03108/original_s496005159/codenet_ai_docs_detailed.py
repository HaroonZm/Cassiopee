class UnionFind:
    """
    Disjoint-set (Union-Find) data structure implementation.
    Efficiently keeps track of disjoint sets and supports union and find operations.

    Attributes:
        n (int): Number of elements/nodes.
        parents (list): Parent and size information for each node.
            - If parents[x] < 0, x is a root and -parents[x] is the set's size.
            - Else, parents[x] is the parent index of x.
    """
    def __init__(self, n):
        """
        Initialize UnionFind with n nodes. Each node starts as its own root.

        Args:
            n (int): Number of nodes/elements.
        """
        self.n = n
        self.parents = [-1] * n  # Each node is a root, with initial set size 1

    def find(self, x):
        """
        Find the root of the node x with path compression.

        Args:
            x (int): Node index to find the root of.

        Returns:
            int: Root index of the group containing x.
        """
        history = []
        # Traverse up the parent pointers until reaching the root
        while self.parents[x] >= 0:
            history.append(x)
            x = self.parents[x]
        # Path compression for all visited nodes
        for node in history:
            self.parents[node] = x
        return x

    def union(self, x, y):
        """
        Merge the sets containing nodes x and y.

        Uses union by size: attaches the smaller tree to the root of the larger one.

        Args:
            x (int): Index of first node.
            y (int): Index of second node.
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            # Already in the same group, no action needed
            return
        # Ensure the new root is the bigger group (by size)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        # Update the size of the new root (x)
        self.parents[x] += self.parents[y]
        # Set y's root to x
        self.parents[y] = x

    def size(self, x):
        """
        Return the size of the set containing node x.

        Args:
            x (int): Node index.

        Returns:
            int: Number of nodes in the same group as x.
        """
        # Root's parents[x] is negative of group size
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        Check if nodes x and y are in the same set.

        Args:
            x (int): First node.
            y (int): Second node.

        Returns:
            bool: True if x and y are in the same group, False otherwise.
        """
        return self.find(x) == self.find(y)

from sys import stdin
input = stdin.buffer.readline

def main():
    """
    Main function for solving the problem.

    Reads the number of nodes and edges, then processes unions in reverse order to
    compute, for each step, the number of connected node pairs (unconnected before union).

    Input:
        n m
        i1 j1
        i2 j2
        ...
        im jm

        n: number of nodes
        m: number of connections (edges)
        (ik, jk): endpoints of the k-th edge (1-based indices)

    The program outputs m numbers: the number of unconnected pairs before each new edge is added (in input order).
    """
    n, m = map(int, input().split())

    # Read all connections (edges), storing endpoints as 0-based indices
    a = [0] * m
    b = [0] * m
    for ind in range(m):
        i, j = map(int, input().split())
        a[ind] = i - 1  # Convert to 0-based index
        b[ind] = j - 1  # Convert to 0-based index

    ans = [0] * m  # List to store answers (number of unconnected pairs at each step)
    uf = UnionFind(n)  # Initialize UnionFind with n nodes

    # Initial number of unordered pairs among n nodes (n choose 2)
    cnt = n * (n - 1) // 2

    # Process additions in reverse order to simulate removal of edges
    for ind in range(m - 1, -1, -1):
        ans[ind] = cnt  # Store current number of unconnected pairs
        if not uf.same(a[ind], b[ind]):
            # When connecting two distinct groups,
            # decrease cnt by the number of new pairs now connected
            cnt -= uf.size(a[ind]) * uf.size(b[ind])
            uf.union(a[ind], b[ind])

    # Output all recorded answers (in input order)
    for val in ans:
        print(val)

main()