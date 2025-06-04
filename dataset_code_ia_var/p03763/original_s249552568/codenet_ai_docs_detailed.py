def main():
    """
    Reads multiple strings and computes the multiset intersection
    of their lowercase English letters. Outputs the common letters in
    lexicographical order, each repeated the minimum number of times it appears
    in all strings.
    """
    import sys

    # Read the number of strings to process
    n = int(input())
    
    # Initialize two lists of size 26 to count each lowercase letter (a-z)
    # alpnum stores the minimum frequency of each letter found so far
    # alpnumtmp is a temporary array for frequencies in the current string
    alpnum = [0] * 26
    alpnumtmp = [0] * 26
    
    # Read the first string and populate 'alpnum' with its character counts
    tmp = input()
    for j in range(len(tmp)):
        # Map 'a'-'z' to indices 0-25
        alpnum[ord(tmp[j]) - ord("a")] += 1

    # Iterate over the remaining (n-1) strings
    for i in range(1, n):
        # Read the next string
        tmp = input()
        
        # Reset the temporary frequency array
        for j in range(26):
            alpnumtmp[j] = 0

        # Count the frequency of each letter in the current string
        for j in range(len(tmp)):
            alpnumtmp[ord(tmp[j]) - ord("a")] += 1

        # For each character, set the minimum frequency between
        # the current min (alpnum) and this string (alpnumtmp)
        for j in range(26):
            alpnum[j] = min(alpnum[j], alpnumtmp[j])
    
    # Build the answer string using common letters in ascending order
    ans = ""
    for i in range(26):
        # Append the character (i + 97 is ASCII for 'a') alpnum[i] times
        for j in range(alpnum[i]):
            ans += chr(97 + i)
    
    # Output the final answer
    print(ans)

# Call the main function to execute the program
if __name__ == "__main__":
    main()