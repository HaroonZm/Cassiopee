def ssplit(s):
    # Initialize a temporary variable 'tp' with value 0 (not used in the logic, but included from original code)
    tp = 0
    # Initialize an empty string 'tmp' which will be used to collect digit characters
    tmp = ""
    # Initialize an empty list 'ret' which will store processed tuples representing numbers and non-digit characters
    ret = []
    # Iterate through each character 'c' in the input string 's'
    for c in s:
        # Check if the current character 'c' is a digit character (0-9)
        if c.isdigit():
            # If it is a digit, concatenate it to the 'tmp' string to build the complete number
            tmp += c
        else:
            # If the character is not a digit (i.e., it's a non-digit character)
            # Check if 'tmp' is not an empty string, which means we've previously collected digits to make a number
            if tmp != "":
                # Convert the string of digits in 'tmp' to an integer using int()
                # Append a tuple (0, integer_value) to 'ret'. 0 indicates it's a number.
                ret.append((0, int(tmp)))
                # Reset 'tmp' to an empty string to start collecting the next number if any
                tmp = ""
            # For the current non-digit character, get its Unicode code point using ord()
            # Append a tuple (1, code_point) to 'ret'. 1 indicates it's a non-digit character.
            ret.append((1, ord(c)))
    # After iterating over all characters, it's possible that there is still an accumulated number in 'tmp'
    if tmp != "":
        # Convert the final number in 'tmp' to an integer and append as a tuple (0, integer_value)
        ret.append((0, int(tmp)))
    # Return the resulting list of tuples 'ret'
    return ret

# Read a line of input from the user, which is expected to be an integer specifying the number of subsequent lines
n = int(input())
# Read another line of input from the user, expected to be the string to be split and used as the reference
s = ssplit(input())
# For each value in the range from 0 up to (but not including) n (loop will execute n times)
for i in range(n):
    # Read a line of input from the user for comparison
    z = ssplit(input())
    # Compare the list 'z' to the list 's' using the >= operator, which compares the two lists lexicographically
    # If z is greater than or equal to s, print '+'
    if z >= s:
        print('+')
    # Otherwise (z is less than s), print '-'
    else:
        print('-')