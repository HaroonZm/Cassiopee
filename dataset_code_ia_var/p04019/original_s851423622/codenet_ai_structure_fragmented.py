def get_input():
    return input()

def convert_to_list(s):
    return list(s)

def convert_to_set(lst):
    return set(lst)

def is_all_directions_present(s):
    return 'N' in s and 'S' in s and 'E' in s and 'W' in s

def len_is_three(s):
    return len(s) == 3

def len_is_one(s):
    return len(s) == 1

def len_is_two(s):
    return len(s) == 2

def has_opposite_ns(s):
    return 'N' in s and 'S' in s

def has_opposite_we(s):
    return 'W' in s and 'E' in s

def print_no():
    print('No')

def print_yes():
    print('Yes')

def process_two_directions(s):
    if has_opposite_ns(s):
        print_yes()
    elif has_opposite_we(s):
        print_yes()
    else:
        print_no()

def main_logic():
    s = get_input()
    lst = convert_to_list(s)
    directions = convert_to_set(lst)
    if len_is_three(directions) or len_is_one(directions):
        print_no()
    elif is_all_directions_present(directions):
        print_yes()
    elif len_is_two(directions):
        process_two_directions(directions)
    else:
        print_no()

main_logic()