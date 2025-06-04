from collections import deque
from itertools import permutations
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Main function to solve the tree bit-operations problem.

    It reads the following from stdin (the first lines):
        - N: number of nodes in the tree
        - M: number of queries
        - N-1 operation type lines
        - N-1 edges describing the tree structure
        - M queries: each query consists of two integers x, y

    For each query (x, y):
        - Computes the result of processing those inputs using a tree with
          node-specific operations, combining results up the tree according
          to a specific rule (alternating max/min per level).
        - Outputs the integer result.
    """
    N, M = map(int, readline().split())
    
    # Operation codes for each node: 0 for root, rest determined by ops.index()
    OP = [0]*N
    
    # List of possible node operations (performed on temporary variable T)
    ops = [
        "T=T&X\n",  # 0: AND with X
        "T=T&Y\n",  # 1: AND with Y
        "T=T|X\n",  # 2: OR with X
        "T=T|Y\n",  # 3: OR with Y
        "T=T^X\n",  # 4: XOR with X
        "T=T^Y\n"   # 5: XOR with Y
    ]

    # Read the operation of each non-root node and encode as its index in 'ops'
    for i in range(N-1):
        s = readline()
        OP[i+1] = ops.index(s)
    
    # Build adjacency list for tree (undirected graph)
    G = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, readline().split())
        G[u].append(v)
        G[v].append(u)
    
    # Prepare structures for BFS traversal
    used = [0]*N       # Visited nodes
    used[0] = 1        # Mark root as visited
    P = [-1]*N         # Parent for each node
    V = []             # List of traversal order (excluding root)
    D = [0]*N          # Depth of each node (root at depth 0)
    que = deque([0])   # BFS queue
    
    # BFS to establish parent, BFS order (V), and depths (D) for all nodes
    for i in range(N):
        v = que.popleft()
        d = D[v]+1
        for w in G[v]:
            if used[w]:
                continue
            used[w] = 1
            que.append(w)
            P[w] = v
            D[w] = d
            V.append(w)

    def check(x, y):
        """
        Given values for x and y (interpreted as 3-bit values),
        simulate the propagation of bit-operations up the tree.

        Returns the result of applying all operations according to the tree
        structure to the input bits x and y.

        Parameters:
        x (int): 3-bit integer representing the X input
        y (int): 3-bit integer representing the Y input

        Returns:
        int: Computed value at the root of the tree
        """
        # S[v]: Result at node v after applying node operation
        S = [0]*N
        for v in V:
            op = OP[v]
            s = S[P[v]]
            # Determine operation (distinguish AND/OR/XOR and X/Y targets)
            if op & 1:
                if op & 2:
                    s |= y
                elif op & 4:
                    s ^= y
                else:
                    s &= y
            else:
                if op & 2:
                    s |= x
                elif op & 4:
                    s ^= x
                else:
                    s &= x
            S[v] = s
        
        # T[v]: Combined result propagated towards the root
        T = [-1]*N
        for v in reversed(V):
            if T[v] == -1:
                T[v] = S[v]
            p = P[v]
            # Odd depth: propagate max; Even depth: min
            if D[v] & 1:
                T[p] = max(T[p], T[v]) if T[p] != -1 else T[v]
            else:
                T[p] = min(T[p], T[v]) if T[p] != -1 else T[v]
        return T[0]

    # Precompute answers for all possible combinations of 3 input bits
    Q = [(1, 1), (1, 0), (0, 1)]
    R = {}
    # Try all permutations of 3 input bits for both x and y inputs
    for (x0, y0), (x1, y1), (x2, y2) in permutations(Q):
        x = x0 + x1*2 + x2*4    # Encode as 3-bit integer
        y = y0 + y1*2 + y2*4
        d = check(x, y)         # Run check for these bits
        d0 = d & 1                              # Bit 0 result
        d1 = int((d & 2) > 0)                   # Bit 1 result
        d2 = int((d & 4) > 0)                   # Bit 2 result
        # Register all subtuples for later lookups (lengths 3, 2, 1)
        R[(x0, x1, x2), (y0, y1, y2)] = (d0, d1, d2)
        R[(x1, x2), (y1, y2)] = (d1, d2)
        R[(x2,), (y2,)] = (d2,)
    
    # Process all M queries
    for i in range(M):
        x, y = map(int, readline().split())
        c = 0         # Bit-position counter
        E = {}        # For nonzero bits: maps (bit,bit) -> index
        Q = []        # List of current (xi, yi) pairs (from lower bits to higher)
        x0 = x; y0 = y
        # Decompose x and y into respective bit pairs (0 or 1) for each position
        while x0 or y0:
            x1 = x0 & 1; y1 = y0 & 1
            if x1 or y1:
                E[(x1, y1)] = c    # Mark this bit-pair position
            Q.append((x1, y1))
            x0 >>= 1
            y0 >>= 1
            c += 1
        # If both numbers zero, result is always 0
        if not E:
            write("0\n")
            continue
        # Sort bit positions by least-significant bit
        S = list(E.keys())
        S.sort(key = E.__getitem__)
        x1 = tuple(p for p, q in S)
        y1 = tuple(q for p, q in S)
        d1 = R[x1, y1]
        # Map final results for each bit-position
        for p, q, d in zip(x1, y1, d1):
            E[(p, q)] = d
        # Recompose final integer answer from higher bits down
        Q.reverse()
        ans = 0
        for p, q in Q:
            if p or q:
                ans = (ans << 1) | E[(p, q)]
            else:
                ans <<= 1
        write("%d\n" % ans)

solve()