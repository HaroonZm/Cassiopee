def get_input():
    return input()

def check_exit_condition(n):
    return n == 0

def get_numbers():
    return list(map(int, input().split()))

def max_less_than_two(numbers):
    return max(numbers) < 2

def count_positive(numbers):
    return len([i for i in numbers if i > 0])

def print_na():
    print("NA")

def print_result(count):
    print(1 + count)

def main_loop():
    while True:
        n = get_input()
        if check_exit_condition(int(n)):
            break
        numbers = get_numbers()
        if max_less_than_two(numbers):
            print_na()
            continue
        result = count_positive(numbers)
        print_result(result)

main_loop()