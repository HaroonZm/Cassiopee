import sys
from collections import deque

def find(x):
    """
    Find the representative/root of the set to which x belongs using path compression.
    
    Args:
        x (int): The element whose set representative is to be found.
    
    Returns:
        int: The representative/root of x's set.
    """
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])  # Path compression for efficiency
        return parent[x]

def unite(x, y):
    """
    Merge the sets containing elements x and y using union by rank.
    Also updates the size of sets.
    
    Args:
        x (int): First element.
        y (int): Second element.
    
    Returns:
        None
    """
    x = find(x)
    y = find(y)

    if x != y:
        # Union by rank heuristic for balancing
        if rank[x] < rank[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x, y):
    """
    Check if x and y belong to the same set.
    
    Args:
        x (int): First element.
        y (int): Second element.
    
    Returns:
        bool: True if x and y belong to the same set, False otherwise.
    """
    return find(x) == find(y)

# Read input more efficiently
input = sys.stdin.readline
N, M = map(int, input().split())  # N: number of nodes, M: number of edges

# Initialize Union-Find (Disjoint Set Union) data structures
parent = [i for i in range(N)]  # Parent link for each node; start as their own parent
rank = [1] * N                 # Rank for tree height heuristic
size = [1] * N                 # Size of the set to which each node belongs

# Read edges, adjust indices to zero-based, and reverse for processing in reverse order
edge = [tuple(map(int, input().split())) for _ in range(M)]
edge.reverse()
for i in range(M):
    # Convert from 1-based to 0-based indexing
    edge[i] = (edge[i][0] - 1, edge[i][1] - 1)

# Result deque to store the number of new connections created when adding each edge
res = deque()
for i in range(M):
    u = edge[i][0]
    v = edge[i][1]
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        # Nodes u and v are already connected; no new connections formed
        res.append(0)
    else:
        # Number of new pairs connected is product of sizes of two components
        res.append(size[root_u] * size[root_v])
        unite(root_u, root_v)

# Output the cumulative sum of connections after each edge removal (in original order)
ans = 0
for i in range(M):
    ans += res[M - 1 - i]  # Undo the earlier reversal to output answers in right order
    print(ans)