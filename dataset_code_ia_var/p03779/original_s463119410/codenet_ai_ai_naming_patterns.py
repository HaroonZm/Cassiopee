import math

def get_input_number():
    return int(input())

def calculate_discriminant(value_input):
    return 8 * value_input + 1

def compute_square_root(value_discriminant):
    return math.sqrt(value_discriminant)

def compute_subtract_one(value_sqrt):
    return value_sqrt - 1

def compute_divide_by_two(value_subtract_one):
    return value_subtract_one / 2

def compute_ceiling(value_divided):
    return math.ceil(value_divided)

def main():
    input_number = get_input_number()
    discriminant_value = calculate_discriminant(input_number)
    sqrt_value = compute_square_root(discriminant_value)
    subtract_one_value = compute_subtract_one(sqrt_value)
    divided_value = compute_divide_by_two(subtract_one_value)
    ceiling_result = compute_ceiling(divided_value)
    print(ceiling_result)

main()