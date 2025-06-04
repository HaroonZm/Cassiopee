def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def to_int_list(str_list):
    return list(map(int, str_list))

def get_numbers():
    user_input = get_input()
    str_list = split_input(user_input)
    int_list = to_int_list(str_list)
    return int_list

def calculate_sum(numbers):
    return sum(numbers)

def check_bust(total):
    return total >= 22

def get_result(is_bust):
    if is_bust:
        return "bust"
    else:
        return "win"

def main():
    numbers = get_numbers()
    total = calculate_sum(numbers)
    is_bust = check_bust(total)
    result = get_result(is_bust)
    print(result)

main()