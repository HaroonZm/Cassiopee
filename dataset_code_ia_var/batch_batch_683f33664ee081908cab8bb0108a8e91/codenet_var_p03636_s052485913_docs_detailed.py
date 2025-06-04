def abbreviate_string(S):
    """
    Abbreviates a string following the pattern:
    First character + number of characters between first and last + last character.
    For example, 'internationalization' -> 'i18n'.
    
    Parameters:
        S (str): The input string to abbreviate.
        
    Returns:
        str: The abbreviated string.
    """
    # Handle case where string length is less than or equal to 2
    if len(S) <= 2:
        # For very short strings, return the string as is
        return S
    # Construct the abbreviation
    # - S[0]: first character
    # - len(S) - 2: number of characters between first and last
    # - S[-1]: last character
    abbreviation = S[0] + str(len(S) - 2) + S[-1]
    return abbreviation

if __name__ == "__main__":
    # Prompt the user to input a string
    input_string = str(input())
    # Print the abbreviated version of the input string
    print(abbreviate_string(input_string))