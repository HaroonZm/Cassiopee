import sys

def solve():
    """
    Reads an input word to search for, then reads multiple lines of text,
    counting the number of times the word appears (case-insensitive).
    Reading stops when the line "END_OF_TEXT" is encountered, after which
    the function prints the count.

    The search is case-insensitive and words are split using whitespace.
    """
    # Read target word to search for
    t = raw_input()  # In Python 2, raw_input() reads a line from standard input as a string

    total = 0  # Initialize the number of occurrences
    while True:
        # Read a line of the input
        strr = raw_input()
        # If end of text is reached, output the total count and stop
        if strr == "END_OF_TEXT":
            print total
            return
        # Split the line into words using whitespace as separator
        single = strr.split()
        # Iterate over each word in the line
        for i in single:
            # If the current word equals the search word (case-insensitive), increment the count
            if i.lower() == t:
                total += 1

if __name__ == "__main__":
    solve()