def get_input():
    return input()

def parse_input(input_line):
    return list(map(int, input_line.split()))

def get_minimum(a, b):
    return min(a, b)

def is_common_divisor(a, b, i):
    return a % i == 0 and b % i == 0

def process_divisors(a, b, k):
    count = 0
    for i in range(get_minimum(a, b), 0, -1):
        if check_and_increment(a, b, i):
            count += 1
            if check_kth(count, k):
                output_result(i)
                break

def check_and_increment(a, b, i):
    return is_common_divisor(a, b, i)

def check_kth(count, k):
    return count == k

def output_result(i):
    print(i)

def main():
    input_line = get_input()
    a, b, k = parse_input(input_line)
    process_divisors(a, b, k)

main()