#!/usr/bin/env python3
# GRL_5_E: Tree - Range Query on Tree 2

class Edge:
    """
    Represents an undirected edge between two vertices in a graph.
    """
    __slots__ = ('v', 'w')

    def __init__(self, v, w):
        """
        Initialize an edge between vertices v and w.
        :param v: One endpoint of the edge.
        :param w: Other endpoint of the edge.
        """
        self.v = v
        self.w = w

    def either(self):
        """
        Returns one endpoint of the edge.
        :return: Vertex v
        """
        return self.v

    def other(self, v):
        """
        Given one endpoint, returns the other.
        :param v: One endpoint.
        :return: The other endpoint.
        """
        if v == self.v:
            return self.w
        else:
            return self.v

class Graph:
    """
    Represents an undirected graph using adjacency lists.
    """
    def __init__(self, v):
        """
        Initializes a Graph with v vertices.
        :param v: Number of vertices.
        """
        self.v = v
        self._edges = [[] for _ in range(v)]

    def add(self, e):
        """
        Adds an undirected edge to the graph.
        :param e: Edge to add.
        """
        self._edges[e.v].append(e)
        self._edges[e.w].append(e)

    def adj(self, v):
        """
        Returns a list of edges adjacent to vertex v.
        :param v: Vertex index.
        :return: List of Edge instances.
        """
        return self._edges[v]

    def edges(self):
        """
        Generator that yields all edges in the graph.
        """
        for es in self._edges:
            for e in es:
                yield e

class HeavyLightDecomposition:
    """
    Decomposes a tree into heavy paths for efficient path/range queries.
    """
    class _Path:
        """
        Represents a single heavy path in the decomposition.
        """
        __slots__ = ('nodes', '_index')

        def __init__(self):
            """
            Initializes an empty path.
            """
            self.nodes = []
            self._index = None

        @property
        def head(self):
            """
            Returns the head (first) node of the path.
            """
            return self.nodes[0]

        @property
        def size(self):
            """
            Returns the number of nodes in the path.
            """
            return len(self.nodes)

        def append(self, v):
            """
            Appends a node to the path.
            :param v: Node to append.
            """
            self.nodes.append(v)

        def index(self, v):
            """
            Returns the index of node v in the path.
            Uses lazy construction of the index mapping.
            :param v: Node to query.
            :return: Index within the path.
            """
            if self._index is None:
                self._index = {v: i for i, v in enumerate(self.nodes)}
            return self._index[v]

        def next(self, v):
            """
            Returns the next node in the path after v.
            :param v: Current node.
            :return: Next node.
            """
            return self.nodes[self.index(v) + 1]

    def __init__(self, graph, root):
        """
        Initializes the heavy-light decomposition of a tree.
        :param graph: Tree as a Graph instance.
        :param root: Root of the tree.
        """
        self._paths = {}              # Maps head node to _Path object
        self._parent = [root] * graph.v   # Stores parent of each node
        self._head = [-1] * graph.v       # Head node of the path each vertex is on
        self._find_paths(graph, root)

    def _find_paths(self, graph, root):
        """
        Runs heavy-light decomposition by determining heavy children and paths.
        :param graph: Graph instance representing the tree.
        :param root: Root vertex.
        """
        def create_path(v):
            """
            Builds a path starting from node v, following heavy children links.
            :param v: Starting node.
            :return: _Path object from v down heavy chain.
            """
            path = self._Path()
            u = v
            while u != -1:
                path.append(u)
                self._head[u] = v
                u = heavy[u]
            return path

        size = [1] * graph.v      # Subtree size for each vertex.
        maxsize = [0] * graph.v   # Size of the largest child subtree.
        heavy = [-1] * graph.v    # The heavy child for each node.
        visited = [False] * graph.v   # Tracks DFS visitations.

        # First DFS to compute sizes and find heavy children.
        stack = [root]
        while stack:
            v = stack.pop()
            if not visited[v]:
                # First time visiting v
                visited[v] = True
                stack.append(v)  # Place v back for post-processing after DFS
                for e in graph.adj(v):
                    w = e.other(v)
                    if not visited[w]:
                        self._parent[w] = v
                        stack.append(w)
            else:
                # Postorder processing for v
                if v != root:
                    p = self._parent[v]
                    if size[v] > maxsize[p]:
                        maxsize[p] = size[v]
                        heavy[p] = v
                    size[p] += size[v]
                for e in graph.adj(v):
                    w = e.other(v)
                    if w != self._parent[v] and w != heavy[v]:
                        self._paths[w] = create_path(w)

        # Finally add the root path
        self._paths[root] = create_path(root)

    def parent(self, v):
        """
        Returns the parent of vertex v in the tree.
        :param v: Node.
        :return: Parent node.
        """
        return self._parent[v]

    def paths(self):
        """
        Returns all paths in the decomposition.
        :return: Values view of paths (list of _Path objects).
        """
        return self._paths.values()

    def get_path(self, v):
        """
        Returns the heavy path containing node v.
        :param v: Node.
        :return: _Path object.
        """
        return self._paths[self._head[v]]

