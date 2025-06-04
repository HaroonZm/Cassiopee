from bisect import bisect
from heapq import heappush, heappop
import sys

# Aliases for efficient IO
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Main function to solve the problem using path simulation, 
    prefix sum, and priority queue-based dynamic programming.
    Returns False if the program should stop, True otherwise.
    """
    cA = ord('A')  # ASCII value for 'A', used for indexing characters
    
    ds = "LURD"  # Direction string to map movement commands

    # Read initial health (hi) and maximum health (hm)
    hi, hm = map(int, readline().split())
    if hi == hm == 0:
        # End of input condition
        return False

    # Read grid dimensions: number of rows (R) and columns (C)
    R, C = map(int, readline().split())

    # Read grid 'A', converting each character to a 0-based index ('A' = 0, 'B' = 1, ...)
    A = [list(map(lambda x: (ord(x) - cA), readline().strip())) for _ in range(R)]

    # Read the number of cell types with associated health values
    T = int(readline())
    D = [0]*26  # Mapping from cell type index to health value
    for _ in range(T):
        c, d = readline().split()
        D[ord(c) - cA] = int(d)

    # Initial tile's health
    RS = [D[A[0][0]]]

    # Movement deltas for directions 'L', 'U', 'R', 'D'
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    x = 0  # Initial x position
    y = 0  # Initial y position

    # Read the number of movement segments
    S = int(readline())
    for _ in range(S):
        c, n = readline().split()
        dx, dy = dd[ds.index(c)]  # Get direction vector
        for _ in range(int(n)):
            # Move along the direction vector
            x += dx
            y += dy
            v = D[A[y][x]]  # Health value at the new tile
            if v:
                RS.append(v)
    
    L = len(RS)  # Total number of health events along the path

    # Prefix sum array to keep cumulative health pickups/tiles
    SS = [0]*(L+1)
    for i in range(L):
        SS[i+1] = SS[i] + RS[i]

    def check(h, i):
        """
        Given a current health h at position i, 
        find how many more tiles can be traversed before health runs out.

        Args:
            h (int): Current health value.
            i (int): Current position index in the RS list.

        Returns:
            tuple: (remaining_health_when_stop, stop_index)
        """
        # Find the rightmost index where cumulative health does not exceed current health
        idx = bisect(SS, SS[i] + h - 1)
        # Calculate remaining health at the stopping point
        return h - (SS[idx-1] - SS[i]), idx-1

    # Read number of potions and their heal values
    P = int(readline())
    PS = [int(readline()) for _ in range(P)]

    INF = 10**18  # A large number for DP initialization

    D = [INF] * (1 << P)  # DP array for minimum cost to each potion bitmask
    D[0] = 0  # Starting state has zero cost

    C = [0]*(L+1)  # Array to check if the endpoint is reachable in any DP state
    U = [0]*(1 << P)  # Array to skip already processed states

    hi, k = check(hi, 0)  # Initial check: (health left, path index reached)
    que = [(0, 0, k, hi)]  # Priority queue: (cost, bitmask, position, health)
    
    while que:
        df, state, k, h0 = heappop(que)
        if D[state] < df or U[state]:
            # State already processed with lower cost or visited
            continue
        C[k] += 1  # Mark this point as reached
        U[state] = 1  # Mark state as visited

        for i in range(P):
            n_state = state | (1 << i)  # Next state by using potion i
            if state == n_state:
                # Potion already used in this state
                continue
            # Use potion i to heal and move as far as possible
            h, k0 = check(min(h0 + PS[i], hm), k)
            n_df = df + max(h0 + PS[i] - hm, 0)  # Add cost if health exceeds max
            if n_df < D[n_state]:
                # If we have found a path with less cost, push to the queue
                D[n_state] = n_df
                heappush(que, (n_df, n_state, k0, h))

    if C[L]:
        # If endpoint is reachable in any state, print YES
        write("YES\n")
    else:
        # Otherwise, print NO
        write("NO\n")
    return True

# Continuously solve until an end condition is met
while solve():
    ...