import bisect
import sys

# Increase the recursion limit to allow for deep recursions if needed
sys.setrecursionlimit(10**9)

# Use fast input reading method for performance in large inputs
input = sys.stdin.readline

def solve():
    """
    Reads input values N and M, followed by N integers representing points P.
    Calculates the maximum sum of four points where the sum does not exceed M. 
    
    The calculation is done by:
    1. Generating all possible sums of pairs of points (including the same point twice).
    2. Sorting these sums.
    3. For each sum, using binary search to find another sum such that their total does not exceed M.
    
    Returns:
        int or bool: The maximum sum of four points less than or equal to M, or
                     False if input indicates termination (N or M equals zero).
    """
    # Read the number of points (N) and the maximum allowed sum (M)
    N, M = map(int, input().split())
    
    # If either N or M is zero, terminate by returning False
    if N * M == 0:
        return False

    # Read the list of points P, prepending 0 for convenience in indexing
    P = [0] + [int(input()) for _ in range(N)]

    # Generate all possible sums of two points (i, j) with i <= j
    k = [P[i] + P[j] for i in range(N) for j in range(i, N)]
    
    # Sort the pair sums for efficient binary search
    k.sort()

    ret = 0  # This will keep track of the maximum valid sum found

    # Iterate over each pair sum in k
    for tmp in k:
        # If current sum exceeds M, no need to check further as k is sorted
        if tmp > M:
            break
        else:
            # Calculate the remaining allowed sum to reach M
            r = M - tmp
            
            # Find the insertion point to maintain order for r in k using binary search
            l = bisect.bisect_right(k, r)

            # If insertion point is at or beyond the length, add the largest sum available
            if l >= len(k):
                tmp += k[-1]
            # Otherwise add the largest sum not exceeding r
            elif l != 0:
                tmp += k[l - 1]

            # Update the maximum sum found if current sum is greater
            ret = max(ret, tmp)

    return ret


# List to store answers from multiple test cases
ans = []

# Continuously solve for multiple test sets until input indicates termination
while True:
    ret = solve()
    if ret:
        ans.append(ret)
    else:
        break

# Print all answers, each on a new line
print("\n".join(map(str, ans)))