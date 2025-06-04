user_input_string = input()

is_palindrome = user_input_string == user_input_string[::-1]

output_character_if_palindrome = "D"
output_character_if_not_palindrome = "H"

if is_palindrome:
    print(output_character_if_palindrome)
else:
    print(output_character_if_not_palindrome)