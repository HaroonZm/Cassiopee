from math import log2, floor

def read_integer_input():
    return int(input())

def compute_log2_floor_of_incremented_value(value):
    incremented_value = value + 1
    log2_value = log2(incremented_value)
    floored_log2_value = floor(log2_value)
    return floored_log2_value

def main():
    user_input_value = read_integer_input()
    result_value = compute_log2_floor_of_incremented_value(user_input_value)
    print(result_value)

main()