class PathSum2:
    """
    Provides range-add and path-sum queries on a tree via Heavy-Light Decomposition.
    """
    def __init__(self, graph, root):
        """
        Initializes path sum structures for the given tree.
        :param graph: Tree graph.
        :param root: Root node.
        """
        self.root = root
        self.hld = HeavyLightDecomposition(graph, root)
        # For each heavy path, create a RangeQuery structure for range updates/queries
        self.rq = {p.head: RangeQuery(p.size) for p in self.hld.paths()}

    def add(self, v, val):
        """
        Adds 'val' to all vertices on the path from root to vertex v (excluding root).
        :param v: Target node.
        :param val: Value to add.
        """
        u = v
        while u != self.root:
            path = self.hld.get_path(u)
            head = path.head
            # Determine the relevant segment on this path (exclude head if it's root)
            if head != self.root:
                i = path.index(head)
            else:
                i = path.index(path.next(head))
            j = path.index(u)
            self.rq[head].add(i + 1, j + 1, val)
            u = self.hld.parent(head)

    def get(self, v):
        """
        Returns the sum of values along the path from root to vertex v (excluding root).
        :param v: Target node.
        :return: Accumulated sum.
        """
        weight = 0
        u = v
        while u != self.root:
            path = self.hld.get_path(u)
            head = path.head
            i = path.index(head)
            j = path.index(u)
            weight += self.rq[head].sum(i + 1, j + 1)
            u = self.hld.parent(head)
        return weight

class BinaryIndexedTree:
    """
    Implements a one-based Binary Indexed Tree (Fenwick Tree) for prefix sums.
    """
    def __init__(self, n):
        """
        Initializes the BIT structure.
        :param n: Maximum index (size).
        """
        self.size = n
        self.bit = [0] * (self.size + 1)

    def add(self, i, v):
        """
        Adds value v at index i.
        :param i: Index (1-based).
        :param v: Value to add.
        """
        while i <= self.size:
            self.bit[i] += v
            i += (i & -i)

    def sum(self, i):
        """
        Computes prefix sum up to index i (inclusive).
        :param i: Index (1-based).
        :return: Prefix sum.
        """
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

class RangeQuery:
    """
    Supports range addition and range sum query using two BITs.
    """
    def __init__(self, n):
        """
        Initializes the structure for n elements.
        :param n: Number of elements.
        """
        self.size = n
        self.bit1 = BinaryIndexedTree(n + 1)
        self.bit2 = BinaryIndexedTree(n + 1)

    def add(self, i, j, v):
        """
        Adds value v to all elements in index range [i, j] (1-based, inclusive).
        :param i: Start index (1-based).
        :param j: End index (1-based).
        :param v: Value to add.
        """
        self.bit1.add(i, v * -i)
        self.bit1.add(j + 1, v * (j + 1))
        self.bit2.add(i, v)
        self.bit2.add(j + 1, -v)

    def sum(self, i, j):
        """
        Returns the sum of elements in [i, j] (1-based, inclusive).
        :param i: Start index (1-based).
        :param j: End index (1-based).
        :return: Range sum.
        """
        s = self.bit1.sum(j + 1) + (j + 1) * self.bit2.sum(j + 1)
        s -= self.bit1.sum(i) + i * self.bit2.sum(i)
        return s

def run():
    """
    Main function to execute the tree range query operations.

    Reads:
      - The number of vertices.
      - Tree edges (as adjacency lists).
      - The number of queries.
      - And then the queries themselves.

    Supports two query types:
      - 0 u val: Adds val to all nodes on root-to-u path (excluding root).
      - 1 u: Prints sum of weights on root-to-u path (excluding root).
    """
    n = int(input())
    g = Graph(n)

    # Read in the whole tree as adjacency lists
    for i in range(n):
        parts = [int(x) for x in input().split()]
        k, *cs = parts
        if k > 0:
            for j in cs:
                g.add(Edge(i, j))

    ps = PathSum2(g, 0)
    q = int(input())
    for _ in range(q):
        comargs = [int(i) for i in input().split()]
        com, *args = comargs
        if com == 0:
            u, val = args
            ps.add(u, val)
        elif com == 1:
            (u,) = args
            print(ps.get(u))
        else:
            raise ValueError('invalid command')

if __name__ == '__main__':
    run()