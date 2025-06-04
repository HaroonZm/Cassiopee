def read_input():
    _ = input()
    return input()

def parse_list(input_str):
    return list(map(int, input_str.split()))

def is_even(n):
    return n % 2 == 0

def elements_are_all_even(a_list):
    return all(is_even(a) for a in a_list)

def halve_number(n):
    return n // 2

def halve_list(a_list):
    return [halve_number(a) for a in a_list]

def can_divide_all_evenly(a_list):
    return elements_are_all_even(a_list)

def increment(n):
    return n + 1

def process_halving(a_list):
    count = 0
    if not can_divide_all_evenly(a_list):
        return count
    while can_divide_all_evenly(a_list):
        count = increment(count)
        a_list = halve_list(a_list)
    return count

def main():
    input_str = read_input()
    a_list = parse_list(input_str)
    result = process_halving(a_list)
    print(result)

main()