def find_valid_price(start_price_str, invalid_digit_list):
    current_price_int = int(start_price_str)
    invalid_digit_set = set(invalid_digit_list)
    while not set(str(current_price_int)).isdisjoint(invalid_digit_set):
        current_price_int += 1
    return current_price_int

def execute():
    input_price_str, input_excluded_count_str = input().split()
    input_invalid_digits_list = input().split()
    print(find_valid_price(input_price_str, input_invalid_digits_list))

if __name__ == '__main__':
    execute()