import sys

def input():
    """
    Reads a line from standard input and strips the trailing newline character.
    
    Returns:
        str: The input line without the trailing newline.
    """
    return sys.stdin.readline()[:-1]

INF = float("inf")  # Representation of infinity for possible use in algorithms

class BIT:
    """
    Binary Indexed Tree (Fenwick Tree) implementation to support efficient prefix sum queries and updates.

    Attributes:
        N (int): The size of the array for the BIT (number of possible indices).
        bit (List[int]): Internal array representing the Binary Indexed Tree.
    """
    def __init__(self, N):
        """
        Initializes the BIT for N elements (indices 1 to N inclusive).

        Args:
            N (int): Number of elements for the BIT structure.
        """
        self.N = N
        self.bit = [0] * (N + 1)  # 1-based indexing
    
    def add(self, x, a):
        """
        Adds value 'a' to index 'x' in the BIT, and propagates the update.

        Args:
            x (int): The index at which the value should be added (1-based).
            a (int): The value to add to the index.
        """
        while x <= self.N:
            self.bit[x] += a
            x += x & -x  # Move to the next node responsible for this index

    def sum(self, x):
        """
        Computes the prefix sum of elements from index 1 to x.

        Args:
            x (int): The index up to which the sum is computed (inclusive, 1-based).

        Returns:
            int: The sum from index 1 to x.
        """
        ret = 0
        while x != 0:
            ret += self.bit[x]
            x -= x & -x  # Move to parent node
        return ret

# Read input for string length
N = int(input())
# Read the initial string as a list of characters
S = list(input())
# Number of queries to process
Q = int(input())

# Create a BIT for each lowercase letter (total 26 letters)
bit = [BIT(N + 1) for _ in range(26)]

# Initialize BITs, count occurrences of each character at each position
for i in range(N):
    char_index = ord(S[i]) - 97  # Map character 'a'-'z' to 0-25
    bit[char_index].add(i + 1, 1)  # BITs are 1-based indexed

# Process each query
for _ in range(Q):
    parts = input().split()
    q = int(parts[0])

    if q == 1:
        # Update query: Change character at a given position to another character
        i = int(parts[1]) - 1  # 0-based index for position in S
        new_c = parts[2]
        old_c_index = ord(S[i]) - 97  # Index of the old character
        new_c_index = ord(new_c) - 97  # Index of the new character

        # Remove old character count from BIT
        bit[old_c_index].add(i + 1, -1)
        # Update the character in the string
        S[i] = new_c
        # Add new character count to BIT
        bit[new_c_index].add(i + 1, 1)
    else:
        # Query for the number of distinct letters in a substring (range query)
        l = int(parts[1])
        r = int(parts[2])
        distinct_count = 0

        # Iterate over all 26 alphabets to check for presence in the substring [l, r]
        for letter_index in range(26):
            occurrences = bit[letter_index].sum(r) - bit[letter_index].sum(l - 1)
            if occurrences > 0:
                distinct_count += 1
        print(distinct_count)