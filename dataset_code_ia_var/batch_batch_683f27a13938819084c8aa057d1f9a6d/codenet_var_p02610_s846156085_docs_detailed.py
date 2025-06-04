import heapq

def greedy(limit, n):
    """
    Calculates the maximum sum by greedily selecting the largest available value 
    at each step from the provided limits, iterating from the last index to the first.

    Args:
        limit (List[List[int]]): A list where each element is a list of integers. 
                                 These represent the available "extra" values at each position.
        n (int): The total number of positions.

    Returns:
        int: The sum of the maximal values chosen at each step according to the greedy strategy.
    """
    ans = 0                      # Initialize the answer to 0
    hq = []                      # Priority queue (heap) to keep track of maximal values

    # Iterate from the last position to the first
    for i in range(n-1, -1, -1):
        # Push all available values at position i into the heap (as negatives, to simulate max-heap)
        for item in limit[i]:
            heapq.heappush(hq, -item)
        # If there are any values in the heap, pop the largest one and add its value to answer
        if hq:
            ans += -heapq.heappop(hq)

    return ans


def solve():
    """
    For each test case, processes a series of participants with left and right "scores" and an associated position.
    The function computes the maximum possible score by making optimal choices about which side each participant should stand.
    Uses a greedy strategy to select the best assignments for left and right, in addition to always taking the minimal base value.
    Prints the computed answer for the current test case.
    """
    n = int(input())                  # Number of participants
    limit_l = [[] for _ in range(n)]  # Extra scores for those who prefer left
    l_cnt = 0                        # Count of left-preferring participants
    limit_r = [[] for _ in range(n)]  # Extra scores for those who prefer right
    r_cnt = 0                        # Count of right-preferring participants
    ans = 0                          # Initialize total answer for the current test case

    # Process each participant
    for i in range(n):
        k, l, r = map(int, input().split())  # Read the position (k) and scores (l and r)
        ans += min(l, r)                     # Always take the minimal base value
        
        if l > r:
            # Prefers the left side; save the extra (l - r) to left limit list for their chosen position
            limit_l[k-1].append(l - r)
            l_cnt += 1
        else:
            # Prefers the right side; save the extra (r - l) to right limit list for mirrored position
            if n - k - 1 >= 0:
                limit_r[n - k - 1].append(r - l)
            # If (n - k - 1) is negative, right score can't be allocated, so nothing is added
            r_cnt += 1

    # Use the greedy algorithm to add maximal extra contributions from both left and right sides
    ans += greedy(limit_l, n)
    ans += greedy(limit_r, n)
    print(ans)
    return

def main():
    """
    Handles multiple test cases. Reads number of test cases, then processes each using the solve function.
    """
    t = int(input())              # Number of test cases
    for _ in range(t):
        solve()

# Execute the main function
main()