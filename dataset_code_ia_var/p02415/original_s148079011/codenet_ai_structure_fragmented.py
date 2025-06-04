def get_input():
    return input()

def swap_case(s):
    return s.swapcase()

def print_result(s):
    print(s)

def main():
    user_input = get_input()
    swapped = swap_case(user_input)
    print_result(swapped)

if __name__ == "__main__":
    main()