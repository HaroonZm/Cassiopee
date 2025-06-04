def get_input():
    return input()

def convert_to_int(value):
    return int(value)

def subtract_from_one(value):
    return 1 - value

def display_result(result):
    print(result)

def main():
    user_input = get_input()
    int_value = convert_to_int(user_input)
    result = subtract_from_one(int_value)
    display_result(result)

main()