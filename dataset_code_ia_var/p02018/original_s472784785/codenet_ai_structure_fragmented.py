def get_input():
    return input()

def get_numbers_input():
    return input()

def convert_to_int_list(input_str):
    return list(map(int, input_str.split()))

def is_even(number):
    return number % 2 == 0

def filter_even_numbers(numbers):
    return [x for x in numbers if is_even(x)]

def count_elements(elements):
    return len(elements)

def main():
    read_unused_line()
    numbers = process_numbers()
    evens = filter_even_numbers(numbers)
    count = count_elements(evens)
    print_result(count)

def read_unused_line():
    _ = get_input()

def process_numbers():
    input_str = get_numbers_input()
    return convert_to_int_list(input_str)

def print_result(result):
    print(result)

main()