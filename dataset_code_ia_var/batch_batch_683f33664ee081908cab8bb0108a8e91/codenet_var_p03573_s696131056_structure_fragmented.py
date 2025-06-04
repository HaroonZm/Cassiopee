def get_input():
    return input().split()

def is_first_equal_second(lst):
    return lst[0] == lst[1]

def is_first_equal_third(lst):
    return lst[0] == lst[2]

def print_element_at_index(lst, idx):
    print(lst[idx])

def handle_first_equal_second(lst):
    print_element_at_index(lst, 2)

def handle_first_equal_third(lst):
    print_element_at_index(lst, 1)

def handle_else(lst):
    print_element_at_index(lst, 0)

def process_input(lst):
    if is_first_equal_second(lst):
        handle_first_equal_second(lst)
    elif is_first_equal_third(lst):
        handle_first_equal_third(lst)
    else:
        handle_else(lst)

def main():
    user_input = get_input()
    process_input(user_input)

main()