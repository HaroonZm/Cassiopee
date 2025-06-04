import random

def read_inputs():
    """
    Reads the input values:
    - First line: N and X
    - Next N lines: binary strings representing elements of A

    Returns:
        N (int): Number of elements in A
        X (str): Upper bound binary string
        A (list[int]): List of integers derived from binary strings
    """
    mod = 998244353  # Not used here, but present for completeness if needed by caller
    N, X = input().split()
    N = int(N)
    A = []
    for _ in range(N):
        # Convert the binary input string to its integer value
        A.append(int(input(), 2))
    return N, X, A

def initialize_basis(A, X):
    """
    Initializes the basis array 'data' for the given list A and upper bound X.

    Args:
        A (list[int]): List of sorted integers
        X (str): Upper bound binary string

    Returns:
        data (list[int]): Basis for binary vectorspace, up to length M+1
        M (int): Length of the binary representation - 1
    """
    # Compute the length for the basis according to the highest bit in X and A
    a = A[-1]
    M = max(len(X)-1, a.bit_length()-1)
    data = [0] * (M+1)
    n = a.bit_length() - 1
    # Initialize basis leaders
    for i in range(M-n, -1, -1):
        data[i+n] = a << i
    return data, M

def insert_into_basis(A, data, M):
    """
    Reduces each element of A with respect to the current basis 'data', 
    and updates 'data' to be a basis of the span of the input A (except largest element).

    Args:
        A (list[int]): Sorted list of integers to process (excluding the largest)
        data (list[int]): The basis array to update
        M (int): Length of the binary representation - 1

    Returns:
        None; modifies 'data' in-place.
    """
    N = len(A)
    for i in range(N-1):
        a = A[i]
        flag = True
        while flag:
            n = a.bit_length()
            # Minimize a using data (basis)
            for j in range(n-1, -1, -1):
                a = min(a, a ^ data[j])
            if a != 0:
                # Insert new vector into basis at the correct bit length
                data[a.bit_length()-1] = a
                id = a.bit_length() - 1
                # Try to "push" this a upward to fill higher basis slots, creating linear independence
                while data[id+1] == 0:
                    candidate = (data[id] << 1) ^ a
                    candidate2 = data[id] << 1
                    data[id+1] = min(candidate, candidate2)
                    # If we successfully filled the slot with something new
                    if data[id+1]:
                        id += 1
                    else:
                        flag = False
                else:
                    # Move a up by shifting left in the basis structure
                    a = data[id] << 1
            else:
                # Finished processing this vector
                break

def build_rank_prefix(data, M):
    """
    Builds an array data2 where data2[i] is the number of nonzero vectors in the 
    basis up to index i-1. This is used to count the degrees of freedom (rank).

    Args:
        data (list[int]): The basis array.
        M (int): Length of the binary representation - 1.

    Returns:
        data2 (list[int]): Prefix sum array of basis non-zeros.
    """
    data2 = [0] * (M+1)
    for i in range(M+1):
        data2[i] = (data[i] != 0)
    # Prefix sum computation
    for i in range(1, M+1):
        data2[i] += data2[i-1]
    # Add an initial 0 for easier 1-based indexing
    data2 = [0] + data2
    return data2

def count_xor_combinations(data, data2, X, mod=998244353):
    """
    Calculates the number of nonempty subsets of A whose XOR is less than or equal to X,
    using the basis 'data' and prefix sum of ranks 'data2'.

    Args:
        data (list[int]): The basis array.
        data2 (list[int]): Prefix sum of basis non-zeros.
        X (str): The upper bound as a binary string.
        mod (int): Modulus for calculation.

    Returns:
        ans (int): The answer, modulo mod.
    """
    x = 0  # This will keep the current xor we're testing through the bits of X
    ans = 0  # Count of valid solutions
    n = len(X) - 1
    for i in range(len(X)):
        if X[i] == "1":
            # If currently x has bit set at position n-i
            if (x >> (n-i)) & 1 == 1:
                if data[n-i]:
                    # If basis exists at this position, add number of subset with lower bits
                    ans += pow(2, data2[n-i], mod)
                    ans %= mod
            else:
                # There are solutions by setting this bit to 0, add their count
                ans += pow(2, data2[n-i], mod)
                ans %= mod
                # If possible, set this bit using basis vector to keep track of path
                if data[n-i]:
                    x = x ^ data[n-i]
                else:
                    break
        else:
            # If bit in X is 0
            if (x >> (n-i)) & 1 == 1:
                if data[n-i]:
                    x = x ^ data[n-i]
                else:
                    break
            else:
                continue
    else:
        # If the loop completes without break (i.e., x <= X holds), count it as a valid answer
        ans += 1
        ans %= mod
    return ans

def main():
    """
    Main function responsible for reading inputs, processing the basis, 
    and computing the number of valid xor subsets <= X.
    """
    mod = 998244353
    # Step 1: Read all inputs (N, X, and A)
    N, X, A = read_inputs()

    # Step 2: Sort the array A in increasing order (for efficient basis construction)
    A.sort()

    # Step 3: Initialize the basis with the largest element
    data, M = initialize_basis(A, X)

    # Step 4: Insert the remaining vectors into the basis to maximize linear independence
    insert_into_basis(A, data, M)

    # Step 5: Construct prefix sums of ranks of the basis
    data2 = build_rank_prefix(data, M)

    # Step 6: Calculate the answer using the basis and data2
    ans = count_xor_combinations(data, data2, X, mod)

    # Output the answer
    print(ans)

if __name__ == "__main__":
    main()