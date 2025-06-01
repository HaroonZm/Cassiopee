def process_numbers():
    """
    Continuously reads input from the user. For each iteration:
    - Reads an integer n.
    - If n is 0, terminates the loop.
    - Reads a list of n integers.
    - If the maximum value in the list is less than 2, prints "NA".
    - Otherwise, prints the count of positive integers in the list plus one.

    This process repeats until the input integer n is 0.
    """
    while True:
        # Read an integer value n from input
        n = int(input())
        
        # If n is zero, exit the loop and end the function
        if n == 0:
            break
        
        # Read a list of n integers from input
        a = list(map(int, input().split()))
        
        # Check if the maximum value in the list is less than 2
        if max(a) < 2:
            # If so, print "NA" and continue to the next iteration
            print("NA")
            continue
        
        # Count how many elements in 'a' are positive
        positive_count = len([x for x in a if x > 0])
        
        # Print the count of positive elements plus one
        print(positive_count + 1)

# Start the process
process_numbers()