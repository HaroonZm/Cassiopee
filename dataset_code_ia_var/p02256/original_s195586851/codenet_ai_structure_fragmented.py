def is_divisible(a, b):
    return a % b == 0

def compute_remainder(a, b):
    return a % b

def swap(a, b):
    return b, a

def recursive_gcd(a, b):
    if is_divisible(a, b):
        return b
    else:
        return recursive_gcd(*swap(b, compute_remainder(a, b)))

def read_input():
    return raw_input()

def split_input(input_str):
    return input_str.split()

def convert_to_ints(str_list):
    return map(int, str_list)

def get_numbers():
    input_str = read_input()
    splitted = split_input(input_str)
    nums = convert_to_ints(splitted)
    return list(nums)

def display_result(result):
    print(result)

def process():
    numbers = get_numbers()
    a, b = numbers[0], numbers[1]
    result = recursive_gcd(a, b)
    display_result(result)

def main():
    process()

if __name__ == '__main__':
    main()