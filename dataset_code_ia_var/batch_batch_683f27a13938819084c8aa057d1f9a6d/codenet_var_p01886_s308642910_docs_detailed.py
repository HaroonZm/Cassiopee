from collections import defaultdict
import sys

# Assigning standard input and output reading/writing utilities for efficient reading and writing
readline = sys.stdin.readline
write = sys.stdout.write

def cross3(p0, p1, p2):
    """
    Calculate the cross product of vectors (p1 - p0) and (p2 - p0).
    
    This is used to determine the orientation of the triplet of points:
    - If result > 0: counterclockwise turn
    - If result < 0: clockwise turn
    - If result == 0: collinear points

    Args:
        p0 (tuple): The starting point, (x, y).
        p1 (tuple): The first endpoint, (x, y).
        p2 (tuple): The second endpoint, (x, y).

    Returns:
        int: The scalar value of the cross product.
    """
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

def solve():
    """
    Main function to process the points and compute an optimal geometric value.

    Steps:
    1. Read the number of points.
    2. Group all y-coordinates by their x-coordinate into a dictionary.
    3. Convert dictionary items to sorted list for ordered processing.
    4. For both the default and reversed orderings, call the helper function 'calc'
       which calculates a sequence of accumulated cross product values.
    5. Combine the results from both orderings to find the minimum possible sum.
    6. Output the result, formatted as an integer.
    """
    N = int(readline())                # Read the number of points
    mp = defaultdict(list)             # Dictionary to group y-coordinates by x

    # Read all points and populate the mapping
    for i in range(N):
        x, y = map(int, readline().split())
        mp[x].append(y)
    
    # Convert dictionary items to a list of (x, [y1, y2, ...]) and sort by x
    S = list(mp.items())
    S.sort()

    def calc(S, k):
        """
        Helper function to process sorted points and accumulate cross product values
        for convex hull construction.

        Args:
            S (list): List of tuples (x, [y-coordinates]) sorted by x.
            k (int): Sorting direction for y-coordinates. If False (0), descending, if True (1), ascending.
        
        Returns:
            list: Accumulated cross product values at each step of the sweep.
        """
        P = []          # Stack for one hull chain
        Q = []          # Stack for other hull chain
        r = 0           # Accumulated area-like value
        R = [0]         # List to store prefix sums

        # Traverse all x, y lists
        for x, ys in S:
            # Sort y-coordinates for this x in the specified direction
            ys.sort(reverse=bool(k))
            # Insert each (x, y) point
            for y in ys:
                p = (x, y)
                # Maintain stack P for convexity; pop until last 3 points make left turns
                while len(P) >= 2 and cross3(P[-2], P[-1], p) <= 0:
                    r += abs(cross3(P[-2], P[-1], p))
                    P.pop()
                P.append(p)
                # Maintain stack Q for convexity in the opposite sense
                while len(Q) >= 2 and cross3(Q[-2], Q[-1], p) >= 0:
                    r += abs(cross3(Q[-2], Q[-1], p))
                    Q.pop()
                Q.append(p)
            R.append(r)  # Add current r after all y's for this x
        return R

    R0 = calc(S, 0)        # Process points in increasing order of x and descending y
    S.reverse()            # Reverse the order for the other direction
    R1 = calc(S, 1)        # Process points in decreasing order of x and ascending y

    L = len(S)             # Total number of unique x positions
    ans = 10**20           # Initialize answer with a large value

    # Try all possible partitions and keep the minimum sum of both hull chains
    for i in range(L + 1):
        ans = min(ans, R0[i] + R1[-1 - i])

    # Output the final answer, with adjustment for integer division and rounding up
    write("%d\n" % ((ans + 1) // 2))

# Execute the main solving function
solve()