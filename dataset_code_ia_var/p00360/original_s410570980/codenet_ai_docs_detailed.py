import sys

def main():
    """
    Main function to compute the lexicographically smallest string
    after at most k adjacent swaps on a given string input.
    Reads input and outputs the final string.
    """
    # Utility function to read an integer from stdin quickly
    NI = lambda : int(sys.stdin.readline())
    # Utility function to read a string from stdin (removes endline chars)
    SI = lambda : sys.stdin.readline().rstrip()

    # Read the string s and swap limit k
    s = SI()
    n = len(s)
    k = NI()

    def conv(x):
        """
        Converts a lowercase character to its integer representation (0-25).
        Args:
            x (str): Single lowercase character.
        Returns:
            int: Integer in [0, 25] corresponding to the character.
        """
        return ord(x) - ord('a')

    # Fenwick Tree (Binary Indexed Tree) initialization, size n+1 for 1-based index
    bit = [0] * (n+1)

    def bit_add(i):
        """
        Increments the value at index 'i' in BIT.
        Used to record that the position has been used for a move.
        Args:
            i (int): 1-based index in the Fenwick Tree.
        """
        while i <= n:
            bit[i] += 1
            i += i & (-i)

    def bit_sum(i):
        """
        Computes prefix sum up to index 'i' in BIT.
        Returns the total number of performed moves that cover indices < i.
        Args:
            i (int): 1-based index in the Fenwick Tree.
        Returns:
            int: Prefix sum up to index 'i'.
        """
        ret = 0
        while i > 0:
            ret += bit[i]
            i -= i & (-i)
        return ret

    # z marks which characters have been moved already
    z = [0] * n  # 1 if character at that index is used
    # top holds the frontmost available index in the string for each letter
    top = [-1] * 26  # For each letter 'a'-'z', its smallest index in s not yet used
    # nxt holds the "next" occurrence position in s for each index
    nxt = [-1] * n   # For each position, the next occurrence of that character
    # bef temporarily holds, for each character, the previous occurrence index
    bef = [-1] * 26

    # Prepare the 'top', 'nxt', and 'bef' arrays
    for i in range(n):
        cv = conv(s[i])
        # Link the previous occurrence to this position
        if bef[cv] >= 0:
            nxt[bef[cv]] = i
        bef[cv] = i
        # Set top for characters where it's their first occurrence
        if top[cv] < 0:
            top[cv] = i

    ans = []  # Resulting answer as a list of characters

    # Greedy algorithm: in each step, try to promote the lexicographically smallest character to the front, as long as k allows it
    while k > 0:
        for i in range(26):  # For each letter from 'a' to 'z'
            if top[i] < 0:
                continue  # No available occurrence for this letter
            p = top[i]  # Index of this letter's frontmost available occurrence
            # Number of swaps required is the distance minus already promoted characters to its left
            cost = p - bit_sum(p+1)
            if cost <= k:
                # Move this character to the current output position
                ans.append(chr(ord('a')+i))
                z[top[i]] = 1  # Mark as used
                k -= cost     # Use up the swaps
                top[i] = nxt[top[i]]  # move to next occurrence of this letter
                bit_add(p+1)           # Register move in BIT (1-based index)
                break
        else:
            # No more moves possible within k
            break

    # Append the unused characters in their original order
    for i in range(n):
        if z[i] == 0:
            ans.append(s[i])

    # Output the final character list as a string
    print(*ans, sep='')

if __name__ == '__main__':
    main()