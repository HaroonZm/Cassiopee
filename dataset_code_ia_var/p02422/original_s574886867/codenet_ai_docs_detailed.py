def process_string_commands():
    """
    Reads a string and a set of commands from input, processes each command on the string,
    and prints results for 'print' commands.

    The function expects the following input format:
    - The first line contains the initial string `s`.
    - The second line contains an integer `n`, the number of commands.
    - The next `n` lines each contain a command in one of the following formats:
        - "replace a b p": Replace substring s[a:b+1] with p.
        - "reverse a b": Reverse the substring s[a:b+1].
        - "print a b": Print the substring s[a:b+1].
    """
    # Read the initial string
    s = input()
    # Read the number of commands to process
    n = int(input())

    # Read and parse all commands, storing them as lists of string tokens
    l = []
    for i in range(n):
        # Each command is split into a list of strings
        l.append(list(map(str, input().split())))

    # Process each command in the order they were given
    for i in range(len(l)):
        command = l[i][0]       # The command type: 'replace', 'reverse', or 'print'
        a = int(l[i][1])        # Starting index (inclusive)
        b = int(l[i][2])        # Ending index (inclusive)
        c = s[a:b+1]            # Current substring selected by indices a to b (inclusive)

        if command == "replace":
            # For 'replace', get the replacement substring from the command
            replacement = l[i][3]
            # Update the string by replacing the specified substring with the new one
            s = s[:a] + replacement + s[b+1:]
        elif command == "reverse":
            # For 'reverse', reverse the specified substring and integrate it back into s
            reversed_substring = c[::-1]
            s = s[:a] + reversed_substring + s[b+1:]
        elif command == "print":
            # For 'print', output the selected substring
            print(c)

# Call the function to execute the processing logic
process_string_commands()