def process_pairs():
    """
    Reads pairs of integers from user input, computes sums with collision resolution,
    and outputs sorted results. For every input pair (a, b), it tries to add (a+b)
    into a set. If this number already exists in the set, it removes that number
    from the set and continues by adding 1 (i.e., tries (a+b+1)), repeating the process
    until a unique value is found to insert. Finally, outputs all numbers in the set
    in sorted order, each followed by '0'.
    """
    # Initialize an empty set to store the resolved unique values
    m = set()
    # Read the number of test cases or pairs to process
    n = int(input())
    for _ in range(n):
        # Read a pair of integers from input and assign to variables a, b
        a, b = map(int, input().split())
        # Initialize collision resolution increment
        i = 0
        while True:
            # Check if (a + b + i) is already present in the set
            if a + b + i in m:
                # If yes, remove it (toggle off), and check the next integer
                m.remove(a + b + i)
                i += 1
            else:
                # If not present, add the value to the set and break out of the loop
                m.add(a + b + i)
                break
    # Convert the set to a list for sorting
    result = list(m)
    result.sort()
    # Output each number in the sorted list followed by ' 0'
    for num in result:
        print("{} 0".format(num))

# Run the main processing function
process_pairs()