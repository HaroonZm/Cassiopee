def read_input():
    """
    Read the input from the user. 
    First, an integer N is read, then N integers are read into a list.

    Returns:
        tuple: N (int), the number of elements;
               A (list of int), the list of input integers.
    """
    N = int(input())
    A = [int(input()) for _ in range(N)]
    return N, A

def get_least_significant_zero_counts(A):
    """
    For each number in the list A, calculate the number of trailing zeros in the binary representation (i.e., the position of the lowest set bit).
    Also, track the presence of each possible count up to 43.

    Args:
        A (list of int): List of integers.

    Returns:
        tuple: 
            s (int): XOR of all numbers in A.
            L (list of bool): L[i] is True iff there exists a number in A with exactly i trailing zeros.
    """
    s = 0  # Will store the XOR of all numbers.
    L = [False] * 44  # Flags for existence of at least one number with i trailing zeros (i from 0 to 43).

    for a in A:
        s ^= a  # Compute XOR of all numbers.
        c = 0  # Count number of trailing zeros.
        temp = a
        while temp & 1 == 0:
            c += 1
            temp >>= 1
        L[c] = True  # Mark that a number with c trailing zeros is present.
    return s, L

def minimal_operations_to_zero_xor(s, L):
    """
    Computes the minimal number of operations needed to make the XOR of all numbers zero,
    following the constraints imposed by the original algorithm.
    If this is not possible, returns -1.

    Args:
        s (int): Current XOR of all numbers.
        L (list of bool): Existence flags for trailing zero counts.

    Returns:
        int: The minimal number of required operations, 0 if the XOR is already zero, or -1 if impossible.
    """
    if s == 0:
        return 0  # Already satisfied, no operations required.

    # Convert s to a binary string with leading '0' to match the original algorithm structure.
    ss = "0" + bin(s)[2:]
    ans = 0  # Count of required operations.

    # Traverse the binary string from least-significant bit towards the most significant.
    for i in range(len(ss)-1):
        # Check for transitions (i.e., where bit changes between adjacent positions).
        if ss[-1-i] != ss[-2-i]:
            if L[i]:
                # Operation can be performed at this bit position.
                ans += 1
            else:
                # No number exists allowing operation at this bit position: impossible.
                return -1
    return ans

def main():
    """
    Main execution function. Reads input, computes required values, and prints the result.
    """
    N, A = read_input()
    s, L = get_least_significant_zero_counts(A)
    result = minimal_operations_to_zero_xor(s, L)
    print(result)

if __name__ == "__main__":
    main()