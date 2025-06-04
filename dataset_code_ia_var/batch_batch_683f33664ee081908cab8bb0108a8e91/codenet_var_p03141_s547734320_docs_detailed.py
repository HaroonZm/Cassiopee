import numpy as np

def read_input():
    """
    Reads the integer N and then reads N pairs of integers from standard input.
    
    Returns:
        Tuple:
            - A (list of int): List containing the first value of each pair.
            - B (list of int): List containing the second value of each pair.
            - N (int): The number of pairs read.
    """
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        # Read a pair of integers for each iteration and assign to A and B
        A[i], B[i] = map(int, input().split())
    return A, B, N

def calculate_answer(A, B, N):
    """
    Calculates the required answer using the arrays A and B of length N.
    
    Approach:
        - Convert lists A, B to numpy arrays for efficient computation.
        - Compute element-wise sum of a and b to get array c.
        - Sort c in descending order to prioritize larger values.
        - Compute the sum of all elements in array b.
        - Select all elements at even indices (0, 2, 4, ...) from sorted c and sum them.
        - Subtract the total sum of b from the sum of selected elements to get the answer.
    
    Args:
        A (list of int): First set of values input.
        B (list of int): Second set of values input.
        N (int): Number of pairs.
        
    Returns:
        int: Computed answer by problem's rules.
    """
    # Convert lists to numpy arrays for vectorized operations
    a = np.array(A)
    b = np.array(B)
    
    # Compute the element-wise sum of arrays a and b
    c = a + b

    # Sort the array c in descending order
    csorted = np.sort(c)[::-1]

    # Compute the total sum of array b
    bsum = np.sum(b)

    # Initialize the sum for elements at even indices from sorted c
    csum = 0
    for i in range(N):
        if i % 2 == 0:
            # Add value at even index
            csum += int(csorted[i])

    # The final answer is the difference between csum and bsum
    ans = csum - bsum
    return ans

def main():
    """
    Main entry point for reading input, processing data, and printing the result.
    """
    # Read input arrays and number of elements
    A, B, N = read_input()
    # Calculate answer based on problem's logic
    ans = calculate_answer(A, B, N)
    # Print the final computed result
    print(ans)

if __name__ == "__main__":
    main()