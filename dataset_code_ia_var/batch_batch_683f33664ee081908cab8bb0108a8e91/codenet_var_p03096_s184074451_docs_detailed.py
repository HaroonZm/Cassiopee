def main():
    """
    Reads input, processes the sequences, and computes the number of valid ways
    to traverse the sequence given the problem's constraints. The result is output modulo MOD.
    """
    MOD = 10 ** 9 + 7  # Define the large modulus as per competitive programming convention

    N = int(input())  # Read the length of the sequence

    clist = []  # Will store the input sequence
    for i in range(N):
        c = int(input())
        clist.append(c)
    # clist now contains the input values

    # Remove consecutive duplicates to create c2list
    c2list = clist[:1]  # Start with the first element
    for i in range(1, N):
        if clist[i] != c2list[-1]:  # Only append if not the same as the last in c2list
            c2list.append(clist[i])
    N2 = len(c2list)  # New length after removing consecutive duplicates

    # cdic keeps a mapping from each unique value to list of its positions in c2list
    cdic = {}
    for i in range(N2):
        c = c2list[i]
        if c not in cdic:
            cdic[c] = [i]
        else:
            cdic[c].append(i)

    # dp[i] stores the number of ways to traverse up to position i in c2list
    dp = [1] + [0] * (N2 - 1)  # Base case: one way to reach the first element

    for i in range(1, N2):
        c = c2list[i]
        dp[i] = dp[i - 1]  # Always can continue from the previous position

        # For current value, add valid jumps from previous occurrences of the same value
        if len(cdic[c]) < 5:
            # For few occurrences, just search in reverse for the most recent before i
            for j in reversed(cdic[c]):
                if j < i:
                    dp[i] += dp[j]
                    break
        else:
            # If there are many occurrences, use binary search to find the rightmost before i
            l, r = 0, len(cdic[c]) - 1
            while l <= r:
                mid = (l + r) // 2
                # Handle lookahead safely: cdic[c][mid+1] may not exist at r=len-1
                next_index = mid + 1
                if cdic[c][mid] < i and (next_index >= len(cdic[c]) or cdic[c][next_index] >= i):
                    dp[i] += dp[cdic[c][mid]]
                    break
                elif cdic[c][mid] >= i:
                    r = mid - 1
                else:
                    l = mid + 1

    print(dp[-1] % MOD)


if __name__ == "__main__":
    main()