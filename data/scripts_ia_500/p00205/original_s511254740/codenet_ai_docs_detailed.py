def process_inputs():
    """
    This function continuously reads five inputs from the user,
    processes them based on specific rules, and prints the results accordingly.

    The processing logic is as follows:
    - Reads 5 inputs from the user and stores them in a list.
    - Converts the list to a set to determine unique elements.
    - Determines a value 'w' based on presence conditions in the set:
        * If both 1 and 2 are present, then w = 1.
        * Else if both 1 and 3 are present, then w = 3.
        * Otherwise, w = 2.
    - If the number of unique elements is not equal to 2:
        * Prints the number 3 five times (once for each input).
    - Otherwise:
        * Prints 1 if the current element equals w, else prints 2.
    - Continues this process indefinitely until an exception occurs (e.g., EOF).

    Returns:
        None
    """
    while True:
        try:
            # Read five inputs from the user, storing them as integers in a list
            inputs = [int(input()) for _ in range(5)]
            
            # Convert list to set to get unique elements
            unique_elements = set(inputs)
            
            # Determine the value of 'w' based on presence of 1, 2, and 3 in unique_elements
            if 1 in unique_elements and 2 in unique_elements:
                w = 1
            elif 1 in unique_elements and 3 in unique_elements:
                w = 3
            else:
                w = 2
            
            # If the number of unique elements is not exactly 2,
            # print the number 3 for each input
            if len(unique_elements) != 2:
                for _ in inputs:
                    print(3)
            else:
                # If exactly two unique elements,
                # print 1 if the element matches w, otherwise print 2
                for element in inputs:
                    print(1 if element == w else 2)
        
        except Exception:
            # Break the loop on any exception (e.g., end of input)
            break


# Call the function to start processing
process_inputs()