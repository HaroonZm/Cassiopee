class Tree:
    """
    Represents a tree data structure and supports heavy-light decomposition (HLD) related operations.
    """

    def __init__(self, n, edge):
        """
        Initializes the Tree object.

        Args:
            n (int): Number of nodes in the tree.
            edge (list of tuples): Each tuple (u, v) represents an undirected edge between nodes u and v (1-indexed).
        """
        self.n = n  # Total number of nodes
        # Adjacency list representation of the tree (0-indexed)
        self.tree = [[] for _ in range(n)]
        # Build the adjacency list; decrement 1 to adjust to 0-indexed
        for e in edge:
            self.tree[e[0] - 1].append(e[1] - 1)
            self.tree[e[1] - 1].append(e[0] - 1)

    def setroot(self, root):
        """
        Sets the root of the tree and computes parent, depth, order, and subtree sizes.

        Args:
            root (int): The node (0-indexed) that will become the root.
        """
        self.root = root  # The chosen root node
        self.parent = [None for _ in range(self.n)]  # Parent for each node
        self.parent[root] = -1  # Root's parent is -1 (undefined)
        self.depth = [None for _ in range(self.n)]  # Depth of each node from root
        self.depth[root] = 0
        self.order = []  # List for DFS order
        self.order.append(root)
        self.size = [1 for _ in range(self.n)]  # Size of the subtree rooted at each node (including itself)

        # DFS traversal to set parent, depth, and fill order
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:  # For each adjacent node
                if self.parent[adj] is None:  # Not visited yet
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)
        # Compute subtree sizes in post-order
        for node in self.order[::-1]:  # Process from leaves to root
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue  # Do not go upward
                self.size[node] += self.size[adj]

    def heavylight_decomposition(self):
        """
        Performs the heavy-light decomposition (HLD) on the tree.

        After running this, nodes are indexed by HLD order and head, next arrays are prepared.
        """
        self.order = [None for _ in range(self.n)]  # HLD order for each node
        self.head = [None for _ in range(self.n)]   # Head of the current heavy path for each node
        self.head[self.root] = self.root            # Head for root is itself
        self.next = [None for _ in range(self.n)]   # Heavy child for each node (if exists)
        stack = [self.root]
        order = 0  # Counter for HLD order assignment
        while stack:
            node = stack.pop()
            self.order[node] = order  # Assign next available order
            order += 1
            maxsize = 0
            # Find the heavy child (max subtree size)
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                if maxsize < self.size[adj]:
                    maxsize = self.size[adj]
                    self.next[node] = adj
            # Recurse for all non-heavy children
            for adj in self.tree[node]:
                if self.parent[node] == adj or self.next[node] == adj:
                    continue  # Skip parent & heavy child
                self.head[adj] = adj  # Light child's head is itself
                stack.append(adj)
            # Recurse for the heavy child (if any), inheriting the current node's head
            if self.next[node] is not None:
                self.head[self.next[node]] = self.head[node]
                stack.append(self.next[node])

    def range_hld(self, u, v, edge=False):
        """
        Decomposes the path from node u to node v into O(logN) ranges according to HLD.

        Args:
            u (int): Start node (0-indexed).
            v (int): End node (0-indexed).
            edge (bool): If True, returns ranges over edges, not nodes.

        Returns:
            list of tuples: Ranges (l, r) in HLD order that cover the path from u to v. 
        """
        res = []
        while True:
            # Ensure u comes before v in the HLD order
            if self.order[u] > self.order[v]:
                u, v = v, u
            # If u and v are on different heavy paths, move v up to its heavy path's parent
            if self.head[u] != self.head[v]:
                res.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.parent[self.head[v]]
            else:
                # When both are on the same path, record the direct segment
                res.append((self.order[u]+edge, self.order[v]+1))
                return res

    def subtree_hld(self, u):
        """
        Returns the HLD order range for the subtree of node u.

        Args:
            u (int): The node whose subtree's range is desired.

        Returns:
            tuple: (l, r) range in HLD order for the whole subtree rooted at u.
        """
        return self.order[u], self.order[u] + self.size[u]

    def lca_hld(self, u, v):
        """
        Finds the lowest common ancestor (LCA) of nodes u and v using HLD information.

        Args:
            u (int): First node (0-indexed).
            v (int): Second node (0-indexed).

        Returns:
            int: The LCA node.
        """
        while True:
            # Ensure u is higher up in HLD order than v
            if self.order[u] > self.order[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                v = self.parent[self.head[v]]
            else:
                return u

class BinaryIndexedTree:
    """
    Implements a 1-indexed Binary Indexed Tree (Fenwick Tree) supporting prefix sums and single point updates.
    """

    def __init__(self, n):
        """
        Initializes the Binary Indexed Tree (BIT).

        Args:
            n (int): The size of the underlying array.
        """
        self.n = n
        self.tree = [0 for _ in range(n + 1)]  # 1-indexed, thus n+1

    def sum(self, idx):
        """
        Computes the prefix sum up to and including index idx.

        Args:
            idx (int): Index up to which to compute the sum (1-indexed).

        Returns:
            int: Prefix sum up to idx.
        """
        res = 0
        while idx:
            res += self.tree[idx]
            idx -= idx & -idx  # Move to parent
        return res

    def add(self, idx, x):
        """
        Adds x to the value at index idx.

        Args:
            idx (int): Index at which to add x (1-indexed).
            x (int): Value to add.
        """
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx & -idx  # Move to next affected node

    def bisect_left(self, x):
        """
        Finds the smallest index such that the prefix sum is at least x.

        Args:
            x (int): The threshold value.

        Returns:
            int: The smallest index where the prefix sum >= x (1-indexed).
        """
        if x <= 0:
            return 0
        res, tmp = 0, 2 ** ((self.n).bit_length() - 1)
        while tmp:
            if res + tmp <= self.n and self.tree[res + tmp] < x:
                x -= self.tree[res + tmp]
                res += tmp
            tmp >>= 1
        return res + 1

class RAQandRSQ:
    """
    Range Add and Range Sum Query (RAQ and RSQ) using two Binary Indexed Trees.
    """

    def __init__(self, n):
        """
        Constructor initializing two BITs (for efficient range add and sum queries).

        Args:
            n (int): Size of the array (1-indexed).
        """
        self.bit1 = BinaryIndexedTree(n)
        self.bit2 = BinaryIndexedTree(n)

    def add(self, lt, rt, x):
        """
        Adds x to each element in the range [lt, rt).

        Args:
            lt (int): Left index (inclusive, 1-indexed).
            rt (int): Right index (exclusive, 1-indexed).
            x (int): Value to add.
        """
        self.bit1.add(lt, -x * (lt - 1))
        self.bit1.add(rt, x * (rt - 1))
        self.bit2.add(lt, x)
        self.bit2.add(rt, -x)

    def sum(self, lt, rt):
        """
        Returns the sum of elements in the range [lt, rt).

        Args:
            lt (int): Left index (inclusive, 1-indexed).
            rt (int): Right index (exclusive, 1-indexed).

        Returns:
            int: The sum over [lt, rt).
        """
        rsum = self.bit2.sum(rt - 1) * (rt - 1) + self.bit1.sum(rt - 1)
        lsum = self.bit2.sum(lt - 1) * (lt - 1) + self.bit1.sum(lt - 1)
        return rsum - lsum

import sys
input = sys.stdin.readline  # Use fast I/O

from operator import add

# Read the number of nodes
N = int(input())
E = []  # Edge list

# Read the tree structure
for i in range(N):
    inp = list(map(int, input().split()))
    k, c = inp[0], inp[1:]
    # Each node i specifies k children c[j]
    for j in range(k):
        E.append((i + 1, c[j] + 1))  # Edges as 1-indexed tuples

# Build the tree, set its root, and perform HLD
t = Tree(N, E)
t.setroot(0)
t.heavylight_decomposition()

# Initialize structure for range add & sum queries
r = RAQandRSQ(N)

res = []  # Results to print

# Read number of queries
Q = int(input())

for _ in range(Q):
    args = list(map(int, input().split()))
    q, p = args[0], args[1:]
    if q == 0:
        # Type 0: Add w to the path from root to v
        v, w = p
        # Decompose the path and apply the addition to each HLD segment
        for lt, rt in t.range_hld(0, v, edge=True):
            r.add(lt, rt, w)
    else:
        # Type 1: Query sum on the path from root to u
        s = 0
        u = p[0]
        # Accumulate the result from all HLD segments on this path
        for lt, rt in t.range_hld(0, u, edge=True):
            s += r.sum(lt, rt)
        res.append(s)

# Output all results
print('\n'.join(map(str, res)))