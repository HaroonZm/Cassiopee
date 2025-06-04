def get_user_input():
    return input()

def perform_swapcase(s):
    return s.swapcase()

def print_result(result_str):
    print(result_str)

def main():
    user_input = get_user_input()
    swapped = perform_swapcase(user_input)
    print_result(swapped)

main()