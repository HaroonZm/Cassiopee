from itertools import accumulate  # Import 'accumulate' function for prefix sums

def resolve():
    # Read two integers from input, separated by a space: 'n' (length of list) and 'k' (window size)
    n, k = map(int, input().split())

    # Read 'n' integers from input and store them as a list 'a'
    a = list(map(int, input().split()))

    # Create a new list 'x' where each element is the corresponding element from 'a'
    # If the element in 'a' is positive (>0), keep it, otherwise, replace it with 0
    # This is done using a list comprehension with a conditional expression
    x = [i if i > 0 else 0 for i in a]

    # Initialize a variable 'ans' to 0, which will store the maximum sum found
    ans = 0

    # Compute the prefix sum (cumulative sum) of list 'x' to enable fast sum queries on subarrays
    # 'accumulate(x)' returns an iterator of prefix sums (without initial 0),
    # so [0] + ... is used to add a leading zero for easier index calculations
    acc = [0] + list(accumulate(x))

    # Similarly, compute prefix sum of list 'a' and prepend with 0 for the same reason
    aaa = [0] + list(accumulate(a))

    # Iterate over all possible starting indices for selecting a window of size 'k' (inclusive), [0, n+1-k)
    for i in range(n + 1 - k):
        # For current starting index 'i', calculate the sum of all positive values in 'x',
        # except for those in the window [i, i+k)
        # acc[-1] is the total sum of all positive values,
        # acc[i] is the sum before our window,
        # acc[i+k] is the sum up to the end of our window,
        # so acc[i] + acc[-1] - acc[i+k] is the sum before the window plus sum after the window
        tmp = acc[i] + acc[-1] - acc[i + k]

        # Check if this sum 'tmp' is greater than the best answer so far, update if so
        if tmp > ans:
            ans = tmp

        # Compute the sum of elements in window [i, i+k) in the original array 'a',
        # which can be calculated quickly using prefix sums: aaa[i+k] - aaa[i]
        # Add this sum to 'tmp' to consider the case where we replace all values in the window
        # (even negatives) by their actual values (instead of zeros in 'x')
        # Update 'ans' if this total is greater than the current 'ans'
        if tmp + aaa[i + k] - aaa[i] > ans:
            ans = tmp + aaa[i + k] - aaa[i]

    # Print the maximum sum found as the result
    print(ans)

# This ensures that 'resolve()' is only called when this script is executed directly,
# and not when it is imported as a module in another script
if __name__ == '__main__':
    resolve()