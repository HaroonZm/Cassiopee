def classify_japanese_counter_word(number_str):
    """
    Classifies the given input according to the Japanese counter word endings.
    
    Parameters:
        number_str (str): The input number as a string.
    
    Returns:
        str: One of 'hon', 'pon', or 'bon' according to the last digit.
    """
    # List of last digits corresponding to 'hon'
    hon_endings = [2, 4, 5, 7, 9]
    # List of last digits corresponding to 'pon'
    pon_endings = [0, 1, 6, 8]
    # Last digit corresponding to 'bon'
    bon_ending = 3

    # Extract the last character (digit) from the input string
    last_char = number_str[-1]
    # Convert the last character to an integer for classification
    last_digit = int(last_char)

    # Decide the output based on the last digit
    if last_digit in hon_endings:
        return 'hon'
    elif last_digit in pon_endings:
        return 'pon'
    elif last_digit == bon_ending:
        return 'bon'

def main():
    """
    Main function to receive user input and print the Japanese counter classification.
    """
    # Receive input from user as a string
    n = input()
    # Classify using the defined function and print the result
    print(classify_japanese_counter_word(n))

# Execute main function if this script is run directly
if __name__ == "__main__":
    main()