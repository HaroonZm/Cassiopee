def get_input():
    return input()

def parse_input(input_str):
    parts = input_str.split()
    l = int(parts[0])
    r = int(parts[1])
    d = int(parts[2])
    return l, r, d

def is_divisible(x, d):
    return x % d == 0

def increment(x):
    return x + 1

def evaluate_range(l, r, d):
    count = 0
    current = l
    while not is_range_end(current, r):
        if check_and_increment_count(current, d):
            count = update_count(count)
        current = increment(current)
    return count

def is_range_end(current, r):
    return current == r + 1

def check_and_increment_count(current, d):
    return is_divisible(current, d)

def update_count(count):
    return count + 1

def print_result(result):
    print(result)

def main():
    input_str = get_input()
    l, r, d = parse_input(input_str)
    result = evaluate_range(l, r, d)
    print_result(result)

main()