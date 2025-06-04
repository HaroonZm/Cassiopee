def get_table():
    """
    Returns the T9 mapping table used for translating key presses
    to their corresponding characters. Each entry represents the characters
    output by repeatedly pressing a key on a typical phone keypad, following
    the T9 text input system.

    Returns:
        list: A list of strings where each string contains the possible characters for a numeric key.
    """
    return [
        ".,!? ",   # Key '1'
        "abc",     # Key '2'
        "def",     # Key '3'
        "ghi",     # Key '4'
        "jkl",     # Key '5'
        "mno",     # Key '6'
        "pqrs",    # Key '7'
        "tuv",     # Key '8'
        "wxyz"     # Key '9'
    ]


def decode_t9_message(msg, table):
    """
    Decodes a single message encoded with the T9 keypad-like encoding.

    The message consists of a sequence of digits ('1'-'9') and '0' separators. Digits
    indicate repeated presses on the corresponding key, and '0' is used to commit the
    current character and reset for the next one.

    Args:
        msg (str): The input string to decode, representing key presses.
        table (list): The T9 mapping table.

    Returns:
        str: The decoded message.
    """
    ans = ""    # The fully decoded message
    j = 0       # Tracks the current index for repeated key presses
    t = ""      # Temporarily holds the current character being built

    # Iterate through each character (keypress) in the encoded message
    for i in msg:
        if i == "0":
            # '0' indicates selection of current character; append to ans
            ans += t
            j = 0
            t = ""
        else:
            # Convert key character to index for the table (e.g., '2' -> 1)
            key_index = int(i) - 1
            # Select the correct character from the table using current press count (j)
            t = table[key_index][j]
            # Increment the press count and wrap around if necessary
            j += 1
            j %= len(table[key_index])
    return ans


def main():
    """
    Main function to accept user input, process multiple T9 encoded messages,
    and print the decoded messages. It first reads the number of test cases,
    then iteratively processes each message input, printing the decoded result.
    """
    table = get_table()
    n = int(raw_input())
    for _ in range(n):
        # Read a single line message and remove carriage returns if any
        msg = raw_input().replace('\r', '')
        # Decode the encoded message and print the result
        decoded = decode_t9_message(msg, table)
        print decoded


# Entry point for the script execution
if __name__ == "__main__":
    main()