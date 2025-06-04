def get_number_of_inputs():
    return int(input())

def get_single_input():
    return int(input())

def get_input_list(n):
    return [get_single_input() for _ in range(n)]

def gcd_recursive(a, b):
    if is_zero(b):
        return a
    return gcd_recursive(b, a_mod_b(a, b))

def is_zero(value):
    return value == 0

def a_mod_b(a, b):
    return a % b

def compute_lcm(x, y):
    current_gcd = gcd_recursive(x, y)
    return division(x * y, current_gcd)

def division(x, y):
    return x // y

def update_lcm(current_lcm, new_value):
    return compute_lcm(current_lcm, new_value)

def calculate_lcm_for_list(numbers):
    result = get_initial_lcm()
    for number in numbers:
        result = update_lcm(result, number)
    return result

def get_initial_lcm():
    return 1

def print_result(result):
    print(result)

def main():
    n = get_number_of_inputs()
    arr = get_input_list(n)
    lcm_result = calculate_lcm_for_list(arr)
    print_result(lcm_result)

main()