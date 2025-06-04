def uncompress(text, L):
    """
    Uncompresses a compressed text string with repeat patterns up to a maximum length.

    Args:
        text (str): The compressed input string. Patterns are like 3(a) or 2(ab), meaning repeat the string in parentheses x times.
        L (int): The maximum length of the string to uncompress. The function will stop once newText exceeds length L.

    Returns:
        str: The uncompressed string up to a maximum of L+1 characters (for safe boundary checking).
    """
    newText = ''   # Accumulates the uncompressed string
    pos = 0        # Current position in the compressed input

    while True:
        # Stop if we've uncompressed more than L characters
        if len(newText) > L:
            break

        # Stop if we've reached the end of the input text
        if pos >= len(text):
            break

        # If the current character is a digit, it marks a repeat pattern
        if text[pos].isdigit():
            # Find where the repeat number ends
            endDigit = getEndDigit(text, pos)
            num = int(text[pos : endDigit])  # The repeat count

            # If the following character is a '(', it's a pattern like 3(something)
            if text[endDigit] == '(':
                endPar = getEndParenthesis(text, endDigit)
                # Recursively uncompress the text inside the parentheses, reducing L by length so far
                insideText = uncompress(text[endDigit + 1 : endPar - 1], L - len(newText))
                # Repeat the expanded insideText num times
                for _ in range(num):
                    newText += insideText
                    if len(newText) > L:
                        break
                pos = endPar   # Move position to after the closing parenthesis
            else:
                # Simple form: digit followed by a character, e.g., 3a
                newText += (text[endDigit] * num)
                pos = endDigit + 1   # Move position past the repeat character

        else:
            # If not a digit, simply append the current character
            newText += text[pos]
            pos += 1

    return newText

def getEndParenthesis(text, pos):
    """
    Finds the position immediately after the matching closing parenthesis for an opening parenthesis at 'pos'.

    Args:
        text (str): The string to search in.
        pos (int): The index of the opening parenthesis '(' to match.

    Returns:
        int: The index just after the closing parenthesis ')'.
    """
    count = 0  # Tracks parenthesis nesting depth
    while True:
        if text[pos] == '(':
            count += 1
        elif text[pos] == ')':
            count -= 1
        if count == 0:
            # Found the matching closing parenthesis
            return pos + 1
        pos += 1

def getEndDigit(text, pos):
    """
    Finds the index where a contiguous sequence of digits (starting at 'pos') ends.

    Args:
        text (str): The string to search.
        pos (int): The starting index (should be at a digit).

    Returns:
        int: The index just after the sequence of digits (i.e., first non-digit after pos).
    """
    while True:
        if not text[pos].isdigit():
            return pos
        pos += 1

if __name__ == '__main__':
    # Read input until the special '0 0' case is encountered
    while True:
        text, idx = input().strip().split()
        if text == '0' and idx == '0':
            break

        # Uncompress the input text up to the needed length
        text = uncompress(text, int(idx))
        # Print the character at position idx in the uncompressed string, or 0 if out of range
        print(text[int(idx)] if len(text) > int(idx) else 0)