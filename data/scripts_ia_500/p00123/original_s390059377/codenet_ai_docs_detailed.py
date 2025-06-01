import sys

def classify_measurements(a: float, b: float) -> str:
    """
    Classify a pair of numerical measurements a and b into categories based on defined threshold values.
    
    Parameters:
    a (float): The first measurement value.
    b (float): The second measurement value.
    
    Returns:
    str: The category label corresponding to the input measurements.
         Possible outputs are 'AAA', 'AA', 'A', 'B', 'C', 'D', 'E', or 'NA'.
         
    Classification rules:
    - 'AAA' if a < 35.5 and b < 71.0
    - 'AA'  if a < 37.5 and b < 77.0
    - 'A'   if a < 40.0 and b < 83.0
    - 'B'   if a < 43.0 and b < 89.0
    - 'C'   if a < 50.0 and b < 105.0
    - 'D'   if a < 55.0 and b < 116.0
    - 'E'   if a < 70.0 and b < 148.0
    - 'NA'  if none of the above conditions are met
    """
    if (a < 35.5) and (b < 71.0):
        return 'AAA'
    elif (a < 37.5) and (b < 77.0):
        return 'AA'
    elif (a < 40.0) and (b < 83.0):
        return 'A'
    elif (a < 43.0) and (b < 89.0):
        return 'B'
    elif (a < 50.0) and (b < 105.0):
        return 'C'
    elif (a < 55.0) and (b < 116.0):
        return 'D'
    elif (a < 70.0) and (b < 148.0):
        return 'E'
    else:
        return 'NA'

def main():
    """
    Read pairs of float values from standard input line by line, classify them using `classify_measurements`,
    and print the resulting classification to standard output.
    
    Input format:
    Each line must contain two space-separated values that can be parsed as floats.
    
    Output:
    Prints one classification label per input line to standard output.
    """
    for line in sys.stdin:
        # Strip any trailing newline or whitespace and split the line into two parts.
        parts = line.strip().split()
        
        # Ensure that exactly two tokens are present in the input line.
        if len(parts) != 2:
            # Skip lines that do not contain exactly two values
            continue
        
        # Parse the two values as floats
        try:
            a = float(parts[0])
            b = float(parts[1])
        except ValueError:
            # Skip lines where conversion to float fails
            continue
        
        # Obtain classification label
        classification = classify_measurements(a, b)
        
        # Output the classification
        print(classification)

if __name__ == '__main__':
    main()