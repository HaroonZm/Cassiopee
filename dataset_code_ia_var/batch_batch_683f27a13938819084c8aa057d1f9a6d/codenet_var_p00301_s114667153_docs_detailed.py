def encode_number_in_custom_base(w):
    """
    Encode an integer into a custom base-3-like representation.
    
    For a given integer w, construct a string representation where:
      - If the current value mod 3 == 0: append '0' to the result string.
      - If the current value mod 3 == 1: append '+' to the result string.
      - If the current value mod 3 == 2: append '-' to the result string and increment w by 1.
    The process continues by integer-dividing w by 3 in each step, until w becomes zero.
    The final encoded string is reversed before returning.

    Args:
        w (int): The integer to encode.

    Returns:
        str: The custom encoded string representation of the input integer.
    """
    res = ''  # Initialize the result string
    while w > 0:
        if w % 3 == 0:
            res += '0'  # Append '0' when w is divisible by 3
        elif w % 3 == 1:
            res += '+'  # Append '+' when remainder is 1
        else:  # Case when w % 3 == 2
            res += '-'  # Append '-' when remainder is 2
            w += 1      # Increment w to handle the 'carry' in this numeral system
        w //= 3  # Move to the next higher digit
    return res[::-1]  # Reverse the string to get the correct order

def main():
    """
    Main function to read input from user, encode the value, and print the result.
    """
    w = int(input())  # Read integer input from the user
    encoded = encode_number_in_custom_base(w)  # Encode the number
    print(encoded)  # Print the encoded string

if __name__ == "__main__":
    main()