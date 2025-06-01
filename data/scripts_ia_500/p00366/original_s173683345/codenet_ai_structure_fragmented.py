def get_input_number():
    return int(input())

def get_input_numbers(count):
    numbers = []
    for _ in range(count):
        numbers.append(get_input_number())
    return numbers

def is_divisor(x, i):
    return x % i == 0

def find_divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if is_divisor(x, i):
            divisors.append(i)
    return tuple(divisors)

def find_divisor_index(divisors, value):
    index = 0
    while divisors[index] < value:
        index += 1
    return index

def calculate_difference_sum(numbers, divisors):
    total_diff = 0
    for number in numbers:
        idx = find_divisor_index(divisors, number)
        total_diff += divisors[idx] - number
    return total_diff

def main():
    N = get_input_number()
    t = get_input_numbers(N)
    max_value = max(t)
    div = find_divisors(max_value)
    result = calculate_difference_sum(t, div)
    print(result)

main()