def count_subarrays_with_unique_sum_xor():
    """
    Reads an integer n from input and a list A of n integers.
    Computes the total number of contiguous subarrays (segments [l, r))
    where the sum of the elements is equal to their XOR.
    This function uses the two-pointer (sliding window) technique for an efficient solution.
    Prints the final answer.
    """
    n = int(input())
    A = list(map(int, input().split()))
    # ans stores the final count of valid subarrays
    ans = 0
    # r is the right endpoint of the current window (exclusive)
    r = 0
    # nowsum is the current sum of the window [l, r)
    nowsum = 0
    # nowxsum is the current XOR of the window [l, r)
    nowxsum = 0

    for l in range(n):
        # Expand the right boundary (r) of the window as much as possible
        # while the condition is satisfied: sum == xor
        while r < n and (nowsum + A[r] == (nowxsum ^ A[r])):
            nowsum += A[r]        # Add A[r] to current sum
            nowxsum ^= A[r]       # XOR A[r] to current xor
            r += 1                # Move right boundary to the right

        # The window [l, r) is the largest for this l satisfying the condition
        ans += r - l              # Count all valid subarrays starting at l

        # Shrink the window from the left by removing A[l]
        nowsum -= A[l]            # Remove A[l] from sum
        nowxsum ^= A[l]           # Remove A[l] from xor

    print(ans)