def main():
    """
    Main function to find and print all positions where the rolling hash of the difference array
    of list 'a', when taken from a cyclic shift, matches the rolling hash of the difference array
    of list 'b'. For all matches found, prints the starting index and the XOR needed for the match.
    """

    # Define the modulus for the rolling hash computations (a large prime)
    mod = 2 ** 61 - 1
    
    # Precompute powers of 3 modulo 'mod' up to 400,000 for the rolling hash base
    pow3 = [1] * 400001
    # Precompute modular inverses of powers of 3 modulo 'mod' up to 200,000
    pow3i = [1] * 200001
    p = 1  # Will hold successive powers of 3 modulo mod
    
    # Compute the modular inverse of 3 modulo 'mod' using Fermat's Little Theorem
    i3 = pow(3, mod - 2, mod)
    
    # Precompute pow3[i] = 3^i % mod for i from 1 to 400,000
    for i in range(1, 400001):
        pow3[i] = p = p * 3 % mod

    # Reset p for computing inverse powers
    p = 1
    # Precompute pow3i[i] = (3^i)^-1 % mod for i from 1 to 200,000
    for i in range(1, 200001):
        pow3i[i] = p = p * i3 % mod

    class rolling_hash:
        """
        Rolling hash class for efficiently computing hash values of subarrays.
        Assumes input is a sequence of integers.
        """

        def __init__(self, seq, char_list=None):
            """
            Initializes the rolling hash structure for a given integer sequence.

            Args:
                seq (list of int): The input sequence to preprocess for hashing
                char_list: Ignored, for compatibility.
            """
            seq_size = self.seq_size = len(seq)  # Length of the input sequence
            mod = self.mod = 2 ** 61 - 1  # Use same modulus as above
            # Hash[i] stores the hash value from start up to index (i-1)
            Hash = self.Hash = [0] * (seq_size + 1)
            # Build prefix hashes: Hash[i+1] = hash of first (i+1) elements
            for i in range(seq_size):
                # To distinguish zero elements, use (seq[i] + 1)
                Hash[i + 1] = (Hash[i] + (seq[i] + 1) * pow3[i]) % mod

        def calc_hash(self, l, r):
            """
            Computes the hash value of the subarray seq[l:r].

            Args:
                l (int): Start index of the subarray (inclusive, 0-based)
                r (int): End index of the subarray (exclusive)

            Returns:
                int: Hash value of seq[l:r]
            """
            # Compute raw difference and normalize by multiplying with the inverse power
            return ((self.Hash[r] - self.Hash[l]) * pow3i[l] % self.mod)

    # Read input: n is the length of input arrays a and b
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    memo = []  # To store all valid starting positions

    # Compute the difference array for cyclic shifts of 'a':
    # a_xor = [a[i-1] ^ a[i] for i in range(n)] concatenated with itself for easy rotation
    a_xor = [a[i - 1] ^ a[i] for i in range(n)] + [a[i - 1] ^ a[i] for i in range(n)]
    # Build the rolling hash for double-length a_xor for cyclical comparisons
    a1 = rolling_hash(a_xor)

    # Compute the difference array for 'b' only (no double-length needed)
    b_xor = [b[i - 1] ^ b[i] for i in range(n)]
    b_hash = rolling_hash(b_xor).calc_hash(0, n)

    # Check all possible cyclic shifts by comparing the hashes
    for i in range(n):
        if a1.calc_hash(i, i + n) == b_hash:
            memo.append(i)

    # The first element from b for later XOR correction
    b0 = b[0]

    # For all matching positions, compute the XOR shift x and output (index, x)
    for i in memo:
        x = b0 ^ a[i]
        print(i, x)

main()