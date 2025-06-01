def process_input():
    """
    Process multiple sets of inputs until a termination condition is met.
    
    For each input set:
    - Reads three integers i, j, k representing counts.
    - If all three are zero, terminates processing.
    - Reads 'input()' number of subsequent lines, each containing four integers x, y, z, r.
    - Processes the data to classify elements into three categories and prints their classifications.
    
    The classification rules are:
    - Elements in set 'a' (unassigned) are printed as 2.
    - Elements in set 'b' (partially assigned) are printed as 0.
    - Elements in set 'c' (fully assigned) are printed as 1.
    """
    while True:
        # Read three integers representing counts of different components
        i, j, k = map(int, raw_input().split())
        
        # Termination condition: if all counts are zero, exit the loop
        if i == 0 and j == 0 and k == 0:
            break
        
        # Total number of elements
        n = i + j + k
        
        # List to store sets of elements that may be partially assigned
        s = []
        
        # Set 'a' contains all element indices initially (from 0 to n-1)
        a = set(range(n))
        
        # Set 'b' will contain elements partially assigned
        b = set()
        
        # Set 'c' will contain elements fully assigned
        c = set()
        
        # Read the number of subsequent lines describing element groups
        num_lines = input()
        
        for _ in range(num_lines):
            # Read the group elements and their status 'r'
            x, y, z, r = map(int, raw_input().split())
            
            # Convert to zero-based indices
            x -= 1
            y -= 1
            z -= 1
            
            if r == 0:
                # If r is 0, add the set of elements to list 's' for later processing
                s.append(set([x, y, z]))
            else:
                # If r is not zero, add these elements to the fully assigned set 'c'
                c.add(x)
                c.add(y)
                c.add(z)
        
        # Process the sets in 's' to identify partially assigned elements
        while True:
            # Flag to determine if any changes were made in this iteration
            f = True
            
            # Iterate over a copy of 's' to avoid modification during iteration
            for lst in s[:]:
                # Check if the intersection of current set and fully assigned 'c' has at least two elements
                if len(lst & c) >= 2:
                    # Remove this set from 's' as it's now processed
                    s.remove(lst)
                    
                    # Remove elements already in 'c' from this set
                    lst = lst - c
                    
                    # If any elements remain, they are partially assigned; add one to 'b'
                    if len(lst) >= 1:
                        b.add(lst.pop())
                    
                    # Since we made changes, set flag to False to continue processing
                    f = False
            
            # If no changes were made, exit the loop
            if f:
                break
        
        # Remove elements assigned to 'b' and 'c' from 'a'
        a = a - b
        a = a - c
        
        # Print classifications for all elements from 0 to n-1
        for i in range(n):
            if i in a:
                # Elements unassigned
                print 2
            elif i in b:
                # Elements partially assigned
                print 0
            else:
                # Elements fully assigned
                print 1

# Call the function to start processing
process_input()