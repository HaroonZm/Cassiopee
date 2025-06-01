def process_numbers():
    """
    Continually processes input sequences of integers until a termination condition is met.
    
    For each iteration:
    - Reads an integer n which represents the number of elements in the sequence.
      If n is 0, the function terminates.
    - Reads a sequence of n integers.
    - If the maximum value in the sequence is less than 2, prints 'NA'.
    - Otherwise, counts how many elements are equal to zero (t), then prints n - t + 1.
    
    This function handles input/output interaction and does not return any value.
    """
    while True:
        # Read the number of elements in the sequence
        n = int(input())
        
        # Exit condition: if n is zero, stop processing
        if n == 0:
            break
        
        # Read the sequence of integers and convert them to a list
        s = list(map(int, input().split()))
        
        # Check if the maximum element in the sequence is less than 2
        if max(s) < 2:
            # If condition met, output 'NA' indicating not applicable or no valid result
            print('NA')
        else:
            # Count the number of zeros in the sequence
            t = s.count(0)
            
            # Print the adjusted count according to the problem's logic
            print(n - t + 1)


# Call the function to start processing input
process_numbers()