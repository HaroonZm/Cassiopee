import sys
from collections import Counter, defaultdict

# Buffered and regular readline for fast I/O
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

def read_int():
    """
    Reads a single integer from standard input.

    Returns:
        int: The integer read from input.
    """
    return int(buff_readline())

def read_int_n():
    """
    Reads a line of space-separated integers from standard input.

    Returns:
        List[int]: The list of integers read from input.
    """
    return list(map(int, buff_readline().split()))

# Global variable for caching power values for rolling hash computations
gpw = None

class RH:
    """
    Rolling Hash (RH) implementation for efficient substring hash computation.
    Useful for comparing slices of bit representations.

    Attributes:
        base (int): Hash base value for rolling hash.
        mod (int): Modulus to avoid integer overflow.
        h (List[int]): Prefix hashes for the sequence.
        pw (List[int]): Precomputed powers of base modulo mod for substring hash calculation.
    """
    def __init__(self, s, base, mod):
        """
        Initializes the rolling hash object for sequence 's'.

        Args:
            s (List[int]): Input sequence (e.g., bits of a number).
            base (int): Hash base.
            mod (int): Modulus for hash calculation.
        """
        self.base = base
        self.mod = mod

        l = len(s)
        self.h = h = [0] * (l + 1)
        tmp = 0
        # Compute prefix hashes for the input sequence
        for i in range(l):
            tmp = (tmp * base + s[i]) % mod
            h[i + 1] = tmp

        # Use global power cache if available, else precompute powers of base
        global gpw
        if gpw is None:
            self.pw = pw = [1] * (len(s) + 1)
            v = 1
            for i in range(l):
                pw[i + 1] = v = v * base % mod
            gpw = pw
        else:
            self.pw = gpw

    def calc(self, l, r):
        """
        Calculates the rolling hash of the subsequence s[l:r].

        Args:
            l (int): Start index (inclusive).
            r (int): End index (exclusive).

        Returns:
            int: Hash value for the subsequence.
        """
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

def slv(N, A, B):
    """
    Finds all valid (k, x) pairs where B is obtained by applying XOR operation to 
    A with a shifted and reversed mask, considering all cyclic rotations and possible bit masks.

    Args:
        N (int): The length of input arrays A and B.
        A (List[int]): The first integer sequence.
        B (List[int]): The second integer sequence.

    Returns:
        List[str]: List of formatted results as 'k x' for all valid pairs.
    """
    # Determine the number of bits required to represent the largest element
    L = max(max(A), max(B)).bit_length()
    ah = []   # List to store rolling hashes of A's bits for each bit position
    bh = []   # List for B's bits
    bnh = []  # List for inverse (not) of B's bits

    for i in range(L):
        ta = []   # i-th bit of A for all elements
        tb = []   # i-th bit of B
        tbn = []  # Inverse of tb
        
        for a, b in zip(A, B):
            ta.append((a >> i) & 1)
            tb.append((b >> i) & 1)
            tbn.append(tb[-1] ^ 1)  # Negate last value in tb

        ah.append(RH(ta, 641, 10**9 + 7))
        bh.append(RH(tb, 641, 10**9 + 7))
        bnh.append(RH(tbn, 641, 10**9 + 7))

    # Array to store computed mask x for each shift k, None if invalid
    x = [0] * N

    # For each bit position, check for all shifts k whether the rotated XOR pattern matches
    for i in range(L):
        for k in range(N):
            # Rolling hash for A's i-th bit after rotating left by k
            l = ah[i].calc(k, N)
            # Rolling hash for A's i-th bit before k
            r = ah[i].calc(0, k)

            if x[k] is None:
                continue  # Already invalidated this k

            # Condition 1: Rotated pattern matches inverse of B
            if l == bnh[i].calc(0, N-k) and r == bnh[i].calc(N-k, N):
                x[k] += 1 << i  # Set this bit in candidate mask x[k]

            # Condition 2: Rotated pattern matches B as is (no bit to set in x[k])
            elif l == bh[i].calc(0, N-k) and r == bh[i].calc(N-k, N):
                pass  # No change to x[k]
            else:
                # No valid match, invalidate shift k
                x[k] = None

    # Collect all valid (k, x) solutions
    ans = []
    for k, xx in enumerate(x):
        if xx is not None:
            ans.append('%d %d' % (k, xx))

    return ans

def main():
    """
    Main function for problem execution.
    Reads input, processes data, and outputs results.
    """
    N = read_int()
    A = read_int_n()
    B = read_int_n()
    print(*slv(N, A, B), sep='\n')

if __name__ == '__main__':
    main()