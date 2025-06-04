def get_input():
    return input()

def split_input(s):
    return s.split()

def str_to_int_list(lst):
    return [int(x) for x in lst]

def get_numbers():
    s = get_input()
    lst = split_input(s)
    return str_to_int_list(lst)

def count_occurrences(lst, value):
    return lst.count(value)

def is_unique(lst, value):
    return count_occurrences(lst, value) == 1

def print_value(val):
    print(val)

def process_list(lst):
    for i in lst:
        if is_unique(lst, i):
            print_value(i)

def main():
    numbers = get_numbers()
    process_list(numbers)

main()