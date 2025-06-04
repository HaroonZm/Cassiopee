def process_inputs():
    """
    Main loop to process multiple test cases until a zero is entered.
    For each test case:
      - Reads 'n', the number of subsequent inputs.
      - Collects 'n' lines containing three integers: key, a, and b.
      - Aggregates the value a*b for each unique key.
      - After processing all entries, prints all keys whose total sum >= 1000000.
      - If none or the maximum is below 1000000, prints 'NA'.
    """
    while True:
        # Read the number of input lines for this test case.
        n = int(input())
        # If input is 0, exit the loop and terminate the program.
        if n == 0:
            break

        d = {}  # Dictionary to store the cumulative sum for each key.
        e = []  # List to store the order in which keys first appear.

        # Iterate over the next 'n' lines of input.
        for i in range(n):
            # Read a line, split into integers.
            tmp = list(map(int, input().split(' ')))
            key, a, b = tmp[0], tmp[1], tmp[2]
            value = a * b  # Compute the product.

            # Aggregate the value for the key.
            if key in d:
                d[key] += value
            else:
                d[key] = value
                e.append(key)  # Track order of appearance for potential output.

        # After all entries:
        if not d or max(d.values()) < 1000000:
            # If no value reaches 1,000,000, print 'NA'.
            print('NA')
        else:
            # Print in the order they first appeared any key whose sum >= 1,000,000
            for k in e:
                if d[k] >= 1000000:
                    print(k)

# Call the main function to start processing user input.
process_inputs()