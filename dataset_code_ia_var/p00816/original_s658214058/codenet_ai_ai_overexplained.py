#!/usr/bin/python

# Define a function named 'shred' that takes two parameters: 'num' and 'bit'
def shred(num, bit):
    # Convert the integer 'num' to a string, then to a list of single-character strings (digits)
    num = list(str(num))
    # Initialize a variable 'i' to zero; this will be used as an index for scanning the list
    i = 0
    # Enter a loop that will continue as long as 'bit' is not zero
    while bit:
        # Check if the least significant bit (rightmost bit) of 'bit' is set (i.e., bit is odd here)
        if bit & 1:
            # If it is set, combine the current digit and the next digit into one string
            num[i] += num[i+1]
            # Remove the next digit at position i+1 from the list, as it has been merged
            num.pop(i+1)
            # Do not increment 'i' in this branch because the current index now points to the merged string
        else:
            # If the current bit is not set, simply move to the next digit in the list
            i += 1
        # Right shift the 'bit' variable by 1 to examine the next bit in the next iteration
        bit >>= 1
    # Once the while loop ends, return the modified list of strings (possibly merged digits)
    return num

# Define a function to handle one test case and determine when input ends
def testcase_ends():
    # Read a line of input, split it into whitespace-separated parts,
    # convert each part to an integer, and assign to variables 't' and 'num'
    t, num = map(int, raw_input().split())
    # Check if both 't' and 'num' are zero, which signals end of input
    if t == 0 and num == 0:
        # Return 1 to indicate the end-of-cases condition has been met
        return 1

    # Initialize an empty list 'cut' to store the best splits (as lists of merged digit-strings)
    cut = []
    # Initialize 'best' to -1, representing the best sum found so far
    best = -1
    # For all possible ways to insert or not insert breaks between digits,
    # generate all binary masks from 0 up to (2^(len(str(num))-1))-1
    # Each bit in 'i' represents whether to merge two adjacent digits
    for i in range(1<<(len(str(num))-1)):
        # Call the 'shred' function with the original number and current bitmask 'i'
        curcut = shred(num, i)
        # Convert each merged string segment in 'curcut' to integer and sum them up
        cursum = sum(map(int, curcut))
        # If the sum is greater than 't', skip this combination
        if cursum > t: continue
        # If the sum equals the current best, append this split to the solutions list
        if cursum == best:
            cut.append(curcut)
        # If the sum exceeds the previous best, replace the solutions list with only this split and update 'best'
        elif cursum > best:
            cut = [curcut]
            best = cursum
    # After checking all possible masks:
    # If no solution found (cut is empty), print 'error'
    if not cut:
        print 'error'
    # If more than one equally optimal solution, print 'rejected'
    elif len(cut) > 1:
        print 'rejected'
    # If exactly one optimal solution found, print the sum followed by the merged digit-strings, separated by spaces
    else:
        print best, ' '.join(cut[0])

# Define the main driver function
def main():
    # Loop forever
    while True:
        # Call the test case function; if it returns a true value (non-zero), stop looping and exit
        if testcase_ends():
            return 0

# If this script is being run directly and not imported as a module,
# call the main function to start the program
if __name__ == '__main__':
    main()