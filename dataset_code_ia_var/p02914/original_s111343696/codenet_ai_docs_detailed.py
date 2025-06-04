import numpy as np

def gaussian_elimination_xor(A: np.ndarray) -> np.ndarray:
    """
    Performs Gaussian elimination over the binary field (GF(2)) on the array A, modifying it in place 
    to form its reduced row-echelon form with respect to the XOR operation.

    Args:
        A (np.ndarray): Input numpy array of integers.

    Returns:
        np.ndarray: The basis of the input array under XOR, after elimination.
    """
    # Loop from the highest bit (59) down to 0
    for i in range(59, -1, -1):
        # Identify which elements have the ith bit set but are less than 2**(i + 1)
        one_digit = (A & (1 << i)) != 0
        pivot_flag = np.where(one_digit & (A < (1 << (i + 1))))[0]
        if len(pivot_flag) == 0:
            # If there is no candidate for pivot in this bit, skip
            continue
        p = pivot_flag[0]
        pivot = A[p]
        # For all rows with the ith bit set, XOR them with the pivot row to clear the bit
        A[one_digit] ^= pivot
        # Restore pivot row since the above also XORed it to zero
        A[p] = pivot
    return A

def calculate_maximum_xor_sum(A: np.ndarray) -> int:
    """
    Calculates the maximum XOR sum achievable by selecting a subset of the input array,
    using the XOR basis reduction algorithm.

    Args:
        A (np.ndarray): Input numpy array of integers.

    Returns:
        int: The maximal achievable subset XOR sum plus the contribution from odd '1's positions.
    """
    # Calculate overall XOR of all elements (cumulative XOR)
    xor = np.bitwise_xor.reduce(A)
    
    # Find bit positions where the number of '1's is odd in the cumulative XOR
    odd_digit = [1 << i for i in range(60) if xor & (1 << i)]

    # Ignore the bits that have an odd count of '1's by masking them from all elements
    for i in odd_digit:
        A = A & (~i)
    
    # Perform the elimination to get XOR basis elements
    A = gaussian_elimination_xor(A)
    
    # The result is sum of fixed bits (odd_digit) plus twice the maximal XOR from basis
    res = sum(odd_digit) + 2 * (np.bitwise_xor.reduce(A))
    return res

def main():
    """
    Main execution function. Reads input, processes data, and prints result.
    """
    # Read the number of elements
    N = int(input())
    # Read the integer array as numpy array of int64
    A = np.array(list(map(int, input().split())), dtype=np.int64)
    # Compute the result using the XOR elimination algorithm
    result = calculate_maximum_xor_sum(A)
    # Print the final result
    print(result)

if __name__ == "__main__":
    main()