def get_input():
    return input()

def parse_input(input_str):
    return list(map(int, input_str.split()))

def get_a(numbers):
    return numbers[0]

def get_b(numbers):
    return numbers[1]

def get_c(numbers):
    return numbers[2]

def sum_values(a, b, c):
    return a + b + c

def is_bust(total):
    return total >= 22

def print_result(result):
    print(result)

def main():
    inp = get_input()
    nums = parse_input(inp)
    a = get_a(nums)
    b = get_b(nums)
    c = get_c(nums)
    total = sum_values(a, b, c)
    if is_bust(total):
        print_result("bust")
    else:
        print_result("win")

main()