def get_input():
    return input()

def get_first_three_chars(s):
    return s[:3]

def display_result(result):
    print(result)

def main():
    user_input = get_input()
    first_three = get_first_three_chars(user_input)
    display_result(first_three)

main()