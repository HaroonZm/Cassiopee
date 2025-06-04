def main():
    """
    Main function to process input and output pairs of items that appear together
    at least 'f' times among groups.
    
    It reads:
    - First line: n (number of groups) and f (minimum frequency).
    - Next n lines: For each group, first an integer m (number of items), then m items.
    
    For each group, it updates a dictionary counting occurrences of each unordered item pair.
    Finally, it outputs all pairs with a frequency >= f.
    """
    # Read the number of groups 'n' and the frequency threshold 'f'
    n, f = map(int, input().split())
    # Dictionary to count the number of times each unordered pair appears
    pair = {}
    
    # Process each group
    for i in range(n):
        # Read each group: first value is the count m, remaining are the items
        m, *items = input().split()
        m = int(m)
        # For each pair of items within the group, count their co-occurrence
        for p in range(m):
            for q in range(p):
                # Unordered pair: sorted tuple to avoid duplication
                key = tuple(sorted([items[p], items[q]]))
                # Increment the counter for this pair
                pair[key] = pair.get(key, 0) + 1
    
    # Gather all item pairs having at least frequency 'f', sorted lexicographically
    ans = sorted(key for key in pair if pair[key] >= f)
    
    # Output the number of qualifying pairs
    print(len(ans))
    # If there are qualifying pairs, output each on a separate line
    if ans:
        for a, b in ans:
            print(a, b)

# Run the main function
if __name__ == "__main__":
    main()