def abbreviate_string(s):
    """
    Abbreviate a string by showing its first character, then the number of characters 
    between the first and last character, followed by its last character.
    
    For example:
        Input: "localization"
        Output: "l10n"
    
    Parameters:
        s (str): The input string to abbreviate.
    
    Returns:
        str: The abbreviated string. If the string length is less than or equal to 2,
             the function will return the string unchanged.
    """
    # Check if the string is less than or equal to 2 characters
    if len(s) <= 2:
        # No abbreviation needed; return the string as is
        return s
    # Get the first character of the string
    first_char = s[:1]
    # Calculate the number of middle characters (excluding first and last)
    middle_count = len(s) - 2
    # Get the last character of the string
    last_char = s[-1:]
    # Form the abbreviated string as per the rule
    return first_char + str(middle_count) + last_char

if __name__ == "__main__":
    # Prompt the user for input
    s = input("Enter a string to abbreviate: ")
    # Print the abbreviated version of the input string
    print(abbreviate_string(s))