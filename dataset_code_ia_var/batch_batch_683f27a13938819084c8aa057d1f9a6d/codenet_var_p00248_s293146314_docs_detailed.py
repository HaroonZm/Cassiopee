class UnionSet:
    """
    Implementation of the Union-Find (Disjoint Set) data structure with path compression and union by size.

    Attributes:
        size (list): List tracking the size of each tree component.
        id (list): Parent pointers for each element, used to track connected components.
    """
    def __init__(self, nmax):
        """
        Initializes the UnionSet data structure.

        Args:
            nmax (int): Maximum number of elements in the set (exclusive upper bound).
        """
        self.size = [1] * nmax  # Each set has initial size 1
        self.id = [i for i in range(nmax + 1)]  # Each node is its own parent

    def root(self, i):
        """
        Finds the root of the node 'i' with path compression.

        Args:
            i (int): The node to find the root for.

        Returns:
            int: The root node of the component containing 'i'.
        """
        # Traverse parent pointers until reaching the root
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # Path compression: point i directly to its grandparent
            i = self.id[i]
        return i

    def connected(self, p, q):
        """
        Determines whether two nodes are in the same connected component.

        Args:
            p (int): First node.
            q (int): Second node.

        Returns:
            bool: True if p and q are in the same component, False otherwise.
        """
        return self.root(p) == self.root(q)

    def unite(self, p, q):
        """
        Unites the components containing p and q.

        Args:
            p (int): First node.
            q (int): Second node.
        """
        i, j = self.root(p), self.root(q)  # Find roots of p and q
        if i == j:
            return  # Already in same component, no action needed
        # Union by size: smaller tree joins larger one
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

def main():
    """
    Main function to process input and determine if a sequence of connections 
    forms a valid undirected graph where each node has degree at most 2 and 
    has no cycles (i.e., a set of simple paths).

    For each test case:
      - Read n and m (number of nodes and edges).
      - For each edge, check that connecting two nodes does not:
          - Make the degree of any node exceed 2
          - Introduce a cycle
      - Output "yes" if all conditions are satisfied, otherwise "no".
      
    Input ends when n == 0.
    """
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break  # Terminate on sentinel value

        n += 1  # Adjust to match original code (1-based index)
        u = UnionSet(n)
        f = [0] * n  # Degree counter for each node
        ans = True  # Validity flag for the current test case

        for _ in range(m):
            if ans:
                a, b = map(int, input().split())
                f[a] += 1
                f[b] += 1
                # Node degree cannot exceed 2
                if f[a] > 2:
                    ans = False
                if f[b] > 2:
                    ans = False
                # No cycle allowed, so nodes must not be already connected
                if u.connected(a, b):
                    ans = False
                # Unite the sets containing a and b
                u.unite(a, b)
            else:
                # Still read the input to align with input lines
                input()
        # Output result for the current test case
        print("yes" if ans else "no")

if __name__ == "__main__":
    main()